# ===== Zadanie 7 =====

test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

question_number = len(test_results)  # liczba pytań

correct_answers = 0  # licznik poprawnych odpowiedzi

for answer in test_results:  # przechodzi po wszystkich wynikach
    if answer:  # jeśli odpowiedź to True
        correct_answers += 1  # zwiększa licznik poprawnych odpowiedzi

incorrect_answers = question_number - correct_answers  # liczba błędnych odpowiedzi

percentage = (correct_answers / question_number) * 100  # procent poprawnych odpowiedzi

print("TEST STATISTICS")
print("===============")

print("Number of questions:", question_number)
print("Number of correct answers:", correct_answers)
print("Number of incorrect answers:", incorrect_answers)
print("Percentage of correct answers:", percentage, "%")