import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+')

args = parser.parse_args()
print(args)

for file_in in args.file:
	file_out = open("Identical_"+str(file_in),"w")
	count = 0
	smiles = []

	with open(file_in,"r") as fp:
		for i,line in enumerate(fp):
			ori =line.strip().split("\t")[0]
			pred =line.strip().split("\t")[2]
			if ori == pred:
				file_out.write(ori+"\t"+pred+"\n")
				count = count+1
	print(count)
file_out.close()
