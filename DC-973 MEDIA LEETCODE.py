import random

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Função para calcular a distância ao quadrado de um ponto até a origem
        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        # Função de partição usada no algoritmo Quickselect
        def partition(left, right):
            pivot = random.randint(left, right)
            points[pivot], points[right] = points[right], points[pivot]
            pivot_distance = distance(points[right])
            i = left
            for j in range(left, right):
                if distance(points[j]) < pivot_distance:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i
        
        # Quickselect
        def quickselect(left, right):
            if left <= right:
                pivot_index = partition(left, right)
                if pivot_index == k:
                    return
                elif pivot_index < k:
                    quickselect(pivot_index + 1, right)
                else:
                    quickselect(left, pivot_index - 1)

        # Chama a função quickselect para encontrar os k pontos mais próximos
        quickselect(0, len(points) - 1)
        
        # Retorna os k primeiros pontos
        return points[:k]
