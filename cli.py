
import argparse


def parse_args():
    """
    Parse command-line arguments for the finance insights pipeline.

    Returns
    -------
    argparse.Namespace
        Parsed CLI arguments
    """
    parser = argparse.ArgumentParser(
        description="Generate financial insights from a CSV file"
    )

    # Positional argument: CSV file path
    parser.add_argument(
        "csv_path",
        help="Path to CSV file containing price data"
    )

    # Optional arguments
    parser.add_argument(
        "--window",
        type=int,
        default=20,
        help="Rolling window size for metrics (default: 20)"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output insights in JSON format"
    )

    parser.add_argument(
        "--export",
        metavar="PATH",
        help="Export enriched CSV to the given path"
    )

    parser.add_argument(
        "--ticker",
        metavar="SYMBOL",
        help="Optional ticker symbol for labeling output"
    )

    return parser.parse_args()