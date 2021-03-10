import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# ROWS - grades for each student
# COLS - grades for each test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.min()
e = grades.std()
f = grades.var()
# print(a, b, c, d, e, f)

g = grades.mean(axis=0)  # printing by column for every row
print("Average of each test is ", g)

h = grades.mean(axis=1)
print("Average of each student is ", h)

numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)

print(sqrt)

numbers2 = np.arange(1, 7) * 10

add = np.add(numbers, numbers2)

print(add)

multiply = np.multiply(numbers2, 5)

print(multiply)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

multiply2 = np.multiply(numbers3, numbers4)

print(multiply2)

# This works because numbers4 has the same length as each row of numbers3, so NumPy can apply the multiply operation by
# treating numbers4 as if it were the following array: array([[2,4,6],[2,4,6]])

# Indexing and slicing
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

a = grades[0, 1]

print(a)
# 96

b = grades[1]

print(b)
# array([100,87,90])

# To select multiple sequential rows use slice
# notation (remeber upper limit is not included):
firsttwo = grades[0:2]

print(firsttwo)

# To select multiple non-sequential rows, use a list of row indices:
test = grades[[1, 3]]

print(test)

# All rows and only the first column:
c = grades[:, 0]
# c2 = grades[:2, 0]
print(c)
# print(c2)

# all rows and columns 0 through 2, You can select consecutive columns using a slice:
d = grades[:, 1:3]
print(d)

# Specific columns using a list of column indices:
e = grades[:, [0, 2]]
print(e)

"""
Use NumPy random-number generation to create an array of twelve random grades in the range 60 through 100, then
reshape the result into a 3by4 array. Calculate the average of all the grades, thea verages of the grades for each test
and teh averages of the grades for each student.
"""
# grades = np.arange(0, 12).reshape(3, 4)
# grades = np.array(np.random.randint(60, 100, size=(3, 4)))
# grades = np.array(np.random.randint(60,100,12))
grades = np.random.randint(60, 101, 12).reshape(3, 4)
# averagetotal = grades.sum()/12
# averagetest = grades[:,0].sum()/4
# averagestudent = grades[]

print(grades.mean())
print(grades.mean(axis=0))
print(grades.mean(axis=1))


# Shallow Copies (View) - Views and modifies the original array, both directions
# The array mthod view returns a new array object with a view of the original array

numbers = np.arange(1, 6)
# array([1,2,3,4,5])

numbers2 = numbers.view()
# array([1,2,3,4,5])

numbers[1] *= 10

print(numbers2)

numbers2[1] /= 10

print(numbers)

# Slice Views
# Slices also create views. Let's make numbers2 a slice that views only the first three elements of numbers:

numbers2 = numbers[0:3]

numbers[1] *= 20

print(numbers2)


# Deep Copies (Copy)
# The array method copy returns a new array object with a deep copy of the original array
numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10

print(numbers)
print(numbers2)

"""The array method reshape and resize both enable you to change an array's dimensions. Method reshape returns
a view (shallow copy) of the original array with the new dimensions. It does not modify the original array:"""


grades = np.array([[87, 96, 79], [100, 87, 90]])

a = grades.reshape(1, 6)
print(a)
print(grades)


b = grades.resize(1, 6)
print(grades)


# Method flatten deep copies the original array's data:

flattened = grades.flatten()

# Alternatively, Method ravel produces a view (shallow copy) of the original array, which shares the grades array's data:

raveled = grades.ravel()

raveled[0] = 100

raveled[5] = 99

# Since it is a view and the data is shared, grades's 6th element and 1st element have been changed.
print(grades)


# You can quickly transpose an array's rows and columns, that is to "flip" the array,
# so the rows become the columns and the columns become the rows.
# The T attribute returns a transposed view (shallow copy) of the array.

transposed = grades.T
print(transposed)


grades = np.array([[87, 96, 79], [100, 87, 90]])

# You can combine arrays by adding more columns or more rows = known as horizontal stacking and vertical stacking.

# HSTACK
#

grades = np.array([[87, 96, 79], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

h_grades = np.hstack((grades, grades2))

print(h_grades)

# old array not affected
print(grades)

# VSTACK

v_grades = np.vstack((grades, grades2))
print(v_grades)