# ===== Zadanie 45 =====

x = int(input('x = '))  # współrzędna x
y = int(input('y = '))  # współrzędna y

if x == 0 and y == 0:  # początek układu
    print('Point P(0,0) is at the origin')

elif x == 0:  # oś Y
    print(f'Point P({x},{y}) is on the Y axis')

elif y == 0:  # oś X
    print(f'Point P({x},{y}) is on the X axis')

elif x > 0 and y > 0:  # I ćwiartka
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')

elif x < 0 and y > 0:  # II ćwiartka
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')

elif x < 0 and y < 0:  # III ćwiartka
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')

else:  # IV ćwiartka
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')