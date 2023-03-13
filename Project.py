from datetime import datetime
import csv
import os.path

# pizza superclassının oluşturulması
class Pizza:
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost
    
    def get_description(self):
        return self._description
    
    def get_cost(self):
        return self._cost
    
# pizza superclassına bağlı subclassların oluşturulması
class Classic(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 5.99)
        
        
class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 6.99)
        
        
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza", 7.99)
        
        
class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 4.99)

# pizza superclassına bağlı decorator classının oluşturulması
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
        self._description = None
        self._cost = None

    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

    def get_description(self):
        return  self.component.get_description() + " " + super().get_description()

# decarator superclassına bağlı olan sosların oluşturulması
class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Zeytin"
        self._cost = 2.0

class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Mantar"
        self._cost = 3.0

class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Keçi Peyniri"
        self._cost = 4.0

class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Et"
        self._cost = 5.0

class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Soğan"
        self._cost = 1.5

class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Mısır"
        self._cost = 2.5

def main():
    menu = open("Menu.txt","r",encoding="utf-8")
    read = menu.read()
    print(read)
    pizzaChoice = int(input("Bir Pizza Seçiniz: "))
    sauceChoices = []
    while True:
        sauceChoice = int(input("Lütfen eklemek istediğiniz sosları seçiniz, Çıkmak için 0'a basın: "))
        if sauceChoice == 0:
            break
        else:
            sauceChoices.append(sauceChoice)

    if pizzaChoice == 1:
        pizza = Classic()
    elif pizzaChoice == 2:
        pizza = Margherita()
    elif pizzaChoice == 3:
        pizza = TurkPizza()
    elif pizzaChoice == 4:
        pizza = SadePizza()

    for sauceChoice in sauceChoices:
        if sauceChoice == 11:
            pizza = Olives(pizza)
        elif sauceChoice == 12:
            pizza = Mushrooms(pizza)
        elif sauceChoice == 13:
            pizza = GoatCheese(pizza)
        elif sauceChoice == 14:
            pizza = Meat(pizza)
        elif sauceChoice == 15:
            pizza = Onions(pizza)
        elif sauceChoice == 16:
            pizza = Corn(pizza)

    totalCost = pizza.get_cost()
    description = pizza.get_description()

    name = input("İsminizi giriniz: ")
    idNumber = input("TC kimlik numaranızı giriniz: ")
    creditCardNumber = input("Kredi kartı numaranızı giriniz: ")
    creditCardPassword = input("Kredi kartı şifrenizi giriniz: ")
    now = datetime.now()
    date  = now.strftime("%d-%m-%Y %H:%M:%S")

    print("Sipariş verdiğiniz için teşekkür ederiz!")
    print("İsim: " + name)
    print("TC kimlik numarası: " + idNumber)
    print("Kredi kartı numarası: " + creditCardNumber)
    print("Sipariş detay: " + description)
    print("Toplam ücret: " + str(totalCost))
    print("Tarih: " + date)

    filename = 'Orders_Database.csv'
    header = ['İsim ', 'TC kimlik numarası', 'Kredi kartı numarasi', 'Pizza açıklaması','Toplam ücret','Tarih']
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        writer.writerow([name, idNumber, creditCardNumber, description, totalCost,date])
        print("Sipariş bilgileri Orders_Database.csv'e kaydedildi.")
main()