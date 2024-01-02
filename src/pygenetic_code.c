#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdbool.h>
#include "pygenetic_code.h"
#include "error.h"
#include "translate.h"
#include "colours.h"

static PyObject * translate(PyObject *self, PyObject *args) {
    /*
    * translate a sequence given in args using translation table and return all orfs
    */

    const char * seq;
    int translation_table;
    int verbose = 0;
    Py_ssize_t seqlen;
    if (!PyArg_ParseTuple(args, "s#i|i", &seq, &seqlen, &translation_table, &verbose)) {
        PyErr_SetString(PyExc_RuntimeError, "Could not parse the arguments to translate");
        return NULL;
    }

    // invalid codon tables: 0, 7, 8, 17, 18, 19, 20,  > 31
    if (translation_table < 0 || translation_table > 31 ||
        translation_table == 7 || translation_table == 8 ||
        (translation_table > 16 && translation_table < 21)) {
        char * errmsg = malloc(100*sizeof(char));
        memset(errmsg, 0, 100*sizeof(char));
        sprintf(errmsg, "Translation table %d is not valid. It can not be <0, 7, 8, 17-20, or >31", translation_table);
        fprintf(stderr, "%s%s%s\n", RED, errmsg, ENDC);
        PyErr_SetString(PyExc_ValueError, errmsg);
        return NULL;
    }

    translate_t *sequence = malloc(sizeof (translate_t));
    if (!sequence)
            error_and_exit("Unable to allocate memory for the sequence struct object\n");

    sequence->dnaseq = malloc((seqlen + 1) * sizeof (char));
    if (!sequence->dnaseq)
            error_and_exit("Unable to allocate memory for the DNA sequence\n");

    strcpy(sequence->dnaseq, seq);
    sequence->dnaseq[seqlen+1] = '\0';
    sequence->name = "translated_sequence";
    sequence->verbose = (bool) verbose;
    sequence->len = (int) seqlen;
    sequence->translation_table = translation_table;
    // these initiate variables set below
    sequence->num_orfs = 0;
    sequence->orfs = malloc(seqlen * 2 * sizeof (char)); // translation is x2 for fwd/rev, x3 for each frame, but /3 for amino acidds
    if (!sequence->orfs)
            error_and_exit("Unable to allocate memory for the sequence ORFs\n");

    // the sequence name is "seq_name frame +x start stop"
    // assuming sequence length less than 1e9 (10 characters each for start/stop), we need 20 + seq_name + 7 for " frame " + 2 for [+/-]x + 2 spaces
    // * the number of ORFs we find. Assuming most orfs are 1 per kb of the sequence should be about seqlen /300
    int seqnamesize = ((50 * (seqlen/10)) * sizeof (char));

    sequence->orf_names = malloc(seqnamesize); // somewhat randomly allocate the same size of the memory as above

    if (!sequence->orf_names)
            error_and_exit( "Unable to allocate memory for the sequence ORF names\n");

    parallel_translate(sequence);

    PyObject *data = PyDict_New();
    for (int i=0; i<sequence->num_orfs; i++) {
      PyDict_SetItem(data, Py_BuildValue("s", sequence->orf_names[i]), Py_BuildValue("s", sequence->orfs[i]));
    }
    return data;
}


static PyMethodDef PyGeneticCodeMethods[] = {
    {"translate",  translate, METH_VARARGS, "Translate a DNA sequence in all 6 frames"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef PyGeneticCodeModule = {
    PyModuleDef_HEAD_INIT,
    "pygenetic_code",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    PyGeneticCodeMethods
};

PyMODINIT_FUNC PyInit_PyGeneticCode(void) {
    return PyModule_Create(&PyGeneticCodeModule);
};
