# Main

3  # SAVE_REG R0,[subroutine1's addr]
0
13
8  # CALL R0
0
8  # CALL R0
0
8  # CALL R0
0
4  # PRINT_REG R0
0
1  # PRINT_BEEJ
2  # HALT

# Subroutine1

3  # SAVE_REG R1,12 (addr 13)
1
12
4  # PRINT_REG R1
1
1  # PRINT_BEEJ
1  # PRINT_BEEJ
1  # PRINT_BEEJ
9  # RET
