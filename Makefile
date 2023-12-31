IDIR =./
CC=gcc
# note that usually use -O2 but for valgrind debugging use -O0 which is slower but more accurate
CFLAGS=-g -Wall -O0 -Wno-return-type -Wno-unused-variable -Wno-unused-function -I$(IDIR)
LFLAGS= -lz -lm -pthread

ODIR=./obj/
SDIR=./src/
BDIR=./bin/

LIBS=-lm

OBJ=seqs_to_ints translate get_orfs error
objects := $(addsuffix .o, $(addprefix $(ODIR), $(OBJ)))

$(objects): $(ODIR)%.o: $(SDIR)%.c
	@mkdir -p $(@D)
	$(CC) -c $(CFLAGS) $< -o $@ $(FLAGS)



TRANSLATIONS=get_orfs seqs_to_ints translate error
get_orfs_obj:= $(addsuffix .o, $(addprefix $(ODIR), $(TRANSLATIONS)))
$(BDIR)get_orfs: $(get_orfs_obj)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -o $@ $^ $(LFLAGS)

get_orfs: $(BDIR)get_orfs

all: get_orfs

.PHONY: clean

clean:
	rm -fr bin/ obj/
