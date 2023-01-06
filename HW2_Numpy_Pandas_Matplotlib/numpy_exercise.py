import numpy
import math

# #b
# print(numpy.array([[1,2], [3,4]]))  
# #c
# print(numpy.diag([1] * 10))  
# #d
# print(numpy.random.random((5,3)))  
# #e
# print(numpy.ones((5,3,10), dtype=int))
# dataForF = numpy.arange(1,16).reshape(3,5)
# print(dataForF)
# print(dataForF[0:3, 0:2])
# print(dataForF[:, 1])
# print(dataForF[2,2:])

##Rotational Matrix
# def rotate(vec):
#     angle = math.radians(45)
#     return vec.dot(numpy.array([[math.cos(angle), -math.sin(angle)],\
#                                 [math.sin(angle), math.cos(angle)]]))
# vector = numpy.array([1/math.sqrt(2), 1/math.sqrt(2)])
# rotated_vec = rotate(vector)
# print(rotated_vec)

##Eigen Value
matrix = numpy.array([[2,1],[0,2]])
print(numpy.linalg.eigvals(matrix))