class Home:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __setattr__(self, a_name, value):
        if a_name in ['name', 'address']:
            self.__dict__[a_name] = value
        else:
            raise NameError

    def __getattr__(self, a_name):
        return "Bunday atribut mavjud emas"

    def __getattribute__(self, a_name):
        return super().__getattribute__(a_name)


h1 = Home("Meniki", "Farg'ona shahar")
# h1.color = "sariq"
# print(h1.color)
print(h1.address)