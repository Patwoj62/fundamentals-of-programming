# ===== Zadanie 13 =====

distances_traveled = [120, 150, 180, 90, 200, 175, 160] # lista przebytych odległości
sorted_distances = sorted(distances_traveled) # sortuje rosnąco za pomocą funkcji built-in sorted()

print(sorted_distances) # wyświetla wynik sortowania

daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18] # lista temperatur
sorted_temperatures = sorted(daily_temperatures, reverse=True) # sortuje malejąco

print(sorted_temperatures) # wyświetla wynik sortowania

file_names = [
"report.docx",
"presentation.pptx",
"data.csv",
"photo.jpg",
"notes.txt",
"invoice.pdf",
"resume.docx",
"budget.xlsx",
"meeting.mp4",
"schedule.pdf"
] # lista nazw plików typu string

sorted_files = sorted(file_names) # sortuje nazwy plików alfabetycznie
print(sorted_files) # wyświetla posortowaną listę plików