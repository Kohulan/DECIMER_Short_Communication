import sys
import numpy as np
import deepsmiles
print("DeepSMILES version: %s" % deepsmiles.__version__)
converter = deepsmiles.Converter(rings=True, branches=True) 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+')

args = parser.parse_args()
print(args)
def main():
	for file_in in args.file:
		file_out = open(str(file_in)[:-4]+"_Smiles_condtraints","w")

		with open(file_in,"r") as fp:
			for i,line in enumerate(fp):
				chembl =(line.strip().split("\t")[1])
				smiles = (line.strip().split("\t")[0])
				

				try:
					encoded = converter.decode(smiles)
					file_out.write(encoded+"\t"+chembl+"\n")
				except Exception as e:
					file_out.write("rejected"+"\t"+chembl+"\n")
					print(chembl)

				#if decoded:
				    #print("Decoded: %s" % decoded)

	file_out.close()

if __name__ == '__main__':
	main()