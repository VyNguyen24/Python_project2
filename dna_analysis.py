# Name: Vy Nguyen
# CSE 160
# Homework 2: DNA analysis

# This program reads in DNA sequencer output and computes statistics, such as
# the GC content, AT content, nucleotide counts, etc.  Run it from the command
# line like this:
#   python dna_analysis.py myfile.fastq


# The sys module supports reading files, command-line arguments, etc.
import sys


# Function to convert the contents of dna_filename into a string of nucleotides
def filename_to_string(dna_filename):
    """
    dna_filename - the name of a file in expected file format
    Expected file format is: Starting with the second line of the file,
    every fourth line contains nucleotides.
    The function will read in all lines from the file containing nucleotides,
    concatenate them all into a single string, and return that string.
    """

    # Creates a file object from which data can be read.
    inputfile = open(dna_filename)

    # String containing all nucleotides that have been read from the file so
    # far.
    seq = ""

    # The current line number (= the number of lines read so far).
    line_num = 0

    for line in inputfile:
        line_num = line_num + 1
        # if we are on the 2nd, 6th, 10th line...
        if line_num % 4 == 2:
            # Remove the newline characters from the end of the line
            line = line.rstrip()
            # Concatenate this line to the end of the current string
            seq = seq + line
    # close file
    inputfile.close()
    return seq


# Function to return GC Classification
def classify(gc_content):
    if gc_content > 0.55:
        return 'high'
    elif gc_content < 0.37:
        return 'low'
    elif 0.37 <= gc_content <= 0.55:
        return 'moderate'
    """
    gc_content - a number representing the GC content
    Returns a string representing GC Classification. Must return one of
    these: "low", "moderate", or "high" based on the cutoffs in the spec
    """

###########################################################################
# Main program begins here
#


if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this "
          "program.")
    sys.exit(2)

# Save the 1st argument provided by the user, as a string.
# Note: sys.argv[0] is the name of the program itself (dna_analysis.py)
file_name = sys.argv[1]

# Open the file and read in all nucleotides into a single string of letters
nucleotides = filename_to_string(file_name)

###
# Compute statistics
###

# YOUR CODE GOES BELOW THIS POINT

# Total nucleotides seen so far.
total_count = 0

# Number of G and C nucleotides seen so far.
gc_count = 0
sum = 0
for base in nucleotides:
    total_count = total_count + 1
    if base == "G" or base == "C" or base == "T" or base == "A":
        sum = sum + 1

    # OK to change this code!
    if base == 'C' or base == 'G':
        gc_count = gc_count + 1

gc_content = gc_count / sum

print('GC-content:', gc_content)

# Number of A and T nucleotides

at_count = 0
total_count = 0

for base in nucleotides:
    total_count = total_count + 1
    if base == 'A' or base == 'T':
        at_count = at_count + 1

at_content = at_count / sum

print('AT-content:', at_content)

# A,T,G,C count

T_count = 0
A_count = 0
G_count = 0
C_count = 0
total_count = 0

for base in nucleotides:
    total_count = total_count + 1
    if base == 'A':
        A_count = A_count + 1
    elif base == 'T':
        T_count = T_count + 1
    elif base == 'G':
        G_count = G_count + 1
    elif base == 'C':
        C_count = C_count + 1

print('G count:', G_count)
print('C count:', C_count)
print('A count:', A_count)
print('T count:', T_count)

sum_counts = G_count + C_count + A_count + T_count

print('Sum of G+C+A+T counts:', sum_counts)
print('Total count:', total_count)
print('Length of nucleotides:', len(nucleotides))
print('AT/GC Ratio:', (A_count + T_count)/(G_count + C_count))
print('GC Classification:', classify(gc_content), 'GC content')

# You can add more assertions here to check properties that you think
# should be true about your results. If the condition listed is false,
# then the given message will be printed.
assert total_count == len(nucleotides), "total_count != length of nucleotides"
