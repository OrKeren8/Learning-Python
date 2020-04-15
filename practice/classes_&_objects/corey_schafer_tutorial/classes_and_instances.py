"""
set a class with a given name
"""
class Employee:

    """
    class variable, every class will have the same variable and its value in it
    """
    raise_amount = 1.04

    """
    make an initialized function which happen right after creating new object of the class
    """
    def __init__(self, first, last, pay):

        """
        set some initialize variables which must be configure while creating a new object of this class
        """
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    '''
    make a usual function for the class            
    :return: the full name by a string with the following format
    '''
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):

        """
        the calculation of the payment of the employee is done with the class variable raise_amount
        """
        self.pay = int(self.pay * self.raise_amount)

'''
make an object of the class Employee with a given name,
in the Parenthesis the values of the instance variables are writen
'''
emp_1 = Employee('corey', 'schemaher', 50000)
emp_2 = Employee('or', 'keren', 1000000)

'''
set an instance variable to the object emp_1 of Employee class
'''
emp_1.some_instance_variable = 'the value of the instance variable'

'''
print the object emp_1 of Employee class
'''
print(emp_1)
print(emp_2.full_name())