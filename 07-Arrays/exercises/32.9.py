# ===== Zadanie 47 =====

def create_2d_arr(x, y):  # funkcja tworząca tablicę

    return [[0 for i in range(y)] for j in range(x)]  # tworzy tablicę x na y


array = create_2d_arr(3, 5)  # tworzy tablicę 3x5

for row in array:  # przechodzi po wierszach

    print(row)  # wyświetla wiersz