


## brew install python3

### location of python
* /usr/local/bin/python3

## add python to the path 
* $ vi .bash_profile
```
 export PATH="/usr/local/opt/python@3.8/libexec/bin:$PATH"
```
* $ source ~/.bash_profile


## python version 
* $ python ––version

## pip version 
* $ pip --version

## to install pybuilder 
* $  pip install pybuilder

## to list the install packages 
* $ pip list

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

* $ pyb run_unit_tests