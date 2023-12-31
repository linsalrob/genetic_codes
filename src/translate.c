//
// Created by edwa0468 on 29/12/2023.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include <pthread.h>
#include "colours.h"
#include "error.h"
#include "seqs_to_ints.h"
#include "translate.h"

void * threaded_translate_sequence(void *thrargs) {
    /*
     * enc: the encoded original sequence
     * protein: a char * that has been malloc'd to include enough space for the protein (1/3 of the sequence)
     * start_frame: the frame to translate
     * translation_table: the translation table to use
     *
     * translate a sequence 3 bases at a time starting at start_frame
     *   start_frame = 1 : [1,2,3]
     *   start_frame = 2 : [4,5,6]
     */
    thread_args_t *thread_args = (thread_args_t *) thrargs;
    int ppos = 0;
    int dna_start = thread_args->start_frame+1; // the additional +1 is so that we are 1-indexed
    for (int i=thread_args->start_frame; i < thread_args->len - 2; i+=3) {
        int posn = (thread_args->enc[i] << 4) + (thread_args->enc[i + 1] << 2) + thread_args->enc[i + 2];
        if (CODONS[thread_args->translation_table][posn] == '*') {
            thread_args->aa_stops[thread_args->num_stops] = ppos;
            thread_args->bp_starts[thread_args->num_stops] = dna_start;
            thread_args->bp_stops[thread_args->num_stops] = i + 2 + 1; // the additional +1 is so that we are 1-indexed
            dna_start = thread_args->bp_stops[thread_args->num_stops] + 1;
            thread_args->num_stops++;
        }
        thread_args->protein[ppos++] = CODONS[thread_args->translation_table][posn];
    }
    // we save the last position as a stop so we can use it below in the iterator
    thread_args->aa_stops[thread_args->num_stops] = ppos;
    thread_args->bp_starts[thread_args->num_stops] = dna_start;
    thread_args->bp_stops[thread_args->num_stops] = thread_args->len+1;
    return NULL;
}

