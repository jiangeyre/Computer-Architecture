"""CPU functionality."""

import sys

'''
# `HLT` instruction handler
HLT = 1
# `LDI` instruction handler
LDI = 130
# `PRN` instruction handler
PRN = 71
'''

SP = 7

HLT = 0b00000001
PRN = 0b01000111
LDI = 0b10000010
ADD = 0b10100000
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.reg[SP] = 0XF4

    def load(self):
        """Load a program into memory."""

        address = 0

        try:
            filename = sys.argv[1]
            address = 0
            with open(filename) as f:
                # read the comments in line by line
                for line in f:
                    # remove any comment
                    line = line.split("#")[0]
                    # remove the white space
                    line = line.strip()
                    # skip over the empty lines
                    if line == "":
                        continue

                    value = int(line, 2)

                    # set the instruction to the mem
                    self.ram[address] = value
                    address += 1

        except FileNotFoundError:
            print("File not found")
            sys.exit(2)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        if op == 'OR':
            if reg_a == 1 and reg_b == 0:
                return True
            elif reg_a == 0 and reg_b == 1:
                return True
            elif reg_a == 1 and reg_b == 1:
                return True
            else:
                return False
        if op == 'XOR':
            if reg_a == 1 and reg_b == 0:
                return True
            if reg_a == 0 and reg_b == 1:
                return True
            else:
                return False
        if op == 'NOR':
            if reg_a == 0 and reg_b == 0:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        value = self.ram[address]

    def run(self):
        """Run the CPU."""
        self.load()

        while True:
            # needs to read mem address stores in register PC and store in IR - local variable
            IR = self.ram_read(self.pc)
            # read the bytes at `PC+1` and `PC+2` from RAM into variables `operand_a` and `operand_b` in case the instruction needs them
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            # Then, depending on the value of the opcode, perform the actions needed for the instruction per the LS-8 spec. Maybe an `if-elif` cascade...? There are other options, too

            if IR == HLT:
                # In `run()` in your switch, exit the loop if a `HLT` instruction is encountered regardless of whether or not there are more lines of code in the LS-8 program you loaded
                print("Exit")
                sys.exit(-1)
                break
            elif IR == PRN:
                # Add the `PRN` instruction
                data = operand_a
                print(self.reg[data])
                self.pc += 2
            elif IR == LDI:
                # Add the `LDI` instruction
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif IR == ADD:
                self.alu("ADD", operand_a, operand_b)
                self.pc += 3
            elif IR == MUL:
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3
            elif IR == PUSH:
                # choose register
                reg = self.ram[self.pc+1]
                # get value from register
                val = self.reg[reg]
                # decrement memory address by one
                self.reg[SP] -= 1
                # vave value from register into memory
                self.ram[self.reg[SP]] = val
                # increment pc by 2
                self.pc += 2
            elif IR == POP:
                # reg holding sp
                reg = self.ram[self.pc+1]
                # value from place in memory
                val = self.ram[self.reg[SP]]
                # save value into register we arelooking at
                self.reg[reg] = val
                # increment pointer
                self.reg[SP] += 1
                # increment pc by 2
                self.pc += 2
            else:
                print("Error")
