# ===== Zadanie 36 =====

def second_largest(arr):  # funkcja zwracająca drugą największą liczbę

    sorted_arr = sorted(arr)  # sortuje liczby rosnąco

    return sorted_arr[-2]  # zwraca przedostatni element


# Returns difference between largest and smallest value

def difference(arr):  # funkcja obliczająca różnicę

    return max(arr) - min(arr)  # zwraca różnicę max-min


# Returns median

def median(arr):  # funkcja zwracająca medianę

    sorted_arr = sorted(arr)  # sortuje tablicę

    return sorted_arr[len(sorted_arr) // 2]  # zwraca środkowy element


# Returns minimum and maximum values

def min_max(arr):  # funkcja zwracająca min i max

    return [min(arr), max(arr)]  # zwraca listę z min i max


# Returns array as string

def array_string(arr):  # funkcja zamieniająca tablicę na tekst

    return "-".join(str(x) for x in arr)  # łączy elementy znakiem -