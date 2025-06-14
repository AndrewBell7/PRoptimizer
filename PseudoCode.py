#!/usr/bin/env python3

######################
### Call this command 
# python <Name of Script> -j <Job Name> -og <OutGroup> 


## input: ERC_results_BXB.tsv


### Import modules
import os
import sys
import numpy as np
import argparse

#Set up argument parser
parser = argparse.ArgumentParser(description='Parameter Scan')

parser.add_argument('-j', '--JOBname', type=str, metavar='', required=True, help='Unique job name for this run of ERCnet. Avoid including spaces or special characters ("_" is ok)') 
parser.add_argument('-og', '--OutGroup', type=str, metavar='', required=True, help='Outgroup. Avoid including spaces or special characters ("_" is ok)') 

args = parser.parse_args()

JOBname=args.JOBname
OutGroup=args.OutGroup

### Locate in-directory

### Create working directory

### Locate out directory

### Create command using os.system to run the final step of ERCnet



#./ERC_analyses.py -j <JobName> -m 24 -s Scer -b BXB
#./Network_analyses.py -j <JobName> -m BXB -s Scer -p <P> -r <R> -y fg -f ERC_results_BXB.tsv -c pearson


#ERC_analyses_command = "./ERC_analyses.py -j "+JobName+" -m 24 -s "+OutGroup+" -b BXB"
#Network_analyses_command = "./Network_analyses.py -j "+JobName+" -m BXB -s "+OutGroup+" -p "+P+" -r "+R+" -y fg -f ERC_results_BXB.tsv -c pearson"

### Create Functional_categories.tsv and place in ERCnet/

'''
ID	Functional_category
A_thaliana__AT1G01070.1	Unknown
A_thaliana__AT1G01080.1	Plastid
A_thaliana__AT1G01090.1	Plastid
A_thaliana__AT1G01100.1	Other
A_thaliana__AT1G01170.1	Mitochondria
A_thaliana__AT1G01180.1	Unknown
A_thaliana__AT1G01190.1	Unknown
A_thaliana__AT1G01200.1	Other
A_thaliana__AT1G01225.1	Unknown
A_thaliana__AT1G01230.1	Other
A_thaliana__AT1G01240.1	Unknown
A_thaliana__AT1G01250.1	Other
A_thaliana__AT1G01290.1	Mitochondria
A_thaliana__AT1G01335.1	Unknown
A_thaliana__AT1G01340.1	Other
A_thaliana__AT1G01355.1	Unknown
A_thaliana__AT1G01360.1	Other
'''

### Create Functional_categories_col_assign.tsv

'''
Category	Color
Plastid	Green
Mitochondria	red
Unknown	gray
Other	gray
Dual	tan
NA	gray
'''

Pvalues = ["0.00001","0.0001","0.001","0.01"]
Rvalues = ["0.2","0.4","0.6","0.8"]


print(Pvalues)
print(Rvalues)


for P in Pvalues:
    for R in Rvalues:
        Network_analyses_command = "./Network_analyses.py -j "+JOBname+" -m BXB -s "+OutGroup+" -p "+str(P)+" -r "+str(R)+" -y fg -f ERC_results_BXB.tsv -c pearson"
        print(Network_analyses_command)
        #os.system(Network_analyses_command)
        break

# out directory: /scratch/bella7/ERCnet2/ERCnet/OUT_ERCFungiJune4/Network_analyses/ Func Cat Tsv

### Read in TSV as a dataframe (new script)
# Create empty array object or a matrix object with P and R values as axis
# Pull out row for each P and R
# Find assortivity / adjusted Z file, value and plug it into the table

# Create PDF of heatmap of the array


