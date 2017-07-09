class Solution:
    def solve(self,A):
        low=0
        high=len(A)-1
        return self.quick_sort(A,low,high)
    
    def sub_sort(self,A,low,high):
        key = A[low]
        while low < high:
            while low < high and A[high] >= key:
                high -= 1
            while low < high and A[high] < key:
                A[low] = A[high]
                low += 1
                A[high] = A[low]
        A[low] = key
        return low


    def quick_sort(self,A,low,high):
        if low < high:
            key_index = self.sub_sort(A,low,high)
            self.quick_sort(A,low,key_index)
            self.quick_sort(A,key_index+1,high)
        return A