void parallel_translate(translate_t * data) {
    /*
     * translate the DNA sequence using threading
     */

    if (data->verbose)
        fprintf(stderr, "%sRead %s with length %ld%s\n", BLUE, data->name, data->len, ENDC);
    unsigned char *enc = malloc((data->len + 1) * sizeof(unsigned char));
    if (!enc)
        error_and_exit("Unable to allocate memory for the encoded sequence");

    encode_sequence(data->dnaseq, enc);
    unsigned char *rcenc = malloc((data->len + 1) * sizeof(unsigned char));
    if (!rcenc)
        error_and_exit("Unable to allocate memory for the reverse complement");

    reverse_complement_sequence(enc, rcenc, data->len);

    // print_translated_sequence(unsigned char* enc, char * protein, int start_frame, int translation_table)
    pthread_t threads[6];
    int starts[6] = {0, 0, 0, 0, 0, 0};
    thread_args_t **thread_args = malloc(6 * sizeof(thread_args_t *));
    if (!thread_args)
        error_and_exit("Unable to allocate memory for the threading\n");

    for (int thread = 0; thread < 6; thread++) {
        thread_args[thread] = malloc(sizeof(thread_args_t));
        if (!thread_args[thread])
            error_and_exit("Unable to allocate memory for one thread\n");

        thread_args[thread]->protein = malloc(((data->len / 3) + 6) * sizeof (char));
        if (!thread_args[thread]->protein)
            error_and_exit("Unable to allocate memory for one thread's protein\n");

        if (data->verbose)
            fprintf(stderr, "%s\tThread is %d - setting frame%s\n", GREEN, thread, ENDC);
        if (thread < 3) {
            thread_args[thread]->enc = enc;
            thread_args[thread]->start_frame = thread;
            thread_args[thread]->strand = '+';
        } else {
            thread_args[thread]->enc = rcenc;
            thread_args[thread]->start_frame = thread - 3;
            thread_args[thread]->strand = '-';
        }

        thread_args[thread]->aa_stops = malloc((data->len + 1) * sizeof (int));
        if (!thread_args[thread]->aa_stops)
            error_and_exit("Unable to allocate memory for one thread's stops\n");


        thread_args[thread]->bp_starts = malloc((data->len + 1) * sizeof (int));
        thread_args[thread]->bp_stops = malloc((data->len + 1) * sizeof (int));
        if (!thread_args[thread]->bp_stops)
            error_and_exit("Unable to allocate memory for one thread's base-pair level stops\n");

        thread_args[thread]->num_stops = 0;
        thread_args[thread]->thread_number = thread;
        thread_args[thread]->seqname = malloc((strlen(data->name) + 2) * sizeof (char));
        thread_args[thread]->seqname = strdup(data->name);
        thread_args[thread]->translation_table = data->translation_table;
        thread_args[thread]->len = data->len;

        if (data->verbose)
            fprintf(stderr, "%s\tissuing thread %d%s\n", GREEN, thread, ENDC);
        starts[thread] = pthread_create(&threads[thread], NULL, &threaded_translate_sequence, (void *) thread_args[thread]);
        if (starts[thread])
            fprintf(stderr, "%sERROR: Starting thread %d returned the error code %d%s\n", RED, thread, starts[thread],
                    ENDC);
    }

    // wait for the threads to finish and create two associative arrays: name and sequence

    for (int thread = 0; thread < 6; thread++) {
        pthread_join(threads[thread], NULL);
        int seq_from = 0;

        if (data->verbose) {
            printf("%s\n%s\n", PINK, thread_args[thread]->seqname);

            for (int i = 0; i <= thread_args[thread]->len / 3; i++)
                printf("%d", i % 10);
            printf("\n%s%s\n", thread_args[thread]->protein, ENDC);
        }

        if (!thread_args[thread]->protein)
            fprintf(stdout, "%sERROR: thread_args[thread]->protein not defined for thread %d%s", RED, thread, ENDC);
        // we define this for _all_ the proteins, and then define the correct length for each ORF once we know it
        char * substr = malloc((strlen(thread_args[thread]->protein) + 2) * sizeof (char));
        if (!substr)
            error_and_exit("Unable to allocate memory for one thread's substring\n");

        // note: above, we save the last stop as the last protein position
        for (int i=0; i <= thread_args[thread]->num_stops; i++) {
            int seq_to = thread_args[thread]->aa_stops[i] + 1; // we want to include the stop codon
            if (seq_from == 0)
                strncpy(substr, thread_args[thread]->protein, seq_to);
            else
                strncpy(substr, thread_args[thread]->protein + seq_from, seq_to - seq_from);

            substr[seq_to - seq_from] = '\0';

            data->orfs[data->num_orfs] = malloc(((seq_to - seq_from) + 1) * sizeof (char));
            if (!data->orfs[data->num_orfs])
                error_and_exit("Unable to allocate memory for the number of ORFs\n");

            strcpy(data->orfs[data->num_orfs], substr);

            size_t needed = snprintf(NULL, 0, "%s frame %c%d %d %d",
                                     thread_args[thread]->seqname,
                                     thread_args[thread]->strand,
                                     thread_args[thread]->start_frame + 1,
                                     thread_args[thread]->bp_starts[i],
                                     thread_args[thread]->bp_stops[i]
            );
            data->orf_names[data->num_orfs] = malloc(needed+2);
            if (!data->orf_names[data->num_orfs])
                error_and_exit("Unable to allocate memory for the ORF's name\n");

            sprintf(data->orf_names[data->num_orfs], "%s frame %c%d %d %d",
                    thread_args[thread]->seqname,
                    thread_args[thread]->strand,
                    thread_args[thread]->start_frame + 1,
                    thread_args[thread]->bp_starts[i],
                    thread_args[thread]->bp_stops[i]
            );
            seq_from = seq_to;
            data->num_orfs++;
        }
        free(substr);
        free(thread_args[thread]->bp_starts);
        free(thread_args[thread]->bp_stops);
        free(thread_args[thread]->aa_stops);
        free(thread_args[thread]->protein);
        free(thread_args[thread]);
    }

    free(enc);
    free(rcenc);
    free(thread_args);
}