# ===== Zadanie 11 =====

def bubble_sort(arr):  # funkcja sortująca listę metodą Bubble Sort

    n = len(arr)  # liczba elementów listy

    for i in range(n):  # licznik przebiegów sortowania
        for j in range(0, n - i - 1):  # porównuje sąsiednie elementy

            if arr[j] > arr[j + 1]:  # sprawdza czy elementy są w złej kolejności

                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # zamienia miejscami elementy

    return arr  # zwraca posortowaną listę


car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]  # lista spalania

print(car_fuel_consumption)  # wyświetla listę przed sortowaniem

sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption.copy())  # tworzy posortowaną kopię listy

print(sorted_car_fuel_consumption)  # wyświetla listę po sortowaniu


bank_transactions = [-150, -20, 300, -45, -60, 500, -120]  # lista transakcji

print(bank_transactions)  # wyświetla dane przed sortowaniem

sorted_bank_transactions = bubble_sort(bank_transactions.copy())  # sortuje dane

print(sorted_bank_transactions)  # wyświetla dane po sortowaniu