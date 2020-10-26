#!/usr/bin/python3
import sys, glob, os, subprocess
import assembler

compiler_commands = [
	"arm-linux-gnueabi-gcc {0} -S -mtune=cortex-m0 -march=armv7-m -mthumb -fomit-frame-pointer -o {1}",
	"clang -S -target arm-none-eabi -mcpu=cortex-m0 -O0 -mfloat-abi=soft --output {} {}"
]

def get_output_file(filename, extension):
	tmp = os.path.splitext(os.path.basename(filename))[0] + extension
	return(tmp)

#Compile le fichier file
def compile_file(filename, output=""):
	command = "arm-linux-gnueabi-gcc {} -S -mtune=cortex-m0 -march=armv7-m -mthumb -fomit-frame-pointer -o {}"
	# print("output " + fout + get_output_file(filename, ".s"))
	if output == "":
		output = get_output_file(filename,".s")
	command = command.format(filename, output)
	subprocess.run(command.split(" "))
	return(not os.path.exists(output))

#Affiche et compile le fichier file
def compile(file, output=""):
	global temporary_file
	print("Compiling file :\t" + os.path.basename(file) + "\t\t", end="")
	if compile_file(file, output) :
		print("Error while compiling.")
		return(1)
	print("Compiled.")
	temporary_file = get_output_file(file, ".s")
	return(0)

# def find_compiler():
# 	global compile_command
# 	for i in range(len(compilers)):
# 		try:
# 			a = "test"
# 			output = subprocess.run(compilers[i].split(), capture_output=True)
# 			# print(outpu.returncode)
# 			if output.returncode == 0:
# 				compile_command = compiler_commands[i]
# 				return
# 		except Exception as e:
# 			print(e)
#
# 	return(-1)

#supprime le fichier file
def remove(file):
	command = "rm {}".format(file)
	subprocess.run(command.split(" "))


def main():
	sys.argv = sys.argv[1:]
	assemble = True
	output = ""

	if len(sys.argv) == 0:
		print("Not enough argument.")
		return(1)


	if sys.argv.count("-s") >= 1:
		assemble = False
		while (sys.argv.count("-s") > 0):
			sys.argv.remove("-s")

	#Prend en compte le fichier de sortie
	if sys.argv.count("-o") >= 1:
		index = sys.argv.index("-o")
		if index + 1 >= len(sys.argv):
			print("Output file undefined.")
			return(1)
		output = sys.argv[index + 1]
		sys.argv.remove(output)
		while (sys.argv.count("-o") > 0):
			sys.argv.remove("-o")

	if len(sys.argv) != 1:
		print("Too many arguments")
		return(1)

	file = sys.argv[0]
	if not os.path.exists(file):
		print("File {} does not exist.".format(file))
		return(1)

	if assemble:
		if compile(file):
			print("Error while compiling.")
			return(1)
		error = assembler.parse(temporary_file, output)
		remove(temporary_file)
		if error:
			print("Error while assembling.")
			return(1)


	else:
		return(compile(file,output))

if __name__ == '__main__':
	sys.exit(main())
