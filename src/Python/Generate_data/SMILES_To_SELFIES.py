import sys
import numpy as np
from selfies import encoder  
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+')

args = parser.parse_args()
print(args)
def main():

	for file_in in args.file:
		file_out = open(str(file_in)+"_SELFIES.txt","w")

		with open(file_in,"r") as fp:
			for i,line in enumerate(fp):
				smiles =(line.strip().split("\t")[0])
				chembl = (line.strip().split("\t")[1])
				

				try:
					encoded = encoder(smiles)
					file_out.write(encoded.replace("][","] [")+"\t"+chembl+"\n")
				except Exception as e:
					print(chembl)

	file_out.close()

if __name__ == '__main__':
	main()