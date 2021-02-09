#!/usr/bin/env python
"""
Count total and unique words in directory
Parameters:
    path: str <path-to-folder>
Usage:
    word_counts_rdkm.py --path <path-to-folder>
Example:
    $ python word_counts_rdkm.py --path data/100_english_novels/corpus
"""

import os
from pathlib import Path
import argparse

# Define main function
def main():
    # Initialise ArgumentParser class
    ap = argparse.ArgumentParser()
    # CLI parameters
    ap.add_argument("-i", "--path", required=True, help="Path to data folder")
    ap.add_argument("-o", "--outfile", required=True, help="Output filename")
    # Parse arguments
    args = vars(ap.parse_args())

    # Output filename
    out_file_name = args["outfile"]
    # Create directory called out, if it doesn't exist
    if not os.path.exists("out"):
        os.mkdir("out")

    # Output filepath
    outfile = os.path.join("out", out_file_name)
    # Create column headers
    column_headers = "filename,word_length,unique_words"
    # Write column headers to file
    with open(outfile, "a", encoding="utf-8") as headers:
        # add newling after string
        headers.write(column_headers + "\n")

    # Create explicit filepath variable
    filenames = Path(args["path"]).glob("*.txt")

    # Iterate over novels
    for novel in filenames:
        # Open the file as infile using with open()
        with open(novel, "r", encoding="utf-8") as infile:
            # Read novel to variable called text
            text = infile.read()
        # Split on whitespace
        list_of_words = text.split()
        # Calculate python3number of words
        total_words = len(list_of_words)
        # Calculate unique words
        total_unique = len(set(list_of_words))
        # Get novel name
        name = os.path.split(novel)[1]
        # Formatted string
        out_string = f"{name}, {total_words}, {total_unique}"
        # Append to output file using with open()
        with open(outfile, "a", encoding="utf-8") as results:
            # add newling after string
            results.write(out_string+"\n")

# Define behaviour when called from command line
if __name__=="__main__":
    main()