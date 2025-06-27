class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Função de merge modificado para contar pares reversos
        def merge_count_split_inv(left, right):
            i, j = 0, 0
            count = 0
            merged = []
            
            # Conta inversões (pares reversos) enquanto mescla
            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    count += len(left) - i  # Todos os elementos à direita de i formam pares com j
                    j += 1
                else:
                    i += 1
            
            # Mescla os arrays left e right
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            # Adiciona os elementos restantes
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged, count

        # Função de merge sort modificado
        def merge_sort_and_count(nums):
            if len(nums) < 2:
                return nums, 0
            mid = len(nums) // 2
            left, left_count = merge_sort_and_count(nums[:mid])
            right, right_count = merge_sort_and_count(nums[mid:])
            merged, split_count = merge_count_split_inv(left, right)
            return merged, left_count + right_count + split_count

        _, total_count = merge_sort_and_count(nums)
        return total_count
