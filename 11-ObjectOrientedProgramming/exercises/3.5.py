# ===== Zadanie 12 =====

from tv5 import TV

def main():

    tv = TV()

    tv.set_channels([
        "TVP1",
        "TVP2",
        "Polsat",
        "TVN",
        "Filmbox",
        "Discovery",
        "National Geographic"
    ])

    tv.turn_on()

    tv.set_channel(1)
    tv.show_status()

    tv.set_channel(4)
    tv.show_status()

    tv.set_channel(6)
    tv.show_status()

    tv.set_channel(7)
    tv.show_status()

if __name__ == "__main__":
    main()