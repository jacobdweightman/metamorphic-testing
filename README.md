# Metamorphic Testing

This repository contains some exploratory work with metamorphic testing. It
contains implementations of the algorithms and tests based on the metamorphic
relations described in [Metamorphic Testing: A New Approach for Generating Next
Test Cases](https://www.cse.ust.hk/~scc/publ/CS98-01-metamorphictesting.pdf) by
 T. Y. Chen et al.

### Structure

Chen et al. give four examples in their paper. The implementations of the
algorithms described can be found in the corresponding Python files in the
root of the project, and the corresponding tests can be found in the `tests`
directory.

### Running

Since this repository is used to illustrate a software testing principle, the
software under test cannot be run on its own. To run the tests, simply navigate to the project root and run

```
python3 -m unittest
```
