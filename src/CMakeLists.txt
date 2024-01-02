
set(SOURCE_FILES get_orfs.c get_orfs.h colours.h error.c error.h kseq.h seqs_to_ints.c seqs_to_ints.h translate.c translate.h)
target_sources(get_orfs PUBLIC ${SOURCE_FILES})
target_sources(PyGeneticCode PUBLIC ${SOURCE_FILES} pygenetic_code.c pygenetic_code.h)
