# -*- coding: utf-8 -*-
import numpy as np
from numpy.linalg import norm
from numpy.random import rand
from sklearn.preprocessing import normalize

__author__ = {'Sirisha Rambhatla': 'rambh002@umn.edu'}


def normc(Mat):
    """Normalize the columns of the matrix so the L2 norm of each column is 1.

    >>> A = rand(4, 4)
    >>> B = normc(A)
    >>> np.allclose(norm(B[:, 0]), 1)
    True
    """
    Mat = clean_and_check(Mat)

    B = normalize(Mat, norm='l2', axis=0)
    return B


def normr(Mat):
    """Normalize the rows of the matrix so the L2 norm of each row is 1.

    >>> A = rand(4, 4)
    >>> B = normr(A)
    >>> np.allclose(norm(B[0, :]), 1)
    True
    """
    Mat = clean_and_check(Mat, nshape=2)

    B = normalize(Mat, norm='l2', axis=1)
    return B


def normv(Vec):
    """Normalizes vectors so their L2 norm is 1.

    >>> x = rand(5)
    >>> y = normv(x)
    >>> np.allclose(norm(y), 1)
    True
    """
    Vec = clean_and_check(Vec, nshape=1)

    B = normalize(Vec, norm='l2')
    return B


def clean_and_check(x, nshape=2):
    """Make sure x is ready for computation; make it a dtype float and ensure it
    has the right shape
    """
    assert len(x.shape) == nshape, 'This input array must be a {X}-D \
    array'.format(X=nshape)

    if x.dtype != np.float:
        x = asarray(x, dtype=float)
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
