import re


class ClassVar:
    name = 'Or'
    surname = 'keren'

    def change_name(self, name):
        self.name = name
    
    def change_surname(self, surname):
        self.surname = surname
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname

x = ClassVar()
y = ClassVar()
print(x.get_name())
x.change_name("moshe")
print(x.get_name())
print(y.get_name())

