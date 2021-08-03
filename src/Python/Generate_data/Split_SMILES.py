import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+')

args = parser.parse_args()
print(args)

def main():
	for file_in in args.file:
		f = open(str(file_in)[:-4]+"_Split.txt","w")

		with open(file_in,"r") as fp:
			for i,line in enumerate(fp):
				id_ = line.strip().split(",")[0]
				smiles = line.strip().split(",")[1]
				f.write(id_+","+' '.join(smiles_atom_tokenizer(smiles))+"\n")
		f.close()

def SMILES_To_Tokens (smiles):
	pattern =  "(\[[^\]]+]|Br?|Cl?|B|N|O|S|P|F|I|b|c|n|o|s|p|\(|\)|\.|=|#|-|\+|\\\\|\/|:|~|@|\?|>|\*|\$|\%[0-9]{2}|[0-9])"
	regex = re.compile(pattern)
	tokens = [token for token in regex.findall(smiles)]
	return tokens

if __name__ == '__main__':
	main()