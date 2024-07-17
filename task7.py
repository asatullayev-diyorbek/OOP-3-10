from abc import ABC, abstractmethod


class Tv(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class SmartTv(Tv):
    def __init__(self):
        self.status = False

    def turn_on(self):
        if self.status:
            print("Smart TV avvalroq yoqilgan")
        else:
            print("Smart TV yoqildi.")
            self.status = True

    def turn_off(self):
        if not self.status:
            print("SmartTV avvalroq o'chirilgan")
        else:
            print("SmartTV o'chirildi.")
            self.status = False


smart_tv = SmartTv()
smart_tv.turn_on()
smart_tv.turn_on()
smart_tv.turn_off()
smart_tv.turn_off()
