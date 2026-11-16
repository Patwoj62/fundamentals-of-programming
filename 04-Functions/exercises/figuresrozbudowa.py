# ===== Zadanie 11 =====

import turtle  # moduł turtle

def draw_square(pen, length):  # funkcja rysująca kwadrat; pen = obiekt Turtle, length = długość boku (int/float)
    for i in range(4): # pętla wykonuje się 4 razy, ponieważ kwadrat ma 4 boki
        pen.forward(length) # rysuje bok o długości length
        pen.right(90) # obraca żółwia o 90 stopni w prawo

def draw_triangle(pen, length): # rysowanie trójkąta równoramiennego
    for i in range(3): # pętla wykonuje się 3 razy, ponieważ trójkąt ma 3 boki
        pen.forward(length)
        pen.left(120) # obrót o 120 stopni potrzebny do narysowania trójkąta

def draw_rectangle(pen, length_a, length_b): # funkcja rysująca prostokąt; length_a i length_b to długości boków
    for i in range(2): # pętla wykonuje się 2 razy, ponieważ są dwie pary boków
        pen.forward(length_a) # rysuje dłuższy bok prostokąt
        pen.right(90) # obrót o 90 stopni
        pen.forward(length_b)
        pen.right(90)