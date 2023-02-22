# def sort(array):
#     """Sort the array by using quicksort."""

#     less = []
#     equal = []
#     greater = []

#     if len(array) > 1:
#         pivot = array[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             elif x > pivot:
#                 greater.append(x)
#         # Don't forget to return something!
#         return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
#     # Note that you want equal ^^^^^ not pivot
#     else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
#         return array

# import time

# start_time = time.time()

# A = [0,1,0,2,0,3,4]
# A = A * 100000
# print(len(A))

# A = sort(A)
# print(len(A))

# import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

# print("--- %s seconds ---" % (time.time() - start_time))


# 2
# import time

# start_time = time.time()

# A = [0,1,0,2,0,3,4]
# A = A * 10000
# print(len(A))

# for i in range(0,len(A)):
#     if A[i] == 0:
#         A.append(A[i])
#         A.remove(A[i])
# # print(A)

# import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

# print("--- %s seconds ---" % (time.time() - start_time))


# 3
import time

start_time = time.time()

A = [0,1,0,2,0,3,4]
A = A * 10000
print(len(A))

for i in range(0,len(A)):
    if A[i] == 0:
        A.append(A.pop(i))
# print(A)

import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

print("--- %s seconds ---" % (time.time() - start_time))