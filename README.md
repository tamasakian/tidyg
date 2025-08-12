# tidyg
TIDYG: A Python tool to tidy and unify ortholog group files from various sources into a consistent format.

## Installation
```
pip3 install git+https://github.com/tamasakian/tidyg.git
```

## Usage

### orthofinder2hog
This function reads an OrthoFinder TSV file and writes the Orthogroup and GeneID columns to an output file.
```
python3 -m tidyg orthofinder2hog input.tsv output.tsv
```
- `input.tsv`: The input OrthoFinder TSV file, called `Orthogroups.tsv`.
- `output.tsv`: The output file where the Orthogroup and GeneID columns will be written.

### sonicparanoid2hog
This function reads a SonicParanoid TSV file and writes the Orthogroup and GeneID columns to an output file.
```
python3 -m tidyg sonicparanoid2hog input.tsv output.tsv
```
- `input.tsv`: The input SonicParanoid TSV file, called `flat.ortholog_groups.tsv`.
- `output.tsv`: The output file where the Orthogroup and GeneID columns will be written.

### pivot_wider
This function pivots a DataFrame from long to wide format.
```
python3 -m tidyg pivot_wider input.tsv output.tsv
```
- `input.tsv`: The input file in long format.
- `output.tsv`: The output file in wide format.

### pivot_longer
This function pivots a DataFrame from wide to long format.
```
python3 -m tidyg pivot_longer input.tsv output.tsv
```
- `input.tsv`: The input file in wide format.
- `output.tsv`: The output file in long format.