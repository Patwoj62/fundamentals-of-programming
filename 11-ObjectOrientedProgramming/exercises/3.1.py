# ===== Zadanie 8 =====

from tv import TV

def main():

    # utworzenie telewizora
    tv = TV()

    # pokazanie statusu
    tv.show_status()

    # włączenie telewizora
    tv.turn_on()

    # pokazanie statusu
    tv.show_status()

    # wyłączenie telewizora
    tv.turn_off()

    # pokazanie statusu
    tv.show_status()

if __name__ == "__main__":
    main()