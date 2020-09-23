### Creating PyBuilder Project
* $ mkdir python-pybuilder-app
* $ cd python-pybuilder-app/
* $ pyb --start-project
```
Project name (default: 'python-pybuilder-app') : 
Source directory (default: 'src/main/python') : 
Docs directory (default: 'docs') : 
Unittest directory (default: 'src/unittest/python') : 
Scripts directory (default: 'src/main/scripts') : 
Use plugin python.flake8 (Y/n)? (default: 'y') : y
Use plugin python.coverage (Y/n)? (default: 'y') : y
Use plugin python.distutils (Y/n)? (default: 'y') : y

Created 'setup.py'.

Created 'pyproject.toml'.
```

## Create a python class or file in 
* proj/src/main/python/main.py
```
print("welcome to espark")
```

## To build the code or rebuild 
* $ pyb

## to execute 
*  python ./src/main/python/main.py


## to run test case 
* $  pyb run_unit_tests