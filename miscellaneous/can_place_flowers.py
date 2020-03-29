"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:

    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.


Python O( n ) sol. based on check-and-plant.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        
        size = len(flowerbed)
        
        if n == 0:
            # n = 0, no need to plant
            return True
        

            
        index = 0        
        count_of_plant = 0
        
        while index < size:
            
            if count_of_plant == n:
                # n flowers are planted already
                break
            
            if flowerbed[index] :
                # skip to next possible space
                index += 2
                continue
        
            elif index == size-1 or flowerbed[index+1] == 0:
                # plant one flower at index
                flowerbed[index] = 1
                
                # go to next possible space
                index += 2
                count_of_plant += 1
            
            else:
                # go to next space
                index += 1
        
        
        return count_of_plant == n
