# ===== Zadanie 9 =====

categories = ["Food", "Transport", "Rent", "Entertainment"]  # lista kategorii wydatków
expenses = [500, 150, 1000, 200]  # lista kosztów odpowiadających kategoriom

max_expense = max(expenses)  # znajduje najwyższy wydatek

index = expenses.index(max_expense)  # pobiera indeks najwyższego wydatku

print("Most expensive category:", categories[index])  # wyświetla nazwę kategorii
print("Expense:", max_expense)  # wyświetla wartość wydatku