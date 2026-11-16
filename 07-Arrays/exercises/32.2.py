# ===== Zadanie 40 =====

import random  # moduł do losowania

def rand_elem(array):  # funkcja zwracająca losowy element

    return random.choice(array)  # wybiera losowy element listy


numbers = [10, 20, 30, 40, 50]  # lista liczb

print(rand_elem(numbers))  # wyświetla losowy element

print(rand_elem(numbers))  # wyświetla losowy element

print(rand_elem(numbers))  # wyświetla losowy element

print(rand_elem(numbers))  # wyświetla losowy element