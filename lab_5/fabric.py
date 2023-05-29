from abc import ABC, abstractmethod

# Abstract Product: Candy
class Candy(ABC):
    @abstractmethod
    def create_candy(self):
        pass

# Concrete Product: ChocolateBar
class ChocolateBar(Candy):
    def create_candy(self):
        print("Creating chocolate bar...")

# Concrete Product: FerreroRocher
class FerreroRocher(Candy):
    def create_candy(self):
        print("Creating Ferrero Rocher...")

# Concrete Product: KinderSurprise
class KinderSurprise(Candy):
    def create_candy(self):
        print("Creating Kinder Surprise...")

# Concrete Product: Raffaello
class Raffaello(Candy):
    def create_candy(self):
        print("Creating Raffaello...")



# Abstract Factory: ChocolateFactory
class ChocolateFactory(ABC):
    @abstractmethod
    def create_candy(self) -> Candy:
        pass

    def pack_candy(self):
        return "Candy ready"

# Concrete Factory: WillyWonkaFactory
class WillyWonkaFactory(ChocolateFactory):
    def create_candy(self) -> Candy:
        return ChocolateBar()

# Concrete Factory: FerreroFactory
class FerreroFactory(ChocolateFactory):
    def create_candy(self) -> Candy:
        return FerreroRocher()

    def create_kinder(self) -> Candy: 
        return KinderSurprise()

    def create_raffaello(self) -> Candy: 
        return Raffaello()
    
    def create_chocolate_bar(self) -> ChocolateBar:
        return None


# Usage
ferrero_factory = FerreroFactory()

ferrero_rocher = ferrero_factory.create_candy()
ferrero_rocher.create_candy()
# Вывод: Creating Ferrero Rocher...

kinder_surprise = ferrero_factory.create_kinder()
kinder_surprise.create_candy()
# Вывод: Creating Kinder Surprise...

raffaello = ferrero_factory.create_raffaello()
raffaello.create_candy()
# Вывод: Creating Raffaello...

chocolate_bar = ferrero_factory.create_chocolate_bar()
if chocolate_bar is not None:
    chocolate_bar.create_candy()
else:
    print("Chocolate bar not available")
# Вывод: Chocolate bar not available

packaged_candy = ferrero_factory.pack_candy()
print(packaged_candy)
# Вывод: Candy ready

