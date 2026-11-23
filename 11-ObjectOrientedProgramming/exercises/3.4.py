# ===== Zadanie 11 =====

from tv4 import TV

def main():

    tv = TV()

    tv.show_status()

    tv.turn_on()

    tv.show_status()

    tv.show_channels()

    tv.set_channels([
        "TVP1",
        "TVP2",
        "Polsat",
        "TVN",
        "Filmbox",
        "Discovery"
    ])

    tv.show_channels()

    tv.show_status()

    tv.turn_off()

if __name__ == "__main__":
    main()