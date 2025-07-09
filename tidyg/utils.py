#!/usr/bin/env python3

def load_fastoma_records(input_file: str) -> list[tuple[str, str, str]]:
    """
    This function reads a FastOMA TSV file and extracts the RootHOG, GeneID, and OMAmerRootHOG columns.

    Args:
        input_file: Path to the FastOMA TSV file.

    Returns:
        list: A list of tuples containing (RootHOG, GeneID, OMAmerRootHOG).

    """
    records = []
    with open(input_file, "r") as input_handle:
        for line in input_handle:
            if line.startswith("RootHOG"):
                continue
            li = line.strip().split("\t")
            if len(li) == 3:
                continue
            records.append((li[0], li[1], li[2]))
    return records
