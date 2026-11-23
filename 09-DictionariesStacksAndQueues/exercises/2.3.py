# ===== Zadanie 7 =====

all_students = {"Alice", "John", "Sara", "Bob"}  # zbiór wszystkich studentów (set)

attended_students = {"Alice", "Bob"}  # zbiór obecnych studentów (set)

absent_students = all_students - attended_students  # różnica zbiorów (Difference)

print(absent_students)  # wyświetlenie nieobecnych studentów