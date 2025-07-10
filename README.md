# tidyg
TIDYG: A Python tool to tidy and unify ortholog group files from various sources into a consistent format.

## Current Version
0.1.0

## Installation
```
pip3 install git+https://github.com/tamasakian/tidyg.git
```

## Usage

### root2hog
This function reads a FastOMA TSV file and writes the RootHOG and GeneID columns to an output file.
```
python3 -m tidyg root2hog input.tsv output.tsv
```

### omamer2hog
This function reads a FastOMA TSV file and writes the OMAmerRootHOG and GeneID columns to an output file.
```
python3 -m tidyg omamer2hog input.tsv output.tsv
```
