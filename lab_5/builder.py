# Product: Coffee
class Coffee:
    def __init__(self):
        self.grinded_beans = None
        self.heated_cup = None
        self.espresso = None
        self.milk_foam = None
        self.cinnamon = None

    def set_grinded_beans(self, grinded_beans):
        self.grinded_beans = grinded_beans

    def set_heated_cup(self, heated_cup):
        self.heated_cup = heated_cup

    def set_espresso(self, espresso):
        self.espresso = espresso

    def set_milk_foam(self, milk_foam):
        self.milk_foam = milk_foam

    def display(self):
        print("Ваш капучино готов!")

# Builder
class CoffeeBuilder:
    def __init__(self):
        self.coffee = Coffee()

    def grind_beans(self):
        self.coffee.set_grinded_beans("Перемалывание зерен")
        print("Перемалывание зерен")

    def heat_cup(self):
        self.coffee.set_heated_cup("Подогрев чашки до 40 градусов")
        print("Подогрев чашки до 40 градусов")

    def brew_espresso(self):
        self.coffee.set_espresso("Приготовление эспрессо")
        print("Приготовление эспрессо")

    def froth_milk(self):
        self.coffee.set_milk_foam("Взбивание молока")
        print("Взбивание молока")

    def get_coffee(self):
        return self.coffee

# Builder: Alena
class Alena(CoffeeBuilder):
    def add_cinnamon(self):
        self.coffee.cinnamon = "Добавление корицы"
        print("Добавление корицы")

# Builder: Maxim
class Maxim(CoffeeBuilder):
    def froth_milk(self):
        self.coffee.set_milk_foam("Взбивание КОКОСОВОГО молока")
        print("Взбивание КОКОСОВОГО молока")

# Director
class CoffeeDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def prepare_coffee(self):
        self.builder.grind_beans()
        self.builder.heat_cup()
        self.builder.brew_espresso()

        if isinstance(self.builder, Alena):
            self.builder.add_cinnamon()
        self.builder.froth_milk()

        return self.builder.get_coffee()


director = CoffeeDirector()

builder_name = input("Введите имя баристы (Alena или Maxim): ")

if builder_name == "Alena":
    builder = Alena()
elif builder_name == "Maxim":
    builder = Maxim()
else:
    builder = CoffeeBuilder()

director.set_builder(builder)
coffee = director.prepare_coffee()
coffee.display()

# Вывод: 
# # Введите имя баристы (Alena или Maxim): Alena
# # Перемалывание зерен
# # Подогрев чашки до 40 градусов
# # Приготовление эспрессо
# # Добавление корицы
# # Взбивание молока
# # Ваш капучино готов!