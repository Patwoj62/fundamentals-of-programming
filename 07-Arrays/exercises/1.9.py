# ===== Zadanie 6 =====

polish_license_plates = [
   'KR5233F',
   'PO6987E',
   'KR16179',
   'BI7192L',
   'KK12255',
   'WA7930T',
   'SK6922I',
   'KK61108',
   'KR90538',
   'BI8052Q',
   'KK54985',
   'LU4864U'
]

counter = 1  # licznik znalezionych tablic

for car_number in polish_license_plates:  # przejście po wszystkich tablicach
    if car_number.startswith("KR") or car_number.startswith("KK"):  # sprawdza Kraków
        print(counter, car_number)  # wyświetla numer porządkowy i tablicę
        counter += 1  # zwiększa licznik