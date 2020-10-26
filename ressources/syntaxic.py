
from lexical import tokens
from dico import *
import os

error = False

def p_statement_expr(p):
	'line : instruction'

	# if p[1].replace(" ", "").isdigit() :
	# 	print("\033[92m", end="")
	# else:
	# 	print("\033[91m", end="")
	#
	# print(p[1],end = "\033[0m\n")

	if p[1].replace(" ", "").isdigit() :
		tmp = bin_to_hex(p[1].replace(" ", "")) + " "
	else:
		tmp = p[1] + "\n"
	fout.write(tmp)


def p_3_REGISTER_COMMAND(p):
	'''instruction : COMMAND REGISTER ',' REGISTER ',' REGISTER'''

	if (p[1] in SHIFTS_3_REGISTER):
		str = SHIFTS_3_REGISTER['opcode'] + " "
		str += SHIFTS_3_REGISTER[p[1]] + " "
		str += "{:0>3b} {:0>3b} {:0>3b}".format(p[6], p[4], p[2])
		p[0] = (str)
	elif (p[1] in WEIRD_3_REGISTER):
		str = WEIRD_3_REGISTER['opcode'] + " "
		str += WEIRD_3_REGISTER[p[1]] + " "
		str += "{:0>3b} {:0>3b}".format(p[4], p[2])
		p[0] = (str)

	else :
		p[0] = ("Unknown 3 REGISTER COMMAND")

def p_COMMAND(p):
	''' line : COMMAND COMMAND'''
	if p[1] != "bx":
		p[0] = "Unknown command : " + p[1]

def p_2_REGISTER_COMMAND(p):
	''' instruction : COMMAND REGISTER ',' REGISTER '''

	if (p[1] in DATA_PROCESSING_COMMAND):
		str = DATA_PROCESSING_COMMAND["opcode"] + " "
		str += DATA_PROCESSING_COMMAND[p[1]] + " "
		str += "{:0>3b} {:0>3b}".format(p[4],p[2])
		p[0] = (str)

	elif (p[1] in WEIRD_2_REGISTER):
		str = WEIRD_2_REGISTER['opcode'] + " "
		str += WEIRD_2_REGISTER[p[1]] + " "
		str += "{:0>3b} {:0>3b}".format(p[4],p[2])
		p[0] = str
	elif (p[1] in MOV_2_REGISTER):
		str = MOV_2_REGISTER['opcode'] + " "
		str += MOV_2_REGISTER[p[1]] + " "
		str += "{:0>3b} {:0>3b}".format(p[4],p[2])
		p[0] = str
	else:
		p[0] = ("Unknown 2 REGISTER COMMAND")



def p_2_REGISTER_COMMAND_SHIFT(p):
	''' instruction : COMMAND REGISTER ',' REGISTER ',' INTEGER'''

	if p[1] in SHIFTS_2_REGISTER_IMMEDIAT_5BIT:
		str = SHIFTS_2_REGISTER_IMMEDIAT_5BIT['opcode'] + " "
		str += SHIFTS_2_REGISTER_IMMEDIAT_5BIT[p[1]] + " "
		str += "{:0>5b} {:0>3b} {:0>3b}".format(p[6]%32, p[4], p[2])
		p[0] = str

	elif p[1] in SHIFTS_2_REGISTER_IMMEDIAT_3BIT:
		str = SHIFTS_2_REGISTER_IMMEDIAT_3BIT['opcode'] + " "
		str += SHIFTS_2_REGISTER_IMMEDIAT_3BIT[p[1]] + " "
		str += "{:0>3b} {:0>3b} {:0>3b}".format(p[6], p[4], p[2])
		p[0] = str

	elif p[1] in WEIRD_2_REGISTER_IMMEDIAT:
		str = WEIRD_2_REGISTER_IMMEDIAT['opcode'] + " "
		str += WEIRD_2_REGISTER_IMMEDIAT[p[1]] + " "
		str += "{:0>3b} {:0>3b}".format(p[2], p[4])
		p[0] = str

	else:
		p[0] = "Unknown 2 REGISTER COMMAND INTEGER"

def p_1_REGISTER_COMMAND(p):
	'''instruction : COMMAND REGISTER ',' INTEGER'''

	if p[1] in SHIFTS_1_REGISTER_IMMEDIAT:
		str = SHIFTS_1_REGISTER_IMMEDIAT['opcode'] + " "
		str += SHIFTS_1_REGISTER_IMMEDIAT[p[1]] + " "
		str += "{:0>3b} {}".format(p[2], int_to_bin(p[4],8))
		p[0] = str
	else:
		p[0] = "Unknown 1 REGISTER COMMAND WITH INTEGER"

def p_REGISTER_STACKPOINTER_SHIFT(p):
	'''instruction : COMMAND REGISTER ',' '[' STACKPOINTER ',' INTEGER ']' '''
	if p[1] in LOADS:
		str = LOADS['opcode'] + " "
		str += LOADS[p[1]] + " "
		str += "{:0>3b} {:0>8b}".format(p[2], p[7])
		p[0] = str
	else:
		p[0] = "Unknown STACKPOINTER COMMAND"

