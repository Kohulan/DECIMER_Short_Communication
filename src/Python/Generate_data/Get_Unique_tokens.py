from collections import Counter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='+')

args = parser.parse_args()
print(args)

def main():
	
	for file_in in args.file:
		file_out = open("Unique_"+str(file_in),"w")
		word_array = []




		with open(file_in, 'r') as input_file:
			for i,line in enumerate(input_file):
				chembl =(line.strip().split("\t")[0])
				tokens =(line.strip().split("\t")[1])
				word_array.append(tokens.split(" "))
			wordlist = ([_ for i in range(len(word_array)) for _ in word_array[i]])
			token_list = str(Counter(wordlist)).replace("Counter({","").replace("})","").replace(", ","\n").replace(": ",":\t")
			file_out.write(token_list)

	file_out.close()

if __name__ == '__main__':
	main()
