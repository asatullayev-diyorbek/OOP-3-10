class Home:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __setattr__(self, a_name, value):
        if a_name in ['name', 'address']:
            self.__dict__[a_name] = value
        else:
            raise NameError("Noto'g'ri atribut nomi")

    def __getattr__(self, a_name):
        return "Bunday atribut mavjud emas"

    def __getattribute__(self, a_name):
        try:
            return super().__getattribute__(a_name)
        except AttributeError:
            return self.__getattr__(a_name)


class Window(Home):
    def __init__(self, name, address, window_type):
        super().__init__(name, address)
        self.window_type = window_type

    def open_window(self):
        return f"{self.window_type} ochildi."


class Door(Home):
    def __init__(self, name, address, door_type):
        super().__init__(name, address)
        self.door_type = door_type

    def open_door(self):
        return f"{self.door_type} eshik ochildi."


class Room(Home):
    def __init__(self, name, address, room_type):
        super().__init__(name, address)
        self.room_type = room_type

    def describe_room(self):
        return f"Bu xona {self.room_type} xonadir."


window = Window("Meniki", "Farg'ona shahar", "Katta")
door = Door("Meniki", "Farg'ona shahar", "Kirish")
room = Room("Meniki", "Farg'ona shahar", "Yotoq")

print(window.open_window())   
print(door.open_door())
print(room.describe_room())
