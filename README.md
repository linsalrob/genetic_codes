[![Edwards Lab](https://img.shields.io/badge/Bioinformatics-EdwardsLab-03A9F4)](https://edwards.flinders.edu.au)
[![DOI](https://www.zenodo.org/badge/60999054.svg)](https://www.zenodo.org/badge/latestdoi/60999054)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub language count](https://img.shields.io/github/languages/count/linsalrob/genetic_codes)
[![PyPi](https://img.shields.io/pypi/pyversions/pygenetic-code?label=PyPi%20Versions)](https://pypi.org/project/pygenetic-code/)


# Genetic Codes

A pure Python library with no imports for working with the NCBI Genetic Codes

The [NCBI Genetic Codes](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1) are central to working with alternate genetic codes. This Python tool kit includes a library that exposes the genetic codes so you can query a codon and get its variants or query a code and get its table.


# Installation

You can install `pygenetic_code` with pip.

```python
pip install pygenetic_code
pygenetic_code --version
```

Conda installation is coming.

# Usage

## Standalone

You can just print translation tables using the `pygenetic_code` command. There are currently a couple of options:

   - `json` prints the table in machine readable json format.
   - `difference` prints a `.tsv` file with the the difference from the standard (translation table 1) code
   - `maxdifference` prints a `.tsv` file with the difference from the most common amino acid. The main difference is that `TGA` is more frequently tryptophan than a stop.


## Library

In your python application you want to access the `translate()` function, that has this signature:

```python
amino_acid = translate(codon, translation_table=1, one_letter=False)
```

The `codon` is the codon that you want to translate as either an RNA (e.g. `AUG`) or DNA (e.g. `ATG`) sequence. The `translation_table` is your required translation table (see the [NCBI website](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes#SG1) for valid tables), and `one_letter` is whether to return a three letter amino acid code (e.g. `Met` or `Ter`) or a one letter amino acid code (e.g. `M` or `*`).

The library provides other ways to access the genetic codes, and those are exemplified in the `pytest` files in [tests/](tests)


# Citing

Please cite this repository as:

Edwards, Robert A. 2023. pygenetic_code. https://github.com/linsalrob/genetic_codes

A full DOI citation is coming soon.
