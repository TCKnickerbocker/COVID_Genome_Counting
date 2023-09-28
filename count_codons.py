import sys
import csv

### Counts the number of times each codon occurs within a file, and outputs the results to a csv
def count_codons(input_filename, output_filename):
    try:  # Read codons from input file
        f = open(input_filename)
        seq = f.readlines()
        f.close()

        # Setup csvwriter, write empty row if non-codon row detected
        with open (output_filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(seq)):
                if seq[i][0] == ">":
                    if i>0:
                        writer.writerow([])
                    continue

                # Clean sequence of newline, initialize counts dictionary
                seq[i] = seq[i].replace("\n", "")
                counts = {}

                # Count codons in sequence (loop by 3)
                for j in range(0, len(seq[i]), 3):
                    codon = seq[i][j : j + 3]
                    # Break if codon is too short to be a codon, else, increment counts for this codon
                    if len(codon) < 3:
                        break
                    elif codon not in counts:
                        counts[codon] = 1
                    else:
                        counts[codon] += 1

                # Write counts to csv for this current loop (gene)
                for key, value in counts.items():
                    writer.writerow([key, value])
    except:
        print("Error reading the file " + input_filename)
        sys.exit(1)

    return counts  


# Check that the command-line arguments are correct
if len(sys.argv) != 3:
    print("Usage: python3 count_codons.py <input_filename> <output_filename>")
    sys.exit(1)

# Get filenames from command-line, call count_codons with them
input_filename = sys.argv[1]
output_filename = sys.argv[2]
count_codons(input_filename, output_filename)
