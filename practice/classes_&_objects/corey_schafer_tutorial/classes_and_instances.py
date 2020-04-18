class Employee:# set a class with a given name

    raise_amount = 1.04# class variable, every object of the class will have the same variable and its value in it
    num_of_employees = 0

    def __init__(self, first, last, pay):# make an initialized function which happen right after creating new object of the class
        """
        set some initialize variables which must be configure while creating a new object of this class
        """
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1# calls the class var by the class itself to make it changed for all of the objects from now on

    @property# this decorator makes the email function to behave like a variable, we call email as it was a variable. because email depends on other changeable vars it should change with them too
    def email(self):
        return "{} {}.email.com".format(self.first, self.last)

    '''
    make a usual function for the class            
    :return: the full name by a string with the following format
    '''
    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @full_name.setter# this decorator helps us change the full name as is it was variable
    def full_name(self, new_name):
        first, last = new_name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter# this decorator helps us delete the full name as is it was variable
    def full_name(self):
        self.first = None
        self.last = None
        print('delete name')

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)# the calculation of the payment of the employee is done with the class variable raise_amount

    @classmethod# this line tell that the function under it will be a class function which means that it affect every object of the class
    def set_raise_amount(cls, amount):# this line takes the class itself as an argument
        cls.raise_amount = amount# takes the class itself as the object of the variable instead of an instance of the class

    @classmethod
    def from_string(cls, emp_str):
        """
        makes a new object with a given string
        :param emp_str: a string which contains the init params of the class
        :return: a new object
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        """
        this type of method used inside the class and doesnt interacts with the class or with it's objects at all.
        """
        if day.weekday() == 4 or day.weekday() == 5:
            return True
        else:
            return False

    def __repr__(self):# this is a spatial function which display e new format of text while printing the object itself for debugging
        return "'{}', '{}', {}".format(self.first, self.last, self.pay)

    def __str__(self):# this is a spatial function which display e new format of text while printing the object itself for the user
        return "{}, {}".format(self.full_name, self.email)

    def __add__(self, other):# add function - called with the sign +
        if isinstance(other, Employee):# check if the adder is in the same type of the employee object
            return self.pay + other.pay

class Developer(Employee):# make a class that inherent everything from Employee class
    raise_amount = 1.10# changes the value of the var for every object created by the class developer

    def __init__(self, first, last, pay, prog_lang):# (not necessary) if we want to create precise initialized function for the developer we can do this with the __init__ function
        super().__init__(first, last, pay)# to make our life easier we call the init function of the parent for the common variables
        # Employee.__init__(first, last, pay)# we can use this line too but its better to use super()
        self.prog_lang = prog_lang

class Manager(Employee):# a good example why we should use inheritance

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name)

def main():
    # make an object of the class Employee with a given name,
    # in the Parenthesis the values of the instance variables are writen
    emp_1 = Employee('corey', 'schemaher', 50000)
    emp_2 = Employee('or', 'keren', 1000000)

    emp_1.some_instance_variable = 'the value of the instance variable'# set an instance variable to the object emp_1 of Employee class
    print(emp_1)# print the object emp_1 of Employee class
    print(emp_2.full_name)
    print(Employee.__dict__)# shoes the variables and the methods in the class
    print(emp_1.num_of_employees)# this line shoes that the number of imp influenced by the class's objects

    Employee.set_raise_amount(1.07)# call to the class function, we can call to the function from an object but its better understood by calling it from the class itself
    print('the new raise amount is: ', emp_1.raise_amount)# checks the variable by an object of the class

    new_emp = Employee.from_string('koko-shulman-60000')# makes a new employee with a string by the class method "from_string"
    print('{} {}, payment: {}'.format(new_emp.first, new_emp.last, new_emp.pay))

    import datetime
    my_date = datetime.date(2020, 4, 17)
    print('if this is a weekend day? : ', Employee.is_workday(my_date))# can be used with an object or the class itself

    dev_1 = Developer('roei', 'alfasi', 50000, 'python')# creating an object of Developer class

    mgr_1 = Manager('big or', 'keren', 150000, [emp_1, dev_1])# making new Manager object
    print(mgr_1.print_emps())# call to function with in the object

    print(Employee.num_of_employees)# shoes the number of objects were opened by the class Employee, include the its inheritance objects

    print(isinstance(dev_1, Developer))# checks if the first argument (object) is an instance of the second argument (class)
    print(issubclass(Developer, Employee))# checks if Developer is a subclass of Employee

    print(mgr_1)# print the str function from manager
    print(str(mgr_1))# print the str function from manager
    print(repr(mgr_1))# print the repr function from manager

    print(dev_1 + emp_1)# call the __adder__ function

    del dev_1.full_name# call the deleter function of the decorator deleter


if __name__ == "__main__":
    main()
