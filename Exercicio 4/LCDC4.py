class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Garantir que nums1 seja o menor array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Tamanho dos arrays
        m, n = len(nums1), len(nums2)
        
        # Divisão binária para encontrar a posição de corte
        low, high = 0, m
        while low <= high:
            # Posição de corte no array nums1
            partition1 = (low + high) // 2
            # Posição de corte no array nums2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Lados esquerdo e direito de cada partição
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Verificar se encontramos a partição correta
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Caso o número de elementos seja ímpar
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # Caso o número de elementos seja par
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            # Ajustar as partições
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        # Se não conseguir encontrar a partição correta
        raise ValueError("Input arrays are not sorted.")
