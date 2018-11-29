class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Abc', 'Cba', 50000)
emp_2 = Employee('Def', 'Fed', 50000)
#print(emp_1.fullname())
#print('{} {}'.format(emp_1.first, emp_1.last))
print (emp_1.first + ' ' + emp_1.last)
