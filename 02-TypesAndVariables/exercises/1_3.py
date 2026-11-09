# ===== Zadanie 3 =====

height = input("Enter your height in cm: ")  # pobranie wzrostu od użytkownika
weight = input("Enter your weight in kg: ")  # pobranie wagi od użytkownika

height = int(height)                         # zamiana tekstu na liczbę całkowitą
weight = int(weight)                         # zamiana tekstu na liczbę całkowitą

bmi = weight / (height / 100) ** 2          # obliczenie BMI

bmi = round(bmi, 2)                         # zaokrąglenie BMI do 2 miejsc

print("Your BMI is", bmi)                   # wyświetlenie BMI
print("Check on the Internet if your BMI is ok!!")  # komunikat dla użytkownika