# The Data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import datetime as dt
import random as rand
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable for the file to save and the path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# Open election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Single out headers from file
    headers = next(election_data)
    # To do: Perform analysis
    print(headers)

# Open election analysis and write to the file
with open(file_to_save,"w") as txt_file:
    txt_file.write("Hello World")
