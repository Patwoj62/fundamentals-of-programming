# ===== Zadanie 10 =====

import turtle  # moduł turtle

def draw_square(length):  # funkcja rysująca kwadrat
    for i in range(4):  # 4 boki
        turtle.forward(length)  # rysowanie boku
        turtle.right(90)  # obrót o 90 stopni