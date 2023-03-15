# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


def operation (row, col):
    return row*col

def print_operation_table (operation, num_rows=6, num_columns=6):
    print(f"{'':>5}", end="")
    for j in range (1, num_columns + 1):
        print(f"{j:>5}", end="")
    print()
    for i in range(1, num_rows + 1):
        print(f"{i:>5}", end="")
        for j in range(1, num_columns + 1):
            print(f"{operation(i, j):>5}", end="")
        print()
print_operation_table(operation, num_rows=6, num_columns=6)