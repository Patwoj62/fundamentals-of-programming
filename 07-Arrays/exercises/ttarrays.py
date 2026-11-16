import random # moduł do losowania liczb

arr1 = [3, 7, 1, 0, 4] # lista liczb całkowitych
print(arr1) # wyświetla listę

arr2 = [[2, 3], [7, 1], [0, 4]] # lista dwuwymiarowa
print(arr2) # wyświetla listę

arr3 = [7 for i in range(5)] # lista wypełniona piątką wartości 7
print(arr3) # wyświetla listę

arr4 = [i for i in range(1, 10)] # liczby od 1 do 9
print(arr4) # wyświetla listę

arr5 = [i * 2 for i in range(1, 10)] # liczby od 2 do 18
print(arr5) # wyświetla listę

arr6 = [random.randint(1, 20) for i in range(10)] # 10 losowych liczb
print(arr6) # wyświetla listę

arr7 = [[] for i in range(5)] # pięć pustych list
print(arr7) # wyświetla listę

arr8 = [[1 for i in range(2)] for j in range(4)] # tablica 4x2 wypełniona jedynkami
print(arr8) # wyświetla listę

arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)] # tablica 5x3 z losowymi liczbami
print(arr9) # wyświetla listę

arr10 = [4, 0, 3] # tablica z wartościami 4,0,3
print(arr10) # wyświetla listę

arr11 = [0 for i in range(15)] # tablica 15-elementowa z zerami
print(arr11) # wyświetla listę

arr12 = [i for i in range(1, 31)] # liczby całkowite z zakresu 1-30
print(arr12) # wyświetla listę

arr13 = [random.randint(0, 1) for i in range(20)] # 20 losowych zer lub jedynek
print(arr13) # wyświetla listę

arr14 = [[False for i in range(2)] for j in range(5)] # tablica 5x2 wypełniona False
print(arr14) # wyświetla listę