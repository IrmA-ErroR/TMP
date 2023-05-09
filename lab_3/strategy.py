from abc import ABCMeta, abstractmethod
import random

class Strategy(ABCMeta):
    @abstractmethod
    def do(self, arr):
        pass

class Strategy1(Strategy):
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = random.choice(arr)
            less = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            greater = [x for x in arr if x > pivot]
            
            return self.quick_sort(less) + equal + self.quick_sort(greater)
        
    def do(self, arr):
        sorted_arr = self.quick_sort(arr)
        print(sorted_arr)


class Strategy2(Strategy):
    def do(self, arr):
        nums = arr
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                # Меняем элементы
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                    swapped = True
        return nums
        

class Context:
    
    def __init__(self) -> None:        
        self.strategy = None
        
    
    def set_strategy(Strategy) -> None:
        self.strategy = Strategy
        
    def make_sorting(arr) -> list[int]:
        return self.strategy.do(arr)


arr = [2, 5, 6, 8, 1, 3, 7, 4, 9, 0]

context = Context()

# Выбираем стратерию  Quick Sort 
context.set_strategy(Strategy1())

# Выполняем сортировку
context.make_sorting(arr)