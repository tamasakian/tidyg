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
            output_handle.write(f"{gene}\t{root}\n")

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
            output_handle.write(f"{gene}\t{omamer}\n")