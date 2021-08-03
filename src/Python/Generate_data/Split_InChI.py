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
			id_ = line.strip().split("\t")[0]
			smiles = line.strip().split("\t")[1]
			f.write(id_+"\t"+' '.join(smiles_atom_tokenizer(smiles))+"\n")
		f.close()

def smiles_atom_tokenizer (smi):
    pattern =  "(\[[^\]]+]|Br?|Cl?|Si?|Se?|N|D|H|O|T|S|B|P|F|I|b|e|i|m|t|h|c|n|o|s|p|q|,|\(|\)|\.|=|#|-|\+|\\\\|\/|:|~|@|\?|>|\*|\$|\%[0-9]{2}|[0-9])"
    regex = re.compile(pattern)
    tokens = [token for token in regex.findall(smi)]
    return tokens

if __name__ == '__main__':
	main()
