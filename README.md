## normalize_easy Package

This package implements `normc()`, `normr()`, `normv()` functions to easily normalize columns, rows of 2-D arrays and vectors respectively. 
This package uses `sklearn.preprocessing.normalize` and forced the input array to have dtype as float. The input array has to be 2-D for `normc()` and `normr()`. 


* `normc()` -> normalizes columns of a 2-D array
* `normr()` -> normalizes rows of a 2-D array
* `normv()` -> normalizes the 1-D array


### To install
* `pip install normalize_easy`, or
* Download the repo and run `python setup.py install`




