def p_block(input_bits):
    # Перестановка P-блоку
    permutation_table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
    10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25, 17, 8, 16, 31, 15, 28, 20, 7, 27, 13, 2, 14, 4, 30, 21, 9, 26, 18, 31, 25, 3, 10, 29, 6, 1, 12, 22, 28, 23]

    output_bits = [0] * 32
    for i, position in enumerate(permutation_table):
        output_bits[i] = input_bits[position - 1]

    return output_bits
