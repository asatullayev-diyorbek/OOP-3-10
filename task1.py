import os
FOLDER_PATH = "c:\\Users\\REPUBLIC OF GAMERS\\Documents\\"  # bu mening kompyuterimdagi documents papkasini manzili
OLD_NAME = "product.xlsx"
NEW_NAME = "my_products.xlsx"


class Rename:
    def __init__(self, f_name):
        self.f_name = f_name

    @property
    def f_name(self):
        return self.__dict__['f_name']

    @f_name.setter
    def f_name(self, f_name):
        if os.path.exists(f_name):
            self.__dict__['f_name'] = f_name
        else:
            raise FileNotFoundError("Fayl topilmadi!")

    def rename(self, new_name):
        try:
            os.rename(self.f_name, new_name)
            print("O'zgartirildi")
        except Exception as e:
            raise print(e)


file1 = Rename(FOLDER_PATH + OLD_NAME)
file1.rename(FOLDER_PATH + NEW_NAME)