def p_REGISTER_STACKPOINTER(p):
	'''instruction : COMMAND REGISTER ',' '[' STACKPOINTER ']' '''
	if p[1] in LOADS:
		str = LOADS['opcode'] + " "
		str += LOADS[p[1]] + " "
		str += "{:0>3b} {:0>8b}".format(p[2], 0)
		p[0] = str
	else:
		p[0] = "Unknown Weird COMMAND"

def p_2_STACKPOINTER_COMMAND_SHIFT_WEIRD(p):
	'''instruction : COMMAND '[' STACKPOINTER ',' ']' STACKPOINTER ',' INTEGER'''
	global error
	if p[1] in STACKPOINTER_ADDS:
		if p[8] % 4 != 0 or not (0 <= p[8] and p[8] <= 508):
			print("The immediat is not a multiple of 4 or is not in the range.")
			error = True

		str = STACKPOINTER_ADDS['opcode'] + " "
		str += STACKPOINTER_ADDS[p[1]] + " "
		str += "{:0>7b}".format(int(p[8] / 4))
		p[0] = str
	else:
		p[0] = ("Unknown STACKPOINTER COMMAND")


def p_2_STACKPOINTER_COMMAND_SHIFT(p):
	'''instruction : COMMAND STACKPOINTER ',' STACKPOINTER ',' INTEGER'''
	global error
	if p[1] in STACKPOINTER_ADDS:
		if p[6] % 4 != 0 or not (0 <= p[6] and p[6] <= 508):
			print("The immediat is not a multiple of 4 or is not in the range.")
			error = True

		str = STACKPOINTER_ADDS['opcode'] + " "
		str += STACKPOINTER_ADDS[p[1]] + " "
		str += "{:0>7b}".format(int(p[6] / 4))
		p[0] = str
	else:
		p[0] = ("Unknown STACKPOINTER COMMAND")

def p_STACKPOINTER_COMMAND_SHIFT(p):
	'''instruction : COMMAND STACKPOINTER ',' INTEGER'''
	global error
	if p[1] in STACKPOINTER_ADDS:
		if p[4] % 4 != 0 or not (0 <= p[4] and p[4] <= 508):
			print("The immediat is not a multiple of 4 or is not in the range.")
			error = True

		str = STACKPOINTER_ADDS['opcode'] + " "
		str += STACKPOINTER_ADDS[p[1]] + " "
		str += "{:0>7b}".format(int(p[4] / 4))
		p[0] = str
	else:
		p[0] = ("Unknown STACKPOINTER COMMAND")


def p_COMMENT_LOOP(p):
	''' instruction : COMMAND LABEL '''
	tmp = p[1][1:]
	if tmp in LOOP_COND:
		str = LOOP_COND['opcode'] + " "
		str += LOOP_COND[tmp] + " "
		offset = loopback[p[2]] - CURRENT_LINE
		# if offset < 0:
		# 	offset += 1
		# print(offset)
		str += "{}".format(int_to_bin(offset - 3,8))
		p[0] = str
	else :
		print("\033[90mLOOP\033[0m")

def p_COMMENT(p):
	'''
		line : MAIN
		line : LABEL '''
	p[0] = None

#En cas d'erreur dans l'analyse syntaxique.
def p_error(p):
	if p:
		print("Syntax error at '%s'" % p.value)
	# else:
	# 	print("Syntax error at EOF")




import re
import ply.yacc as yacc
yacc.yacc()

#Ajoute la derniere instruction pour faire boucler le programme.
def get_last_lines():
	out = "defd" + "\n"
	return(out)

#Indique si la ligne est une ligne commentee
def is_comment(line):
	value = re.search(r'@', line) or re.search(r'main:', line) or re.search(r'^[ \t]*\..+$', line) or re.search(r'//.*$', line) or re.search(r'^[ \t]*$', line)
	return(value)

#Cherche les labels et note leurs positions
def set_loopback(filename):
	global loopback

	i = 0
	loopback = {}
	f = open(filename, "r")
	for line in f:
		str = re.findall(r'\.[a-zA-Z0-9_]+:',line)
		# print(line, str)
		if str:
			loopback[str[0][1:-1]] = i
		elif not is_comment(line):
			# print("{} {}".format(i, line),end="")
			i += 1

#Transforme ligne par ligne les instruction en langage machine.
def process_file(filename, loopback):
	global CURRENT_LINE

	error = False
	f = open(filename, "r")
	fout.write("v2.0 raw\n")
	CURRENT_LINE = 0

	for line in f:
		# print(line[:-1],end="\n")

		if yacc.parse(line):
			error = True
		if not is_comment(line):
			CURRENT_LINE += 1
	f.close()
	return(error)

#Donne le nom du fichier avec l'extension change (enleve aussi le chemin)
def get_output_file(filename, extension):
	tmp = os.path.splitext(os.path.basename(filename))[0] + extension
	return(tmp)

#Transforme le fichier assembler en machine
def translate(filename, output):
	global fout, loopback

	loopback = {}
	set_loopback(filename)
	# print(loopback)
	if output == "":
		output = get_output_file(filename, ".out")

	fout = open(output, "w")
	err = process_file(filename, loopback)

	fout.write(get_last_lines())
	fout.close()
	# print(error)
	return(err or error)
