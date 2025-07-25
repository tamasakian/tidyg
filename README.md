# tidyg
TIDYG: A Python tool to tidy and unify ortholog group files from various sources into a consistent format.

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
- `input.tsv`: The input FastOMA TSV file, called `RootHOGs.tsv`.
- `output.tsv`: The output file where the RootHOG and GeneID columns will be written.

### omamer2hog
This function reads a FastOMA TSV file and writes the OMAmerRootHOG and GeneID columns to an output file.
```
python3 -m tidyg omamer2hog input.tsv output.tsv
```
- `input.tsv`: The input FastOMA TSV file, called `RootHOGs.tsv`.
- `output.tsv`: The output file where the OMAmerRootHOG and GeneID columns will be written.

### pivot_wider
This function pivots a DataFrame from long to wide format.
```
python3 -m tidyg pivot_wider input.tsv output.tsv
```
- `input.tsv`: The input file in long format.
- `output.tsv`: The output file in wide format.

### pivot_longer
This function pivots a DataFrame from wide to long format.
```python3 -m tidyg pivot_longer input.tsv output.tsv
```
- `input.tsv`: The input file in wide format.
- `output.tsv`: The output file in long format.