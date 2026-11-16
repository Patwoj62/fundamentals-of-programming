# ===== Zadanie 2 =====

arr = [1, 2, 3, 4, 5]  # lista początkowa typu list

print("Array:", arr)  # wyświetla stan początkowy listy

arr[0] = arr[0] - 1  # zmniejsza pierwszy element o 1
print("Array:", arr)  # wyświetla listę po zmianie

arr[-1] = arr[-1] + 4  # zwiększa ostatni element o 4
print("Array:", arr)  # wyświetla listę po zmianie

arr[len(arr) // 2] = arr[len(arr) // 2] * 2  # mnoży środkowy element przez 2
print("Array:", arr)  # wyświetla końcowy stan listy