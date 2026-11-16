# ===== Zadanie 11 =====

import turtle # moduł turtle
import figuresrozbudowa # własny moduł

window = turtle.Screen() # utworzenie okna
window.bgcolor("lightgreen") # ustawienie tła

pen = turtle.Turtle() # utworzenie żółwia
pen.speed(5) # szybkość rysowania

# kwadrat 1
pen.penup() # ruch bez rysowania
pen.goto(-200, 100) # przejście do pozycji
pen.setheading(0) # ustawienie kierunku w prawo
pen.pendown() # rozpoczęcie rysowania
figuresrozbudowa.draw_square(pen, 80) # rysowanie kwadratu

# kwadrat 2
pen.penup()
pen.goto(100, 100)
pen.setheading(0)
pen.pendown()
figuresrozbudowa.draw_square(pen, 80)

# trójkąt 1
pen.penup()
pen.goto(-200, -50)
pen.setheading(0)
pen.pendown()
figuresrozbudowa.draw_triangle(pen, 80)

# trójkąt 2
pen.penup()
pen.goto(100, -50)
pen.setheading(0)
pen.pendown()
figuresrozbudowa.draw_triangle(pen, 80)

# prostokąt 1
pen.penup()
pen.goto(-200, -200)
pen.setheading(0)
pen.pendown()
figuresrozbudowa.draw_rectangle(pen, 120, 60)

# prostokąt 2
pen.penup()
pen.goto(100, -200)
pen.setheading(0)
pen.pendown()
figuresrozbudowa.draw_rectangle(pen, 120, 60)

pen.hideturtle() # ukrycie żółwia
window.mainloop() # uruchomienie pętli programu