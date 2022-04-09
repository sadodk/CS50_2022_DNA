import csv
import sys

# open csv file (dna sequence) read to memory
# for each str compute longest run repeats in dna sequence
# compare the count against each row in the csv file
# if match print persons name, if not print "No match"


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    databaseName = sys.argv[1]

    persons = []

    # Open the database
    with open(databaseName, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        persons = list(reader)

    # Read DNA sequence file into a variable
    DNAFILE = sys.argv[2]

    with open(DNAFILE, 'r') as txtfile:
        DNAString = txtfile.readline().rstrip("\n")

    # Check database for matching profiles
    for record in persons:
        match = 0
        for keys in record:
            if keys != 'name':
               # print(keys)
               # print(int(record[keys]))
               # print(longest_match(DNAString[0], keys))
                if int(record[keys]) == int(longest_match(DNAString, keys)):
                    match += 1
                  #  print(f'match : {match}')
                if match == len(record)-1:
                    print(record['name'])
                    exit()

    print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()