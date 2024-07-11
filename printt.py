def dois_indices(nums, alvo):
    dicionario = {}
    for i, num in enumerate(nums):
        diferenca = alvo - num
        if diferenca in dicionario:
            return [dicionario[diferenca], i]
        dicionario[num] = i

nums1 = [2, 7, 11, 15]
alvo1 = 9
print(dois_indices(nums1, alvo1)) 

nums2 = [3, 2, 4]
alvo2 = 6
print(dois_indices(nums2, alvo2))  

nums3 = [3, 3]
alvo3 = 6
print(dois_indices(nums3, alvo3))  







