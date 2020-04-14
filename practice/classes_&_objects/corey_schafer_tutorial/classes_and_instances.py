# set a class with a given name
class Employee:

    # make an initialized function which happen right after creating new object of the class
    def __init__(self, first, last, pay):

        # set some initialize variables which must be configure while creating a new object of this class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # make a usual function for the class
    def full_name(self):

        # print the first and the last name by the given format
        return '{} {}'.format(self.first, self.last)


# make an object of the class Employee with a given name,
# in the Parenthesis the values of the instance variables are writen
emp_1 = Employee('corey', 'schemaher', 50000)
emp_2 = Employee('or', 'keren', 1000000)

# set an instance variable to the object emp_1 of Employee class
emp_1.some_instance_variable = 'the value of the instance variable'

# print the object emp_1 of Employee class
print(emp_1)
print(emp_2.full_name())