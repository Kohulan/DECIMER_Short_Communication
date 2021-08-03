'''
 * This Software is under the MIT License
 * Refer to LICENSE or https://opensource.org/licenses/MIT for more information
 * Written by : Kohulan.R on 2018/08/04
'''
#Implementation of diverse molecule picking using RDKit

from rdkit import Chem
from rdkit.Chem import Draw,rdMolDescriptors,AllChem
from rdkit import SimDivFilters,DataStructs
import gzip, time, platform
from datetime import datetime
import pickle
import sys

log_out = open('Select_Report.txt' , 'w')


#Timestamp
datetime.now().strftime('%Y/%m/%d %H:%M:%S')

#Checking loaded packages
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'),' Python Version', platform.python_version(),flush= True)
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'),' RDKit Version:', Chem.rdBase.rdkitVersion,flush= True)

#Start time
start = time.time()

#File parameters
Infile = 'Chembl_27_train'
Outfile = 'Chembl_27_test'

#Change this to get the number of desired molecules
how_many_to_pick = 155648

#Read input file
mols = []
suppl = []

#Generate fingerprints for valid molecules 
with open(Infile,"r") as fp:
	for i,line in enumerate(fp):
		smiles = line.strip().split(",")[1]
		id = line.strip().split(",")[0]
		molecule=Chem.MolFromSmiles(smiles)


		if molecule is None: continue
		molecule.SetProp("_Name",id)
		suppl.append(molecule)

		mols.append(rdMolDescriptors.GetMorganFingerprintAsBitVect(molecule,2))

#pickle.dump(mols,open("1mil_fingerprints.pkl","wb"))

print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'),' Total Valid Molecules', len(mols),flush= True)

#Start picking diversed compounds
mmp = SimDivFilters.MaxMinPicker()
picks = mmp.LazyBitVectorPick(mols, len(mols),(how_many_to_pick+1))
print("Picking done",flush=True)
#Convert to list
pickIndices = list(picks)

print(len(pickIndices))

#Select the subset
subset = [suppl[mol] for mol in pickIndices]

print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'),' Picking completed, Writing file initiated!',flush= True)

#writer = Chem.SDWriter(Outfile)

writer = open(Outfile,"w")

for mol in subset:
	if mol is None: continue
	writer.write(mol.GetProp("_Name")+"\t"+Chem.MolToSmiles(mol)+"\n")

writer.close()



end = time.time()
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'),' Total time elaped %.2f sec'%(end - start),flush= True)
