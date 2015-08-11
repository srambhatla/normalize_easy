# -*- coding: utf-8 -*-
"""
August 11, 2015
Sirisha Rambhatla
rambh002@umn.edu
"""
from numpy import asarray
from pylab import rand, norm, allclose
from sklearn.preprocessing import normalize

# function called normc
def normc(Mat):
   """Normalize the columns of the matrix 

    >>> A = rand(4, 4)
    >>> B = normc(A)
    >>> allclose(norm(B[:, 0]), 1)
    True"""
   
   # Assert 2-D Array
   assert len(Mat.shape)==2 , 'The input array should be a 2-D array'
   
   # Enforce dtype float
   if Mat.dtype != 'float': Mat = asarray(Mat,dtype=float)
   
   # Normalize 
   B = normalize(Mat,norm='l2',axis=0)
   
   return B
   
   # function called normr
def normr(Mat):
   """Normalize the columns of the matrix
    
    >>> A = rand(4, 4)
    >>> B = normr(A)
    >>> allclose(norm(B[0, :]), 1)
    True
    """
   
   # Assert 2-D Array
   assert len(Mat.shape)==2 , 'The input array should be a 2-D array'
   
     # Enforce dtype float
   if Mat.dtype != 'float': Mat = asarray(Mat,dtype=float)
       
   # if statement to enforce dtype float
   B = normalize(Mat,norm='l2',axis=1)
   
   return B
   
def normv(Vec):
    """Normalizes vectors
    
    >>> x = rand(5)
    >>> y = normv(x)
    >>> allclose(norm(y), 1)
    True
    """
    
    # Assert 2-D Array
    assert len(Vec.shape)==1 , 'The input array should be a 1-D array'
   
    # Enforce dtype float
    if Vec.dtype != 'float': Vec = asarray(Vec,dtype=float)
      
    # if statement to enforce dtype float
    B = normalize(Vec,norm='l2')
   
    return B
     
# For doctests   
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)