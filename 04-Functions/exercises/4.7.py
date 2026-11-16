# ===== Zadanie 6 =====

def icao(letter):  # definicja funkcji zwracającej słowo ICAO dla podanej litery
    letter = letter.capitalize()  # zamiana litery na wielką literę, typ str

    if letter == 'A':  # sprawdzenie czy litera to A
        icao_name = 'Alfa'  # przypisanie słowa ICAO
    elif letter == 'B':
        icao_name = 'Bravo' 
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:  # jeśli znak nie jest literą alfabetu
        icao_name = '???'  # wartość domyślna

    return icao_name  # zwrócenie słowa ICAO

# Function usage
name = input('Enter your name: ')  # pobranie imienia od użytkownika, typ str

print('ICAO words for spelling out your name:')  # wyświetlenie nagłówka

for char in name:  # przejście po każdym znaku imienia
    word = icao(char)  # wywołanie funkcji icao() dla bieżącej litery
    print(word, end=" ")  # wyświetlenie słowa ICAO w jednej linii