stack = []  # utworzenie pustego stosu (list)

stack.append(2)  # dodanie liczby 2 na stos
stack.append(3)  # dodanie liczby 3 na stos
stack.append(7)  # dodanie liczby 7 na stos
stack.append(4)  # dodanie liczby 4 na stos
stack.append(1)  # dodanie liczby 1 na stos
stack.append(9)  # dodanie liczby 9 na stos
stack.append(8)  # dodanie liczby 8 na stos

number1 = stack.pop()  # pobranie ostatniego elementu ze stosu (8)
number2 = stack.pop()  # pobranie kolejnego elementu ze stosu (9)

last_two_sum = number1 + number2  # obliczenie sumy dwóch ostatnich liczb

print("Sum of last two numbers:", last_two_sum)  # wyświetlenie wyniku

remaining_sum = 0  # zmienna przechowująca sumę pozostałych elementów (int)

while len(stack) > 0:  # wykonuj dopóki stos nie jest pusty
    remaining_sum += stack.pop()  # pobierz element i dodaj do sumy

print("Sum of remaining elements:", remaining_sum)  # wyświetlenie wyniku

student = {  # utworzenie słownika
    'name': 'John',  # imię, str
    'age': 22,  # wiek, int
    'major': 'Computer Science'  # kierunek studiów, str
}

print(student['name'])  # odczyt wartości dla klucza name

student['grade'] = 'A'  # dodanie nowej pary klucz-wartość

student['age'] = 23  # modyfikacja istniejącej wartości

del student['major']  # usunięcie elementu o kluczu major

print(student)  # wyświetlenie końcowej zawartości słownika

fruits = {  # słownik owoców
    'apple': 3,
    'banana': 5,
    'orange': 2
}

for fruit in fruits:  # iteracja po kluczach
    print(fruit)  # wyświetlenie nazwy owocu

for count in fruits.values():  # iteracja po wartościach
    print(count)  # wyświetlenie ilości

for fruit, count in fruits.items():  # iteracja po parach klucz-wartość
    print(f"The count of {fruit} is {count}")  # wyświetlenie komunikatu
    
    person = {  # słownik osoby
    'name': 'Alice',  # imię
    'age': 30  # wiek
}

if 'name' in person:  # sprawdzenie czy klucz istnieje
    print("Name is present in the dictionary.")  # komunikat gdy istnieje
else:  # w przeciwnym przypadku
    print("Name is not present.")  # komunikat gdy nie istnieje