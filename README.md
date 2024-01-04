[![Edwards Lab](https://img.shields.io/badge/Bioinformatics-EdwardsLab-03A9F4)](https://edwards.flinders.edu.au)
[![DOI](https://www.zenodo.org/badge/60999054.svg)](https://www.zenodo.org/badge/latestdoi/60999054)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub language count](https://img.shields.io/github/languages/count/linsalrob/genetic_codes)
[![PyPi](https://img.shields.io/pypi/pyversions/pygenetic-code?label=PyPi%20Versions)](https://pypi.org/project/pygenetic-code/)


# Genetic Codes

A Python and C library with no external dependencies for translating DNA sequences into protein sequences using different translation tables (aka genetic codes).

The [NCBI Genetic Codes](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1) are central to working with alternate genetic codes. This Python tool kit includes a library that exposes the genetic codes so you can query a codon and get its variants or query a code and get its table. We also provide fast mechanisms to translate DNA sequences into protein sequences using the translation table of your choice.


# Installation

You can install `pygenetic_code` with pip.

```python
pip install pygenetic_code
pygenetic_code --version
```

A conda installation is in the works!

# Usage

There is a command line application, Python example code, and a library that you can use. The command line application and examples show you how to use the library.

## Example code

These examples show you how to incorporate `pygenetic_code` into your own Python code. 

We have a very simple translate function that you can use if you want to translate one (or more) ORFs. The signature is

```python
translate(dna_sequence, translation_table)
```

and we have a simple example that translates a sequence:

```bash
python examples/translate_a_sequence.py
```

We can also translate DNA sequences in all six reading frames, and here is an example that reads a fasta file and translates all six frames using the bacterial genetic code (translation table 11):

```bash
python examples/translate_sequence_in_all_frames.py -f tests/JQ995537.fna -t 11
```

or an alternate genetic code (translation table 15):

```bash
python examples/translate_sequence_in_all_frames.py -f tests/JQ995537.fna -t 15
```

Or you can translate the _E. coli_ K-12 sequence, and so you can identify all the ORFs in that genome:

```bash
python examples/translate_sequence_in_all_frames.py -f tests/U00096.3.fna.gz -t 11
```

(yes, you can use gzip files without decompressing them). 

This will take about 0.1 seconds to do the actual translation, but starting python and all the other overheads make it almost 3/4 second to run.

You can also look at the effect of translation tables on the same sequences by running 

```bash
python examples/average_translation_length.py -f tests/JQ995537.fna # for crassphage
python examples/average_translation_length.py -f tests/U00096.3.fna.gz # for E. coli K-12
```

We recommend using our easy Python wrappers to access the translate functions

```python
from pygenetic_code import translate, six_frame_translation
```

But you can also access our C library directly, using the `PyGeneticCode` module (see below)


## Command line applications

`pygenetic_code` translates DNA sequences either in one reading frame or in all six reading frames using the translation table of your choice.

To translate a sequence in the current reading frame, you can use

```python
pygenetic_code --translate 
```


First, make sure you have a DNA sequence. We provide a few in [tests/](tests/) including [a very short sequence](tests/seq.fasta), [crAssphage](tests/JQ995537.fna), and [E. coli])(tests/U00096.3.fna.gz). 

## Library

### Using the C library directly in Python

You can import the C library by importing PyGeneticCode. 

There are two main methods that you can call:

The first function just returns the translation of your DNA sequence in 5' -&gt; 3' format, so for example, this is the method you might use to translate an ORF.

```python
PyGeneticCode.translate(DNA_sequence, translation_table)
```

(See [examples/translate_a_sequence.py](examples/translate_a_sequence.py_) for an example.

The second method returns all the 6 frame translations.

```python
PyGeneticCode.translate_six_frames(DNA_sequence, translation_table, verbose)
```

(See [examples/translate_sequence_in_all_frames.py](examples/translate_sequence_in_all_frames.py) for an example invocation.)

The DNA sequence is the DNA sequence you want to translate. The translation table must be one of the valid translation tables (see [pygenetic_code/genetic_code.translation_tables](pygenetic_code/genetic_code.translation_tables) for the valid tables).

## Translate a codon

Another way to access the code in your python application is to access the `translate_codon()` function, that has this signature:

```python
amino_acid = translate_codon(codon, translation_table=1, one_letter=False)
```

The `codon` is the codon that you want to translate as either an RNA (e.g. `AUG`) or DNA (e.g. `ATG`) sequence. The `translation_table` is your required translation table (see the [NCBI website](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1) for valid tables), and `one_letter` is whether to return a three letter amino acid code (e.g. `Met` or `Ter`) or a one letter amino acid code (e.g. `M` or `*`).

The library provides other ways to access the genetic codes, and those are exemplified in the `pytest` files in [tests/](tests)


## Viewing translation tables

You can print the translation tables using the `pygenetic_code` command. There are currently a couple of options:

   - `json` prints the table in machine readable json format.
   - `difference` prints a `.tsv` file with the the difference from the standard (translation table 1) code
   - `maxdifference` prints a `.tsv` file with the difference from the most common amino acid. The main difference is that `TGA` is more frequently tryptophan than a stop.
   - 
# Citing

Please cite this repository as:

Edwards, Robert A. 2023. pygenetic_code. https://github.com/linsalrob/genetic_codes. DOI: 10.5281/zenodo.10453453