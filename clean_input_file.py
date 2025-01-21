def clean_input_file(input_file, cleaned_file):
    with open(input_file, 'r') as infile, open(cleaned_file, 'w') as outfile:
        for line in infile:
            items = line.strip().split()
            if items:
                # Remove duplicates and sort
                unique_items = sorted(set(items))
                outfile.write(" ".join(unique_items) + "\n")
    print(f"Cleaned file saved as {cleaned_file}")

# Example usage:
clean_input_file("kosarak.dat.txt", "kosarak_cleaned.dat")
