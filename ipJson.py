#!/usr/bin/env python3
import argparse
import re

print(""" ___ ____        _ ____   ___  _   _
|_ _|  _ \      | / ___| / _ \| \ | |
 | || |_) |  _  | \___ \| | | |  \| |
 | ||  __/  | |_| |___) | |_| | |\  |
|___|_|      \___/|____/ \___/|_| \_|

 _____      _                  _
| ____|_  _| |_ _ __ __ _  ___| |_ ___  _ __
|  _| \ \/ / __| '__/ _` |/ __| __/ _ \| '__|
| |___ >  <| |_| | | (_| | (__| || (_) | |
|_____/_/\_\\__|_|  \__,_|\___ |\__\___/|_|\n""")
# Define a regular expression pattern to match an IP address
pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Extract IP addresses from a text file.')
parser.add_argument('-o',dest='output_file', metavar='OUTPUT_FILE', default='output.csv')
args = parser.parse_args()

# Prompt the user to enter the input file path
input_file = input('Enter the input file path: ')

# Open the input and output files
with open(input_file, 'r') as f_in, open(args.output_file, 'w') as f_out:
    # Loop through each line in the input file
    for line in f_in:
        # Use the re.search() function to find the first occurrence of the pattern in the line
        match = re.search(pattern, line)

        if match:
            # Write the matched IP address to the output file
            f_out.write(match.group(0) + '\n')
