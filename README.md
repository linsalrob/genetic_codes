# Genetic Codes

A Python library for working with the NCBI Genetic Codes

The [NCBI Genetic Codes](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1) are central to working with alternate genetic codes. This Python tool kit includes a library that exposes the genetic codes so you can query a codon and get its variants or query a code and get its table.

The main function that you want to use has this signature:

```python
amino_acid = translate(codon, translation_table=1, one_letter=False)
```

The `codon` is the codon that you want to translate as either an RNA (e.g. `AUG`) or DNA (e.g. `ATG`) sequence. The `translation_table` is your required translation table (see the [NCBI website](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1) for valid tables), and `one_letter` is whether to return a three letter amino acid code (e.g. `Met` or `Ter`) or a one letter amino acid code (e.g. `M` or `*`).

The library provides other ways to access the genetic codes, and those are exemplified in the `pytest` files in [tests/](tests)

# Installation

You can install `pygenetic_code` with pip.

```python
pip install pygenetic_code
```

Conda installation is coming.