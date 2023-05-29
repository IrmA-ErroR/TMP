import random

class Package:
    def __init__(self, origin_country, destination_country, weight, cost):
        self.origin_country = origin_country
        self.destination_country = destination_country
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"Посылка: Из {self.origin_country} в {self.destination_country}, Вес: {self.weight} кг, Стоимость: {self.cost} $"

class TempDatabase:
    def __init__(self):
        self.packages = []

    def add_package(self, package):
        self.packages.append(package)

    def send_packages(self, main_database):
        print("Отправка посылок в основную базу данных:")
        for index, package in enumerate(self.packages, start=1):
            main_database.add_package(package)
            print(f"{index}. {package}")
        print("Посылки успешно отправлены.")
        self.packages = []

class PackageGroup:
    def __init__(self, origin_country):
        self.origin_country = origin_country
        self.packages = []
        self.total_weight = 0

    def add_package(self, package):
        self.packages.append(package)
        self.total_weight += package.weight

    def display(self, group_number):
        print(f"Группа {group_number}:")
        print(f"Страна отправления: {self.origin_country}")
        print(f"Общий вес: {self.total_weight} кг")
        print(f"Посылки:")
        for package in self.packages:
            print(package)
        print()

class MainDatabase:
    def __init__(self):
        self.packages = []
        self.package_groups = {}
        self.group_counter = 1

    def add_package(self, package):
        self.packages.append(package)

        origin_country = package.origin_country
        if origin_country in self.package_groups:
            self.package_groups[origin_country].add_package(package)
        else:
            group = PackageGroup(origin_country)
            group.add_package(package)
            self.package_groups[origin_country] = group

    def display_package_groups(self):
        print("Группы посылок:")
        for group_number, group in enumerate(self.package_groups.values(), start=1):
            group.display(group_number)
            print()

class Mail:
    def __init__(self):
        self.temporary_database = TempDatabase()
        self.main_database = MainDatabase()
        self.countries = ["США", "Великобритания", "Германия", "Франция", "Япония", "Австралия", "Канада", "Бразилия", "Китай", "Индия"]

    def generate_packages(self, num_packages):
        for _ in range(num_packages):
            origin_country = random.choice(self.countries)
            destination_country = random.choice([country for country in self.countries if country != origin_country])
            weight = random.randint(1, 10)
            cost = random.randint(10, 100)
            package = Package(origin_country, destination_country, weight, cost)
            self.temporary_database.add_package(package)
        
        if len(self.temporary_database.packages) >= 10:
            self.temporary_database.send_packages(self.main_database)
            self.main_database.display_package_groups()


mail = Mail()
mail.generate_packages(11)

# # Вывод:
# Отправка посылок в основную базу данных:
# 1. Посылка: Из Китай в Япония, Вес: 9 кг, Стоимость: 55 $
# 2. Посылка: Из Индия в США, Вес: 9 кг, Стоимость: 13 $
# 3. Посылка: Из Бразилия в Китай, Вес: 8 кг, Стоимость: 61 $
# 4. Посылка: Из США в Бразилия, Вес: 5 кг, Стоимость: 86 $
# 5. Посылка: Из Бразилия в Франция, Вес: 1 кг, Стоимость: 63 $
# 6. Посылка: Из Китай в Великобритания, Вес: 8 кг, Стоимость: 47 $
# 7. Посылка: Из Канада в Франция, Вес: 2 кг, Стоимость: 27 $
# 8. Посылка: Из Индия в Франция, Вес: 4 кг, Стоимость: 80 $
# 9. Посылка: Из Великобритания в Китай, Вес: 2 кг, Стоимость: 86 $
# 10. Посылка: Из США в Канада, Вес: 9 кг, Стоимость: 76 $
# 11. Посылка: Из Великобритания в Китай, Вес: 8 кг, Стоимость: 67 $
# Посылки успешно отправлены.

# Группы посылок:
# Группа 1:
# Страна отправления: Китай
# Общий вес: 17 кг
# Посылки:
# Посылка: Из Китай в Япония, Вес: 9 кг, Стоимость: 55 $
# Посылка: Из Китай в Великобритания, Вес: 8 кг, Стоимость: 47 $


# Группа 2:
# Страна отправления: Индия
# Общий вес: 13 кг
# Посылки:
# Посылка: Из Индия в США, Вес: 9 кг, Стоимость: 13 $
# Посылка: Из Индия в Франция, Вес: 4 кг, Стоимость: 80 $


# Группа 3:
# Страна отправления: Бразилия
# Общий вес: 9 кг
# Посылки:
# Посылка: Из Бразилия в Китай, Вес: 8 кг, Стоимость: 61 $
# Посылка: Из Бразилия в Франция, Вес: 1 кг, Стоимость: 63 $


# Группа 4:
# Страна отправления: США
# Общий вес: 14 кг
# Посылки:
# Посылка: Из США в Бразилия, Вес: 5 кг, Стоимость: 86 $
# Посылка: Из США в Канада, Вес: 9 кг, Стоимость: 76 $


# Группа 5:
# Страна отправления: Канада
# Общий вес: 2 кг
# Посылки:
# Посылка: Из Канада в Франция, Вес: 2 кг, Стоимость: 27 $


# Группа 6:
# Страна отправления: Великобритания
# Общий вес: 10 кг
# Посылки:
# Посылка: Из Великобритания в Китай, Вес: 2 кг, Стоимость: 86 $
# Посылка: Из Великобритания в Китай, Вес: 8 кг, Стоимость: 67 $