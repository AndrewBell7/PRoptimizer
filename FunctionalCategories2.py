import csv
import sys

data_dict = {}

# Open the TSV file
with open('Example_Functional_categories.tsv', mode='r', newline='', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        key, value = row[0], row[1]
        data_dict[key] = value

#print(data_dict.values())

for geneID in data_dict.keys():
    if data_dict[geneID] == 'NUCLEOLUS':
        data_dict.update({geneID: 'NUCLEUS'})
    elif data_dict[geneID] == 'NUCLEAR...':
        data_dict.update({geneID: 'NUCLEUS'})
    elif data_dict[geneID] == 'MUCLEUS':
        data_dict.update({geneID: 'NUCLEUS'})
    elif data_dict[geneID] == 'NUCLEUS':
        data_dict.update({geneID: 'NUCLEUS'})
    elif data_dict[geneID] == 'MITOCHON...':
        data_dict.update({geneID: 'MITOCHONDRIA'})
    elif data_dict[geneID] == 'CYTOPLASM':
        data_dict.update({geneID: 'CYTOPLASM'})
    else:
        data_dict[geneID] = 'OTHER'


with open('Functional_categories.tsv', 'w', newline='') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    
    # Optional: write a header
    writer.writerow(['Key', 'Value'])
    
    # Write each key-value pair
    for key, value in data_dict.items():
        writer.writerow([key, value])