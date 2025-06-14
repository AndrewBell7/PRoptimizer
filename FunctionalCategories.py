import csv
import sys

def read_tsv_as_list(file_path):
    """Reads a TSV file and returns its contents as a list of lists.

    Args:
        file_path (str): The path to the TSV file.

    Returns:
        list: A list of lists, where each inner list represents a row in the TSV file.
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        for row in tsv_reader:
            data.append(row)
    return data

file_path = 'output.tsv' # Replace with the actual file path
tsv_data = read_tsv_as_list(file_path)
#print(tsv_data)

#sys.exit()

categories = []
for x in tsv_data:
    if x not in categories:
        categories.append(x)

#print(categories)

for c in categories:
    counter=0
    for x in tsv_data:
        if x == c:
            counter+=1
        print(f"{c}: {counter}")


'''
for category in categories:
    print(category)

for category in categories:
    if 
'''