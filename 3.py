class Solution:
    """
    Временная сложность: O(n logn)
    Пространственная сложность: O(n)

    Преимущества:
    - Эффективен для больших массивов.
    - Стабильность сортировки.

    Недостатки:
    - Дополнительная память.
    - Медленнее на маленьких массивах.
    """

    def merge_sort(self, lst) -> list:
        if len(lst) > 1:
            mid = len(lst) // 2
            L = lst[:mid]
            R = lst[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i += 1
                else:
                    lst[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                lst[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                lst[k] = R[j]
                j += 1
                k += 1

        return lst


class Solution:
    """
    Временная сложность: O(n^2)
    Пространственная сложность: O(1)

    Преимущества:
    - Простота реализации.
    - Эффективен на небольших массивах.

    Недостатки:
    - Низкая эффективность на больших массивах.
    """

    def insertion_sort(self, lst: List[int]) -> None:
        for i in range(1, len(lst)):
            current_index = i

            while current_index > 0 and lst[current_index - 1] > lst[current_index]:
                lst[current_index], lst[current_index - 1] = (
                    lst[current_index - 1],
                    lst[current_index],
                )
                current_index -= 1


class Solution:
    """
    Временная сложность: O(N + K)
    Пространственная сложность: O(N + K)
    K - максимальное занчение в массиве

    Преимущества:
    - Стабильность сортировки.
    - Эффективен на небольших массивах с малым разбросом данных.

    Недостатки:
    - Низкая эффективность на массивах с большим K.
    """

    def counting_sort(self, lst) -> None:
        shift = min(lst)
        K = max(lst) - shift
        counts = [0] * (K + 1)
        for elem in lst:
            counts[elem - shift] += 1

        start_ind = 0
        for i, count in enumerate(counts):
            counts[i] = start_ind
            start_ind += count

        sorted_lst = [0] * len(lst)
        for elem in lst:
            sorted_lst[count[elem - shift]] = elem
            counts[elem - shift] += 1

        return sorted_lst
