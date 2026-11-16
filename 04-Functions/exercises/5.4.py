# ===== Zadanie 10 =====

import turtle  # moduł turtle
import figures  # własny moduł

window = turtle.Screen()  # utworzenie okna
window.bgcolor("lightgreen")  # kolor tła

pen = turtle.Turtle()  # utworzenie żółwia
pen.speed(5)  # prędkość rysowania

figures.draw_square(100)  # rysowanie kwadratu

pen.hideturtle()  # ukrycie żółwia
window.mainloop()  # pozostawienie okna otwartego