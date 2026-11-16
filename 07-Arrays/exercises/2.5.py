# ===== Zadanie 17 =====

cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'], 
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
] # A = Available, B = Booked

def seats_total(seats):  # oblicza całkowitą liczbę miejsc

    total = 0  # licznik miejsc

    for row in seats:  # przechodzi po wszystkich rzędach
        total += len(row)  # dodaje liczbę miejsc w rzędzie

    return total  # zwraca liczbę wszystkich miejsc


def seats_available(seats):  # oblicza liczbę wolnych miejsc

    available = 0  # licznik wolnych miejsc

    for row in seats:  # przechodzi po rzędach
        for seat in row:  # przechodzi po miejscach
            if seat == 'A':  # sprawdza czy miejsce jest wolne
                available += 1  # zwiększa licznik wolnych miejsc

    return available  # zwraca liczbę wolnych miejsc


def seats_booked(seats):  # oblicza liczbę zajętych miejsc

    booked = 0  # licznik zajętych miejsc

    for row in seats:  # przechodzi po rzędach
        for seat in row:  # przechodzi po miejscach
            if seat == 'B':  # sprawdza czy miejsce jest zajęte
                booked += 1  # zwiększa licznik zajętych miejsc

    return booked  # zwraca liczbę zajętych miejsc


def seat_status(seats, row, place):  # sprawdza status wybranego miejsca

    if seats[row - 1][place - 1] == 'A':  # sprawdza czy miejsce jest wolne
        return "Available"  # zwraca informację o wolnym miejscu

    return "Booked"  # zwraca informację o zajętym miejscu


print("CINEMA INFORMATION TABLE")

print("Total seats:", seats_total(cinema_seats))

print("Seats available:", seats_available(cinema_seats))

print("Seats booked:", seats_booked(cinema_seats))

print("Seat in row 1, place 1:", seat_status(cinema_seats, 1, 1))

print("Seat in row 5, place 5:", seat_status(cinema_seats, 5, 5))

print("Seat in row 3, place 5:", seat_status(cinema_seats, 3, 5))