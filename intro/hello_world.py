# import math

# # this is my attempt at quick sort

# def quick_sort (array):
#     if len(array) <= 1:
#         return array
    
#     first_element = array.pop(0)
#     less_than = []
#     greater_than = []
    
#     for num in array:
#         if num <= first_element:
#             less_than.append(num)
#         else:
#             greater_than.append(num)
    
#     return quick_sort(less_than) + [first_element] + quick_sort(greater_than)

# print(quick_sort([9,8,7,5,5,4,1,22,32,63,626,26,262,7,9]))

# # this is my attempt at merge sort

# # def merge_sort (array):
# #     if len(array) <= 1:
# #         return array
    
# #     midpoint = math.floor(len(array) / 2)
# #     left = merge_sort(array[0:midpoint])
# #     right = merge_sort(array[midpoint:len(array)])
    
# #     return merge(left, right)
    
# # def merge(left, right):
# #     merged = []
    
# #     while left and right:
# #         if left[0] <= right[0]:
# #             merged.append(left.pop(0))
# #         else:
# #             merged.append(right.pop(0))
    
# #     return merged + left + right

# # print(merge_sort([9,8,7,5,5,4,1,22,32,63,626,26,262,7,9]))

# # this is my attempt at a bubble sort method

# def bubble_sort(array):
#     sorted = False
    
#     while sorted == False:
#         sorted = True
        
#         for i in range(len(array) - 1):
#             if array[i] > array[i + 1]:
#                 sorted = False
#                 array[i], array[i + 1] = array[i + 1], array[i]
    
#     return array

# print(bubble_sort([9,8,7,5,5,4,1,22,32,63,626,26,262,7,9]))

# def merge_sort(array):
#     if len(array) <= 1: return array
    
#     midpoint = math.floor(len(array) / 2)
    
#     left = merge_sort(array[0:midpoint])
#     right = merge_sort(array[midpoint:len(array)])
    
#     return merge(left, right)

# def merge(left_array, right_array):
#     merged = []
    
#     while left_array and right_array:
#         if left_array[0] <= right_array[0]:
#             merged.append(left_array.pop(0))
#         else:
#             merged.append(right_array.pop(0))
        
#     return merged + left_array + right_array
    
# print(merge_sort([9,8,7,5,5,4,1,22,32,63,626,26,262,7,9]))