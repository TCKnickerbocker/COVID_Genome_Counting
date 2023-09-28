# COVID Genome Amino Acid Plotter

## Description:
### Uses two covid genome files, one is a random frame of RNA within the covid genome and another contains a series of frames centered around a producing gene within the COVID genome. The file structure is as follows:

#### - **count_codons.py**: takes the name of an input file and the name of an output file as arguements when called. Reads the input file, counts its codons, and writes that information to a CSV. Envoked via:
python3 count_codons.py <input_filename> <output_filename>

#### - **plot_codons.py**: takes two csv file names (which are expected to be in a similar format to what count_codons outputs) and converts their codon counts into the appropriate amino acids, plotting the frequencies of all amino acids within each file, side-by-side for easy visual comparison. Envoked via:
python3 plot_codons.py <control_csv_filename> <new_csv_filename>

#### - **codon_table.txt**: A simple table mapping codons to the amino acids they form


