import numpy as np

# Load the TSV file, specifying the tab delimiter
data = np.loadtxt('your_file.tsv', delimiter='\t',names=True)

print(data)
print("Number of SNPs now: ", data.shape[0])
print("Number of columns in the table: ", data.shape[1])
print(data.dtype.names)

# Use np.strings.contains to create a boolean mask for a specific values of sift, polyphen and clinvar columns
sift_keyword = 'berry'
polyphen_keyword = 'berry'
clinvar_keyword = 'berry'

mask_pathogenicity = np.strings.contains(data['SIFT'], sift_keyword) & np.strings.contains(data['PolyPhen'], polyphen_keyword) & np.strings.contains(data['Clinvar'], clinvar_keyword) 
pathogenic_variants = data[mask_pathogenicity]

print("Number of SNPs with pathogenicity predicted by SIFT, PolyPhen, and ClinVar: ", pathogenic_variants.shape[0])
print("Number of columns in the table: ", pathogenic_variants.shape[1])

# mask on epileptic variants among pathogenic
mask_epilepsy = np.strings.contains(data, "epilepsy") 
epilepsy_variants = pathogenic_variants[mask_pathogenicity]
