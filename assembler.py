#!/usr/bin/python3
import sys, glob, os, subprocess
sys.path.append('ressources/')
import syntaxic

#Transforme le fichier assembler en machine
def parse(file, output):
	print("Parsing file :\t\t" + file + "\t\t", end="")
	if syntaxic.translate(file, output):
		print("Error while parsing.")
		return(1)
	print("Parsed.")
	return(0)


def main():
	length = len(sys.argv)
	#Pas de source ou pas de output specifier
	if length == 1 or length == 3:
		print("Not enough argument.")
		return(1)

	#Juste le fichier source est donnee
	elif length == 2:
		file = sys.argv[1]
		output = ""
		if not os.path.exists(file):
			print("File {} does not exist.".format(file))
			return(1)

	#Trop d'arguments tout est contenu dans un main
	elif length >= 5:
		print("Too many argument.")
		return(1)

	#2 cas possible 1 arguements ou 3 arguments
	else:

		if sys.argv.count("-o") != 1:
			print("Too many or none -o argument.")
			return(1)

		if sys.argv[1] == "-o":
			output = sys.argv[2]
			file = sys.argv[3]
		elif sys.argv[2] == "-o":
			output = sys.argv[3]
			file = sys.argv[1]
		else:
			print("The -o is misplaced.")
			return(1)

	return(parse(file, output))


if __name__ == '__main__':
	sys.exit(main())
