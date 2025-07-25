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
            if len(li) != 3:
                continue
            records.append((li[0], li[1], li[2]))
    return records

def load_long_records(input_file: str) -> dict[str, list[str]]:
    """
    This function reads a long format TSV file and extracts the RootHOG, GeneID, and OMAmerRootHOG columns.

    Args:
        input_file: Path to the long format TSV file.

    Returns:
        list: A list of tuples containing (RootHOG, GeneID, OMAmerRootHOG).

    """
    group2genes = {}
    with open(input_file, "r") as input_handle:
        for line in input_handle:
            group, gene = line.strip().split("\t")
            group2genes.setdefault(group, []).append(gene)
    return group2genes

def load_wide_records(input_file: str) -> dict[str, list[str]]:
    """
    This function reads a wide format TSV file and extracts the RootHOG, GeneID, and OMAmerRootHOG columns.

    Args:
        input_file: Path to the wide format TSV file.

    Returns:
        list: A list of tuples containing (RootHOG, GeneID, OMAmerRootHOG).

    """
    group2genes = {}
    with open(input_file, "r") as input_handle:
        for line in input_handle:
            parts = line.strip().split("\t")
            group = parts[0]
            genes = parts[1:]
            if not genes:
                continue
            group2genes[group] = genes
    return group2genes
