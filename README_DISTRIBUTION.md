
### Steps
1. Create a `setup.py` file (find examples online)
2. Create a `__init__.py` file `from .normalize_easy import normr, normc`
3. Update the README file
4.  Follow the structure :

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

5. at root dir run the following
    a. `python setup.py sdist`
    b. `python setup.py bdist_wheel --universal`
    c. `python setup.py install`
6. Then check via ipython  by importing the package
7. If first version go to pipy and add a new package using PKG-INFO file look around in the directories. 
8. twine upload dist/* If first version else put the apt who file name after /
    a. aka `twine upload dist/<package-name><version number>*`