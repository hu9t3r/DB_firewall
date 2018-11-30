class Employee:
    no_of_emp =0
    pay_raise = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        #Employee.no_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def set_pay_rasie(cls, amount):
        cls.pay_raise = amount

    @classmethod
    def split_emp_name(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #def apply_raise(self):
    #    self.pay = int(self.pay * self.pay_raise)

#print(Employee.no_of_emps)

emp_1 = Employee('Abc', 'Cba', 50000)
emp_2 = Employee('Def', 'Fed', 50000)
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Freeman-Mc-40000'
emp_str_3 = 'Joyi-Kate-30000'

#first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee.split_emp_name(emp_str_1)
new_emp_2 = Employee.split_emp_name(emp_str_2)
new_emp_3 = Employee.split_emp_name(emp_str_3)

print(new_emp_1.email)
print(Employee.fullname(new_emp_2))
#print(emp_1.fullname())
#print('{} {}'.format(emp_1.first, emp_1.last))
#print (emp_1.first + ' ' + emp_1.last)
#print(Employee.fullname(emp_1))
#print(Employee.pay_raise)
#Employee.apply_raise(emp_1)
#print(emp_1.pay)
