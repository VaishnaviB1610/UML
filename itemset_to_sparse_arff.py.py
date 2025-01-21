import sys

def itemset_to_sparse_arff_debug(input_file, output_file):
    unique_items = set()
    with open(input_file, 'r') as file:
        for line in file:
            items = line.strip().split()
            unique_items.update(items)
    unique_items = sorted(unique_items)
    item_to_index = {item: idx for idx, item in enumerate(unique_items)}
    print("Item-to-Index Mapping (First 10):", list(item_to_index.items())[:10])

    with open(output_file, 'w') as arff:
        arff.write("@relation kosarak\n\n")
        for item in unique_items:
            arff.write(f"@attribute item_{item} {{0,1}}\n")
        arff.write("\n@data\n")
        
        with open(input_file, 'r') as file:
            for i, line in enumerate(file):
                items = line.strip().split()
                if not items:
                    continue
                indices = sorted(set(item_to_index[item] for item in items))
                sparse_data = ','.join(f"{idx} 1" for idx in indices)
                arff.write(f"{{{sparse_data}}}\n")
                if i < 10:  # Debug: Print first 10 transactions
                    print(f"Transaction {i}: {line.strip()} -> {{{sparse_data}}}")

if __name__ == "__main__":
    input_file = "kosarak_cleaned.dat"  # Use the cleaned file
    output_file = "kosarak_debug.arff"
    itemset_to_sparse_arff_debug(input_file, output_file)
