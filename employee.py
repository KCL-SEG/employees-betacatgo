'''Employee pay calculator.'''
'''ENTER YOUR SOLUTION HERE!'''

class Contract:
    def __init__(self, type, salary, wage, hour):
        self.type = type
        self.salary = salary
        self.wage = wage
        self.hour = hour
    
    def get_pay(self):
        if self.type == 'monthly':
            return self.salary
        elif self.type == 'hourly':
            return self.wage * self.hour

    def __str__(self):
        prefix = 'works on a '
        if self.type == 'monthly':
            return prefix + 'monthly salary of ' + str(self.salary)
        elif self.type == 'hourly':
            return prefix + 'contract of ' + str(self.hour) + ' hours at ' \
                        + str(self.wage) + '/hour'

class Commission:
    def __init__(self, type, bonus, landed, per):
        self.type = type
        self.bonus = bonus
        self.landed = landed
        self.per = per
    
    def get_pay(self):
        if self.type == 'bonus':
            return self.bonus
        elif self.type == 'contract':
            return self.landed * self.per
        elif self.type == 'none':
            return 0
        
    def __str__(self):
        prefix = ' and receives a '
        if self.type == 'bonus':
            return str(prefix + 'bonus commission of ' + str(self.bonus))
        elif self.type == 'contract':
            return str(prefix + 'commission for ' + str(self.landed) \
                        + ' contract(s) at ' + str(self.per) + '/contract')
        elif self.type == 'none':
            return ''

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_pay()

    def __str__(self):
        return self.name + ' ' + str(self.contract) + str(self.commission) \
                    + '. Their total pay is ' + str(self.get_pay()) + '.'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract('monthly', 4000, 0, 0), Commission('none', 0, 0, 0))
print(str(billie))
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract('hourly', 0, 25, 100), Commission('none', 0, 0, 0))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract('monthly', 3000, 0, 0), Commission('contract', 0, 4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract('hourly', 0, 25, 150), Commission('contract', 0, 3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract('monthly', 2000, 0, 0), Commission('bonus', 1500, 0, 0))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract('hourly', 0, 30, 120), Commission('bonus', 600, 0, 0))
