class TV:

    def __init__(self):

        # telewizor wyłączony
        self.is_on = False

        # aktualny kanał
        self.channel_no = 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):

        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")