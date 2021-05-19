# import the library
import numpy as np
[thing for index,thing in enumerate(10)]

arr = np.array([1])
print(arr)
print(type(arr))

arr = np.array([])
print(arr)
print(type(arr))

arr = np.array([])
np.append(arr,2)
print(arr)  # Still Blank

arr = np.array([])
arr = np.append(arr,2)
print(arr)

arr = np.array([])
arr = np.append(arr,2)
print(arr)
print(arr.dtype)
print(arr.size)

numbers = range(1,11)
arr = np.array(numbers)
print(arr)
print(arr.dtype)
print(arr.size)

arr = np.array([1/x for x in range(1,11)])
print(arr)
print(arr.dtype)
print(arr.size)

arr = np.arange(10)
print(arr)

arr = np.arange(1,11)
print(arr)

arr = np.arange(1,11,2)
print(arr)

arr = np.arange(1,11,2)
print(arr)
print(arr[1])

arr = np.array([x for x in range(10,41) if x % 2 == 0 and not x % 5 == 0])
print(arr)

x = np.int_(1.0)
print(x,type(x))
print('='*32)
arr = np.array([2,3], dtype=np.int8)
print(arr)
print(arr.dtype)

x = np.int_(1.0)
print(x,type(x))
print('='*32)

x = np.float32(range(30,50,3))
print(x,type(x))
print('='*32)

x = np.array([1, 2, 3], dtype='f')
print(x)
print(type(x))

x = np.arange(11,40,5)
print(type(x))
print(x.dtype)
x = x.astype(np.int16)
print(x.dtype)

We can add up the values in a numpy array<br>
<code>
x = np.arange(11,40,5)
print(np.sum(x))  # DO NOT TYPE x.sum()

x = [10, 5, 9, 22, -7, 3]
arr = np.array(x, dtype=np.int32)
print(arr)   
print(np.sort(arr)) # Sort the values

x = np.array([2,2,3,4], dtype=np.int32)
y = np.prod(x)      # multiply each value by itself
print(y)

x = [10, 5, 9, 22, -7, 3]
print(np.max(x))    # Get the max value

x = [10, 5, 9, 22, -7, 3]
print(np.mean(x))   # Get the mean

x = [10, 5, 9, 22, -7, 3]
print(np.min(x))    # Get the mean
</code>  

x = np.arange(11,40,5)
print(np.sum(x))  # DO NOT TYPE x.sum()

x = [10, 5, 9, 22, -7, 3]
arr = np.array(x, dtype=np.int32)
print(arr)   
print(np.sort(arr)) # Sort the values

x = np.array([2,2,3,4], dtype=np.int32)
y = np.prod(x)      # multiply each value by itself
print(y)

x = [10, 5, 9, 22, -7, 3]
print(np.max(x))    # Get the max value

x = [10, 5, 9, 22, -7, 3]
print(np.mean(x))   # Get the mean

x = [10, 5, 9, 22, -7, 3]
print(np.min(x))    # Get the mean

x = [10, 5, 9, 22, -7, 3]
x = np.array(x, dtype=np.int16)
for i in x:
    print(i, type(i))

x = [10, 5, 9, 22, -7, 3]
x = np.array(x, dtype=np.int16)
x[0] = x[0] * 2
print(x)

x = [10, 5, 9, 22, -7, 3]
x = np.array(x) * 2
print(x)

import numpy as np
grades = [65.0, 78.0, 77.0, 82.0, 97.0, 87.0, 83.0, 67.0, 83.0, 67.0, 77.0, 79.0, 
 79.0, 68.0, 69.0, 89.0, 79.0, 66.0, 85.0, 93.0, 74.0, 70.0, 83.0, 90.0]
x = np.array(grades)
x_plus = np.array(grades)+5
print(x)
print(np.mean(x))
print(x_plus)
print(np.mean(x_plus))





