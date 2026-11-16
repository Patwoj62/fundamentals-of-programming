# ===== Zadanie 12 =====

def month(n):  # funkcja przyjmuje numer miesiąca, typ int
    months = [  # lista nazw miesięcy, typ list
        'January',  # miesiąc 1
        'February',  # miesiąc 2
        'March',  # miesiąc 3
        'April',  # miesiąc 4
        'May',  # miesiąc 5
        'June',  # miesiąc 6
        'July',  # miesiąc 7
        'August',  # miesiąc 8
        'September',  # miesiąc 9
        'October',  # miesiąc 10
        'November',  # miesiąc 11
        'December'  # miesiąc 12
    ]

    return months[n - 1]  # zwrócenie odpowiedniej nazwy miesiąca