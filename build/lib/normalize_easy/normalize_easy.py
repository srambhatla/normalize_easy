# -*- coding: utf-8 -*-
"""
August 11, 2015
Sirisha Rambhatla
rambh002@umn.edu
"""
import numpy as np
from pylab import rand, norm, allclose
from sklearn.preprocessing import normalize

# function called normc
def normc(Mat):
    """Normalize the columns of the matrix

     >>> A = rand(4, 4)
     >>> B = normc(A)
     >>> allclose(norm(B[:, 0]), 1)
     True"""
     Mat = clean_and_check(Mat)

     B = normalize(Mat,norm='l2',axis=0)
     return B

def normr(Mat):
    """Normalize the columns of the matrix

    >>> A = rand(4, 4)
    >>> B = normr(A)
    >>> allclose(norm(B[0, :]), 1)
    True
    """
    Mat = clean_and_check(Mat, nshape=2)

    B = normalize(Mat,norm='l2',axis=1)
    return B

def normv(Vec):
    """Normalizes vectors

    >>> x = rand(5)
    >>> y = normv(x)
    >>> allclose(norm(y), 1)
    True
    """
    clean_and_check(Vec, nshape=1)

    B = normalize(Vec,norm='l2')
    return B

def clean_and_check(x, nshape=2):
    assert len(x.shape) == nshape, 'This input array must be a {nshape}-D array'.format(nshape)
    if x.dtype != np.float: x = asarray(x, dtype=float)
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)


