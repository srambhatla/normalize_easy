
### Steps
1. Create a `setup.py` file (find examples online)
2. Create a `__init__.py` file `from .normalize_easy import normr, normc`
3.  Follow the structure :

some_root_dir/ 
|-- README
|-- setup.py
|-- an_example_pypi_project
|   |-- __init__.py
|   |-- useful_1.py
|   |-- useful_2.py
|-- tests
|-- |-- __init__.py
|-- |-- runall.py
|-- |-- test0.py

4. at root dir run the following
    a. `python setup.py sdist`
    b. `python setup.py bdist_wheel --universal`
    c. `python setup.py install`
5. Then check via ipython  by importing the package
