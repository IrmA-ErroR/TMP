class SortingAlgorithm:
    def sort(self, array):
        raise NotImplementedError("sort() must be implemented by subclass.")

    def compare(self, a, b):
        return a < b

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


class QuickSort(SortingAlgorithm):
    def sort(self, array):
        self.quick_sort_helper(array, 0, len(array) - 1)

    def quick_sort_helper(self, array, low, high):
        if low < high:
            pivot_index = self.partition(array, low, high)
            self.quick_sort_helper(array, low, pivot_index - 1)
            self.quick_sort_helper(array, pivot_index + 1, high)

    def partition(self, array, low, high):
        pivot_value = array[high]
        i = low - 1
        for j in range(low, high):
            if self.compare(array[j], pivot_value):
                i += 1
                self.swap(array, i, j)
        self.swap(array, i + 1, high)
        return i + 1


class MergeSort(SortingAlgorithm):
    def sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.sort(left_half)
            self.sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if self.compare(left_half[i], right_half[j]):
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1


# Создаем экземпляры классов
qs = QuickSort()
ms = MergeSort()

# Подготавливаем список для сортировки
numbers = [6, 2, 4, 8, 1, 3, 9, 5, 7]

# Сортировка с помощью QuickSort
qs.sort(numbers)
print(numbers)

# Сортировка с помощью MergeSort 
ms.sort(numbers)
print(numbers)  