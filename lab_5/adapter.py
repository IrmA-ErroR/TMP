# Класс Генератор 
class Generator:
    def generate_digits(self, length):
        digits = []
        for i in range(length):
            digits.append(i % 10) 
        return digits

# Класс Адаптер
class Adapter:
    def __init__(self, digits):
        self.digits = digits
        self.number_words = {
            0: "ноль",
            1: "один",
            2: "два",
            3: "три",
            4: "четыре",
            5: "пять",
            6: "шесть",
            7: "семь",
            8: "восемь",
            9: "девять"
        }

    def convert_to_words(self):
        words = []
        for digit in self.digits:
            if digit in self.number_words:
                words.append(self.number_words[digit])
        return words

# Класс Сервис 
class Service:
    def count_letters(self, words):
        letter_count = []
        for word in words:
            letter_count.append(len(word))
        return letter_count

generator = Generator()
digits = generator.generate_digits(10)
print("Сгенерированные цифры:", digits)

adapter = Adapter(digits)
words = adapter.convert_to_words()
print("Прописные числа:", words)

service = Service()
letter_count = service.count_letters(words)
print("Количество букв в каждом слове:", letter_count)

# Вывод:
# # Сгенерированные цифры: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # Прописные числа: ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
# # Количество букв в каждом слове: [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]