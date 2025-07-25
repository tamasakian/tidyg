#!/usr/bin/env python3

from tidyg import utils

def root2hog(input_file: str, output_file: str) -> None:
    """
    This function reads a FastOMA TSV file and writes the RootHOG and GeneID columns to an output file.

    Args:
        input_file: Path to the FastOMA TSV file.
        output_file: Path to the output file where RootHOG and GeneID will be written.
    """
    records = utils.load_fastoma_records(input_file)
    with open(output_file, "w") as output_handle:
        for root, gene, _ in records:
            output_handle.write(f"{root}\t{gene}\n")

def omamer2hog(input_file: str, output_file: str) -> None:
    """
    This function reads a FastOMA TSV file and writes the OMAmerRootHOG and GeneID columns to an output file.

    Args:
        input_file: Path to the FastOMA TSV file.
        output_file: Path to the output file where OMAmerRootHOG and GeneID will be written.
    """
    records = utils.load_fastoma_records(input_file)
    with open(output_file, "w") as output_handle:
        for _, gene, omamer in records:
            output_handle.write(f"{omamer}\t{gene}\n")

def pivot_wider(input_file: str, output_file: str) -> None:
    """
    This function reads a long format TSV file and writes it in a wider format to an output file.

    Args:
        input_file: Path to the long format TSV file.
        output_file: Path to the output file where the wider format will be written.
    """
    group2genes = utils.load_long_records(input_file)
    with open(output_file, "w") as output_handle:
        for group, genes in group2genes.items():
            output_handle.write(f"{group}\t" + "\t".join(genes) + "\n")

def pivot_longer(input_file: str, output_file: str) -> None:
    """
    This function reads a wide format TSV file and writes it in a longer format to an output file.

    Args:
        input_file: Path to the wide format TSV file.
        output_file: Path to the output file where the longer format will be written.
    """
    group2genes = utils.load_wide_records(input_file)
    with open(output_file, "w") as output_handle:
        for group, genes in group2genes.items():
            for gene in genes:
                output_handle.write(f"{group}\t{gene}\n")
