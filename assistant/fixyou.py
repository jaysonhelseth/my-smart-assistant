from pygame import mixer

class FixYou:
    def __init__(self) -> None:
        self.mixer: mixer = mixer
        self.mixer.init()
        self.mixer.music.load("./music/FixYou.mp3")
        self.loop_count = 5

    def toggle(self, value) -> None:
        if value == "start":
            self.__start()

        if value == "stop":
            self.__stop()

    def __start(self) -> None:
        self.mixer.music.play(self.loop_count)

    def __stop(self) -> None:
        self.mixer.music.stop()