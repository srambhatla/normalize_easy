# -*- coding: utf-8 -*-
"""
August 11, 2015
Sirisha Rambhatla
rambh002@umn.edu
"""
from numpy import array
from sklearn.preprocessing import normalize
#A=array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
#asarray(A,dtype=float)

# function called normc
def normc(Mat):
   """normalize the columns of the matrix
   B= normc(A) normalizes the columns
   the dtype of A is float"""
   
   # if statement to enforce dtype float
   B = normalize(array(Mat),norm='l2',axis=0)
   
   return B
   
   # function called normr
def normr(Mat):
   """normalize the columns of the matrix
   B= normr(A) normalizes the row
   the dtype of A is float"""
   
   # if statement to enforce dtype float
   B = normalize(array(Mat),norm='l2',axis=1)
   
   return B
   
#A=array([[1, 5, 0], [0, 2, 1], [1, 0, 2.0]])
#B=normc(A)
#norm(B[:,1])
#norm(B[1,:])