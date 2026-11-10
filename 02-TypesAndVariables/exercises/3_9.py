# ===== Zadanie 16 ====

total = 8000000000                            # populacja świata
north = 7200000000                            # populacja półkuli północnej
south = total - north                         # populacja półkuli południowej

print("World population:", total)             # wyświetlenie populacji świata
print("Northern Hemisphere:", north)          # liczba mieszkańców północy
print("Northern Hemisphere in %:", north / total * 100)  # procent mieszkańców północy
print("Southern Hemisphere:", south)          # liczba mieszkańców południa
print("Southern Hemisphere in %:", south / total * 100)  # procent mieszkańców południa