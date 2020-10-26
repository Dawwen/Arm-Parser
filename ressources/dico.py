def int_to_bin(num, bitWidth):
	num &= (2 << bitWidth-1)-1 # mask
	formatStr = '{:0'+str(bitWidth)+'b}'
	ret =  formatStr.format(int(num))
	return ret

def bin_to_hex(str):
	return('%04x' % int(str, 2))


DATA_PROCESSING_COMMAND = {
	'opcode': '010000', #OpCode for the data processing
	'and': '0000', #Logical and
	'eor': '0001', #Exclusive or
	'lsl': '0010', #Logical shift left register
	'lsr': '0011', #Logical shift right register
	'asr': '0100', #Arithmetic shift right register
	'adc': '0101', #Add with carry
	'sbc': '0110', #Substrate with carry
	'ror': '0111', #Rotate right
	'tst': '1000', #Set flags
	'rsb': '1001', #Reverse substract from 0
	'cmp': '1010', #Compare register
	'cmn': '1011', #Compare negative register
	'lor': '1100', #Logical or
	'mul': '1101', #Multiply
	'bic': '1110', #Bit clear
	'mvn': '1111'  #Bitwise or
}

SHIFTS_2_REGISTER_IMMEDIAT_5BIT = {
	'opcode': '00', #OpCode for the shift add sub move Compare
	'lsl': '000',	#LogicalShift LeftImmediate
	'lsr': '001',	#LogicalShift Right Immediate
	'asr': '010'	#ArithmeticShift Right Immediate
}

SHIFTS_2_REGISTER_IMMEDIAT_3BIT = {
	'opcode': '00',	#OpCode for the shift add sub move Compare
	'add': '01110',	#Add Immediate 3bit
	'sub': '01111'	#Sub Immediate 3bit
}

SHIFTS_3_REGISTER = {
	'opcode': '00',	#OpCode for the shift add sub move Compare
	'add': '01100',	#Add register
	'sub': '01101'	#Sub register
}

SHIFTS_1_REGISTER_IMMEDIAT = {
	'opcode': '00',	#OpCode for the shift add sub move Compare
	'mov': '100'
}

LOADS = {
	'opcode': '1001',
	'str': '0',
	'ldr': '1'
}

LOOP_COND = {
	'opcode': '1101',	#OpCode for the loop
	'eq': '0000',	#Equal
	'ne': '0001',	#Not Equal
	'cs': '0010',	#Carry Set
	'cc': '0011',	#Carry Clear
	'mi': '0100',	#Minus, negative
	'pl': '0101',	#Plus, positive, zero
	'vs': '0110',	#Overflow
	'vc': '0111',	#No overflow
	'hi': '1000',	#Unsigned higher
	'ls': '1001',	#Unsigned lower or same
	'ge': '1010',	#Signed greater than or equal
	'lt': '1011',	#Signed less than
	'gt': '1100',	#Signed greater than
	'le': '1101',	#Signed less than or equal
	''  : '1110'	#Always
}

WEIRD_3_REGISTER = {
	'opcode': '010000',
	'mul': '1101',
	'lsl': '0010'
}

WEIRD_2_REGISTER_IMMEDIAT = {
	'opcode': '010000',
	'rsb': '1001'
}

WEIRD_2_REGISTER = {
	'opcode': '010000',
	'orr': '1100'
}

MOV_2_REGISTER = {
	'opcode': '000 00',
	'mov': '00000'
}

STACKPOINTER_ADDS = {
	'opcode': '1011 0000',
	'add': '0',
	'sub': '1'
}
