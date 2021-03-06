# A simple virtual CPU
# A program that pretends to be a CPU

# I want to:
#
#  * Store a sequence of instructions
#  * Go through those instructions, doing whatever they ask me to do

# Instructions
#  * Print "Beej" on the screen
#  * Halts the program

import sys

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3   # Save a value in a register
PRINT_REG = 4
ADD = 5   # Add two registers, r0 += r1
PUSH = 6
POP = 7
CALL = 8
RET = 9

memory = [0] * 256

SP = 7

registers = [0,0,0,0,0,0,0,0]  # Like variables, named R0-R7

halted = False

pc = 0  # "Program Counter": index into the memory array,
        # AKA "pointer", "address", "location"

registers[SP] = 0xf4

# Load the program from disk
address = 0

with open(sys.argv[1]) as f:
    for line in f:
        string_val = line.split("#")[0].strip()
        if string_val == '':
            continue
        v = int(string_val, 10)
        #print(v)
        memory[address] = v
        address += 1
        

# Run the CPU
while not halted:
    instruction = memory[pc]

    if instruction == PRINT_BEEJ:
        print("Beej!")
        pc += 1

    elif instruction == SAVE_REG:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]

        registers[reg_num] = value

        pc += 3

    elif instruction == PRINT_REG:
        reg_num = memory[pc + 1]
        print(registers[reg_num])

        pc += 2

    elif instruction == ADD:
        reg_num_a = memory[pc + 1]
        reg_num_b = memory[pc + 2]

        registers[reg_num_a] += registers[reg_num_b]

        pc += 3

    elif instruction == PUSH: #  e.g. "PUSH R3"
        # Decrement the SP
        registers[SP] -= 1

        # Get register number
        reg_num = memory[pc + 1]

        # Get value out of the register
        val = registers[reg_num]
        
        # Store value in memory at SP
        top_of_stack_addr = registers[SP]

        memory[top_of_stack_addr] = val

        pc += 2

    elif instruction == POP:
        top_of_stack_addr = registers[SP]
        val = memory[top_of_stack_addr]

        reg_num = memory[pc + 1]
        registers[reg_num] = val

        registers[SP] += 1

        pc += 2

    elif instruction == CALL:
        return_addr = pc + 2

        # Push it on the stack
        registers[SP] -= 1
        top_of_stack_addr = registers[SP]
        memory[top_of_stack_addr] = return_addr

        # Set the PC to the subroutine addr
        reg_num = memory[pc + 1]
        subroutine_addr = registers[reg_num]

        pc = subroutine_addr

    elif instruction == RET:
        # Pop the return addr off stack
        top_of_stack_addr = registers[SP]
        return_addr = memory[top_of_stack_addr]
        registers[SP] += 1

        # Store it in the PC
        pc = return_addr

    elif instruction == HALT:
        halted = True

    else:
        print(f'unknown instruction {instruction} at address {pc}')
        exit(1)


