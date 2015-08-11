# -*- coding: utf-8 -*-
"""
August 11, 2015
Sirisha Rambhatla
rambh002@umn.edu
"""
from numpy import asarray
from sklearn.preprocessing import normalize

# function called normc
def normc(Mat):
   """normalize the columns of the matrix
   B= normc(A) normalizes the columns
   the dtype of A is float"""
   
   # Enforce dtype float
   if Mat.dtype!='float':
      Mat = asarray(Mat,dtype=float)
    
   B = normalize(Mat,norm='l2',axis=0)
   
   return B
   
   # function called normr
def normr(Mat):
   """normalize the columns of the matrix
   B= normr(A) normalizes the row
   the dtype of A is float"""
   
     # Enforce dtype float
   if Mat.dtype!='float':
      Mat = asarray(Mat,dtype=float)
      
   # if statement to enforce dtype float
   B = normalize(Mat,norm='l2',axis=1)
   
   return B
 
# For doctests   
#A=array([[1, 5, 0], [0, 2, 1], [1, 0, 2]])
#B=normc(A)
#norm(B[:,1])
#norm(B[1,:])
