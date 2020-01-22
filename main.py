import sys
import machine
import time

def main():

    my_machine = start()

    while my_machine.on:
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action == 'buy':
            buy(my_machine)
        elif action == 'remaining':
            print(my_machine)
        elif action == 'take':
            my_machine.take()
        elif action == 'fill':
            my_machine.fill()
        elif action == 'exit':
            my_machine.turn_off()


def start():
    print('Starting machine')
    time.sleep(1)
    print('Coffee Machine is ready')
    return machine.Machine(400, 540, 120, 9, 550)


def buy(my_machine):
    options = ['1', '2', '3', 'back']
    coffee = input('What do you want to buy? '
                   '1 - espresso, '
                   '2 - latte, '
                   '3 - cappuccino: '
                   'back - to main menu: ')
    if coffee == 'back':
        return
    elif not coffee in options:
        print('Pick a real option!')
        buy(my_machine)
    else:
        my_machine.check(coffee)


if __name__ == '__main__':
    main()
