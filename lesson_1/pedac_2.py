def sequential_even_sums(num):
    return ((num ** 2) + 1) * num

print(sequential_even_sums(1) == 2)
print(sequential_even_sums(2) == 10)
print(sequential_even_sums(3) == 30)
print(sequential_even_sums(4) == 68)

def sum_even_number_row(row_number):
    rows = []
    start_int = 2
    for row_length in range(1, row_number + 1):
        row = create_row(start_int, row_length)
        rows.append(row)
        start_int = row[-1] + 2
    return sum(rows[-1])

def create_row(start_int, row_length):
    row = []
    current_int = start_int
    while len(row) < row_length:
        row.append(current_int)
        current_int += 2
    return row

print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(3) == 30)
print(sum_even_number_row(4) == 68)
