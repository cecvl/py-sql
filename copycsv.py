import csv
import os


def append_columns_between_lines(input_file, output_file, columns_to_copy, start_line, end_line):

    # Open the input CSV file for reading
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Check if the output file exists and whether it is empty
        file_is_empty = not os.path.exists(output_file) or os.path.getsize(output_file) == 0

        # Open the output CSV file in append mode ('a') to preserve existing data
        with open(output_file, mode='a', newline='', encoding='utf-8') as outfile:
            # Create a CSV writer for the output file
            writer = csv.DictWriter(outfile, fieldnames=columns_to_copy)

            # If the output file is empty, write the header first
            if file_is_empty:
                writer.writeheader()

            # Loop over each row in the input file
            for i, row in enumerate(reader, start=1):  # Start row count from 1
                # Append only rows between start_line and end_line (inclusive)
                if start_line <= i <= end_line:
                    filtered_row = {col: row[col] for col in columns_to_copy}
                    writer.writerow(filtered_row)
                elif i > end_line:
                    break  # Stop processing if we are past the end_line

# Example usage
input_file = 'trial.csv'  # Path to the input CSV file
output_file = 'trial2.csv'  # Path to the output CSV file
columns_to_copy = ['username','course']  # List of columns to copy
start_line = 4  # Start line to append from
end_line =  11 # End line to append until

append_columns_between_lines(input_file, output_file, columns_to_copy, start_line, end_line)  # Append rows 2 to 4 (inclusive) to output file

# altenative//append_columns_between_lines(input_file, output_file, columns_to_copy, 2, 4)