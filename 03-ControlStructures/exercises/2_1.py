# ===== Zadanie 7 =====

size = input('Enter size symbol: ')  # pobranie symbolu rozmiaru

if size == 'S':  # sprawdzenie czy podano S
    print('S: Small size')  # wyświetlenie małego rozmiaru
elif size == 'M':  # sprawdzenie czy podano M
    print('M: Medium size')  # wyświetlenie średniego rozmiaru
elif size == 'L':  # sprawdzenie czy podano L
    print('L: Large size')  # wyświetlenie dużego rozmiaru
elif size == 'XL':  # sprawdzenie czy podano XL
    print('XL: Extra large size')  # wyświetlenie bardzo dużego rozmiaru
else:  # gdy podano nieznany symbol
    print('Incorrect symbol')  # komunikat o błędnym symbolu