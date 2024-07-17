class Phone:
    def __init__(self, name, model, price, color):
        self.name = name
        self.model = model
        self._price = price
        self.__color = color

    @property
    def model(self):
        return self.__dict__['model']

    @model.setter
    def model(self, value):
        if isinstance(value, str):
            self.__dict__['model'] = value
        else:
            raise TypeError

    @model.deleter
    def model(self):
        del self.__dict__['model']
        print("Model o'chirildi")


phone1 = Phone("RedMi", "12C", 170, 'pushti')
print(phone1.__dict__)
del phone1.model
print(phone1.__dict__)
