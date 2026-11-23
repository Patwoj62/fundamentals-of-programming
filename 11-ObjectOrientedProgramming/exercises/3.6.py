# ===== Zadanie 13 =====

from tv6 import TV

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

    tv.show_status()

    tv.volume_up()
    tv.volume_up()
    tv.volume_up()

    tv.show_status()

    tv.volume_down()

    tv.show_status()

if __name__ == "__main__":
    main()