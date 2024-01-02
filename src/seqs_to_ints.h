
#ifndef GENETIC_CODES_SEQS_TO_INT_H
#define GENETIC_CODES_SEQS_TO_INT_H

/*
 * convert a kmer of A,T,G,C into a uint64_t
 */
uint64_t kmer_encoding(char*, int, int);

/*
 * decode a uint64_t into a kmer of A,T,G,C. We need to know how long k is otherwise it will be left filled with A's!
 */

char* kmer_decoding(uint64_t, int);

/*
 * find the next primer for a sequence
 */
uint64_t next_kmer_encoding(char*, int, int, uint64_t);

int encode_base(int);
int decode_base(int);
void encode_sequence(char *, unsigned char *);
void reverse_complement_sequence(unsigned char*, unsigned char *, int);

#endif
