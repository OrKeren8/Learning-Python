class Parent:

    def print_last_name(self):
        print('Kuku')


class Child(Parent):

    def print_first_name(self):
        print('Or')

    # over write the function in parent's class
    # def print_last_name(self):
    #     print('Keren')


Or = Child()
Or.print_first_name()
Or.print_last_name()