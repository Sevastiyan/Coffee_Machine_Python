class Machine:

    def __init__(self, water, milk, beans, cups, money):
        self.on = True
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def turn_off(self):
        print('Turning off')
        self.on = False

    def __str__(self):
        return str('The coffee machine has:\n'
               '{} of water\n'
               '{} of milk\n'
               '{} of beans\n'
               '{} of cups\n'
               '{} of money'.format(self.water, self.milk, self.beans, self.cups, self.money))

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.beans += int(input('write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('White how many disposable cups of coffee do you want to add: '))

    def take(self):
        print('I gave you $' + str(self.money))
        self.money = 0

    def check(self, coffee):
        limit = need(coffee)
        if self.water < limit[0]:
            print('Sorry I need more water')
        elif self.milk < limit[1]:
            print('Sorry I need more milk')
        elif self.beans < limit[2]:
            print('Sorry I need more beans')
        elif self.cups < limit[3]:
            print('Sorry I need more cups')
        else:
            self.make_coffee(coffee)

    def make_coffee(self, coffee):
        print('I have enough resources. Making you a coffee...')
        self.cups -= 1
        if coffee == '1':
            self.water -= 250
            self.beans -= 16
            self.money += 4
        elif coffee == '2':
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
        elif coffee == '3':
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6

def need(coffee):
    limit = [1, 2, 3, 4]
    if coffee == '1':
        limit[0] = 250
        limit[1] = 0
        limit[2] = 16
        limit[3] = 1
    elif coffee == '2':
        limit[0] = 350
        limit[1] = 75
        limit[2] = 20
        limit[3] = 1
    elif coffee == '3':
        limit[0] = 200
        limit[1] = 100
        limit[2] = 12
        limit[3] = 1
    return limit