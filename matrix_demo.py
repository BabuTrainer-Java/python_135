import numpy as  n1
zero_matrix=n1.array(30)
print("Zero::",zero_matrix.ndim ,":::",type(zero_matrix))
one_d=n1.array([1,3,4,5,6])
print("one_D:",one_d.ndim ,":::",type(one_d))
two_d=n1.array([[1,2,3],[4,5,6]])
print("Two_D::",two_d.ndim ,":::",type(two_d))
thr_d=n1.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("Thr_d::",thr_d.ndim ,":::",type(thr_d))
higher_d=n1.array([1,2,3],ndmin=10)
print("higher_d::",higher_d.ndim ,":::",type(higher_d),":::",higher_d)







