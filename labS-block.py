def s_block(input_bits):
    # Таблиця заміщення S-блоку
    substitution_table = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        ...
    ]

    # Розбиваємо вхідні біти на групи
    groups = split_bits_into_groups(input_bits, 6)

    output_bits = []
    for group in groups:
        row = group[0] * 2 + group[5]
        column = group[1] * 8 + group[2] * 4 + group[3] * 2 + group[4]
        value = substitution_table[row][column]
        output_bits.extend(int_to_bits(value, 4))

    return output_bits
