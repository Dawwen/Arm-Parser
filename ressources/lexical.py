# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.	This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
# sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
	raw_input = input


filename = "../src/hello.s"

tokens = (
	'COMMAND', 'REGISTER', 'INTEGER', 'LABEL','STACKPOINTER','MAIN'
)

literals = ['[', ']', ',']

# Tokens
t_ignore = " \t:"
# t_REGISTER = r'r[0-9]+\,?'
def t_MAIN(t):
	r'main:'
	return(t)

def t_COMMMENT(t):
	r'.*@.*$'
	# return(t)

def t_COMMMENT_ignore(t):
	r'\..*[ \t].*$'
	# return(t)

def t_COMMMENT_ignore_2(t):
	r'//.*$'

def t_STACKPOINTER(t):
	r'[sS][pP]'
	return(t)

def t_REGISTER(t):
	r'r[0-9]+'
	t.value = int(t.value[1:])
	return(t)

def t_LABEL(t):
	r'\.[a-zA-Z0-9_]+'
	t.value = t.value[1:]
	# if t.value[-1] == ":":
	# 	t.value = t.value[:-1]
	return(t)

def t_COMMAND(t):
	r'[a-zA-Z]+'
	t.value = t.value.lower()
	if len(t.value) == 4 and t.value[3] == 's':
			t.value = t.value[:-1]
	return(t)


def t_INTEGER(t):
	r'\#[0-9-]*'
	# print((t.value)[1:])
	t.value = int((t.value)[1:])
	return(t)

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")
	# print("\n####	NEW LINE :	####\n")


def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

if __name__ == "__main__":

	data = ""
	f = open(filename, "r")
	for line in f:
		print("# IN #")
		print(line,end="")
		print("# /IN #\n")

		# Give the lexer some input
		lexer.input(line)
		# Tokenize

		print("# OUT #")

		while True:
			tok = lexer.token()
			if not tok:
				break	 # No more input
			print(tok)

		print("# /OUT #\n")

		# data += line
	f.close()
