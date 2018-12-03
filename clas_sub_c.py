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


class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
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

    def print_emp(self, emp):
        if emp in self.employees:
            print('--->', emp.fullname())



dev_1 = Developer('jfkd', 'ureiuw', '60000', 'Python')
dev_2 = Developer('kllfkd', 'deadueoureiuw', '70000', 'C++')
dev_3 = Developer('dasdkllfkd', 'adueoureiuw', '60000', 'C')
dev_4 = Developer('iktkllfkd', 'dsAueoureiuw', '470000', 'JAVA')
dev_5 = Developer('ouyokllfkd', 'Sueoureiuw', '760000', 'C')
dev_6 = Developer('fsgkllfkd', '6ueoureiuw', '750000', 'C#')
dev_7 = Developer('vbndhkllfkd', 'rtu76rueoureiuw', '420000', 'Python')
dev_8 = Developer('kikgkllfkd', 'gtedueoureiuw', '270000', 'Ruby')
print(dev_1.email)
