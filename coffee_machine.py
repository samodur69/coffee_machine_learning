class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    balance = 550
    state = 'choosing_action'
    prompt1 = 'Write action (buy, fill, take, remaining, exit): \n >'
    prompt2 = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n >'

#  input with message message stored in prompt1
    def wait(self, prompt):
        action = input(prompt)
        return action

#    def inp(self):
#        inte = int(input())
#        return inte

#  input with message message stored in prompt2
    def choosing_coffee(self, prompt):
        coffee = input(prompt)
        return coffee

#  take money from balance and balance = 0
    def take(self):
        print(f'I gave you ${self.balance}')
        self.balance = 0

#  refill resources with input
    def refill(self, water_add, milk_add, beans_add, cups_add):
        self.water += water_add
        self.milk += milk_add
        self.beans += beans_add
        self.cups += cups_add

    def process_input(self, action):
        if action == 'take':
            cm.take()
        elif action == 'remaining':
            cm.stock()
        elif action == 'fill':
            w = int(input('Write how many ml of water do you want to add: \n >'))
            m = int(input('Write how many ml of milk do you want to add: \n >'))
            b = int(input('Write how many grams of coffee beans do you want to add: \n >'))
            c = int(input('Write how many disposable cups do you want to add: \n >'))
            cm.refill(w, m, b, c)
        elif action == 'buy':
            self.state = 'choosing_type_coffee'
            action = cm.wait(self.prompt2)
            if action == '1':
                if cm.check(250, 0, 16, 1) == True:
                    cm.prepare(250, 0, 16, 1, 4)
            elif action == '2':
                if cm.check(350, 75, 20, 1) == True:
                    cm.prepare(350, 75, 20, 1, 7)
            elif action == '3':
                if cm.check(200, 100, 12, 1) == True:
                    cm.prepare(200, 100, 12, 1, 6)
            else:
                pass

    def stock(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.balance} of money')

    def check(self, w, m, b, c):
        if self.water < w:
            print('Sorry, not enough water')
            return False
        elif self.milk < m:
            print('Sorry, not enough milk')
            return False
        elif self.beans < b:
            print('Sorry, not enough coffee beans')
            return False
        elif self.cups < c:
            print('Sorry, not enough disposable cups')
            return False
        else:
            print('I have enough resources, making you a coffee!')
            return True

    def prepare(self, w, m, b, c, baksi):
        self.water -= w
        self.milk -= m
        self.beans -= b
        self.cups -= c
        self.balance += baksi
        self.state = 'choosing_action'

cm = CoffeeMachine()
while True:
    action = cm.wait(cm.prompt1)
    if action != 'exit':
        cm.process_input(action)
    else:
        break
