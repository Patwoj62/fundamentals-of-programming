# ===== Zadanie 1 =====

# definicja klasy Student
class Student:

    def __init__(self):  # konstruktor klasy
        self.name = ""  # imię studenta, typ str
        self.age = 0  # wiek studenta, typ int
        self.field_of_study = ""  # kierunek studiów, typ str


def main():  # funkcja główna programu

    student1 = Student()  # utworzenie obiektu Student
    student2 = Student()  # utworzenie obiektu Student
    student3 = Student()  # utworzenie trzeciego studenta

    student1.name = "Dominic"  # przypisanie imienia
    student1.age = 19  # przypisanie wieku
    student1.field_of_study = "Computer Science"  # przypisanie kierunku

    student2.name = "Olivia"  # przypisanie imienia
    student2.age = 21  # przypisanie wieku
    student2.field_of_study = "Economics"  # przypisanie kierunku

    student3.name = "Michael"  # przypisanie imienia
    student3.age = 20  # przypisanie wieku
    student3.field_of_study = "Mathematics"  # przypisanie kierunku

    print("LIST OF STUDENTS")  # nagłówek
    print("================")  # separator

    print(f"{student1.name}, {student1.age} years old, {student1.field_of_study}")  # dane studenta 1
    print(f"{student2.name}, {student2.age} years old, {student2.field_of_study}")  # dane studenta 2
    print(f"{student3.name}, {student3.age} years old, {student3.field_of_study}")  # dane studenta 3


if __name__ == "__main__":  # sprawdzenie uruchomienia pliku
    main()  # wywołanie funkcji głównej