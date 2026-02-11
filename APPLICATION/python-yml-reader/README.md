


```
>> pip install pipreqs
Collecting pipreqs
  Downloading pipreqs-0.4.13-py2.py3-none-any.whl.metadata (7.4 kB)
Collecting docopt (from pipreqs)
  Downloading docopt-0.6.2.tar.gz (25 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting yarg (from pipreqs)
  Downloading yarg-0.1.10-py2.py3-none-any.whl.metadata (4.5 kB)
Collecting requests (from yarg->pipreqs)
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting charset_normalizer<4,>=2 (from requests->yarg->pipreqs)
  Downloading charset_normalizer-3.4.4-cp314-cp314-win_amd64.whl.metadata (38 kB)
Collecting idna<4,>=2.5 (from requests->yarg->pipreqs)
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests->yarg->pipreqs)
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2017.4.17 (from requests->yarg->pipreqs)
  Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Downloading pipreqs-0.4.13-py2.py3-none-any.whl (33 kB)
Downloading yarg-0.1.10-py2.py3-none-any.whl (13 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.4-cp314-cp314-win_amd64.whl (107 kB)
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
Building wheels for collected packages: docopt
  Building wheel for docopt (pyproject.toml) ... done
  Created wheel for docopt: filename=docopt-0.6.2-py2.py3-none-any.whl size=13889 sha256=395f950f2d82f417d3b8ac901c204449ec57c7dcf0435040f370f9de440b31a1
  Stored in directory: c:\users\adars\appdata\local\pip\cache\wheels\79\6f\5f\26c3d1a144117ef52122d67c32b9f3c297c3dec4fea00a31ac
Successfully built docopt
Installing collected packages: docopt, urllib3, idna, charset_normalizer, certifi, requests, yarg, pipreqs
Successfully installed certifi-2026.1.4 charset_normalizer-3.4.4 docopt-0.6.2 idna-3.11 pipreqs-0.4.13 requests-2.32.5 urllib3-2.6.3 yarg-0.1.10
```

```

>> python -m pipreqs.pipreqs --encoding utf-8 ./
INFO: Successfully saved requirements file in ./requirements.txt
```

```
>> pip install PyYAML
Collecting PyYAML
  Downloading pyyaml-6.0.3-cp314-cp314-win_amd64.whl.metadata (2.4 kB)
Downloading pyyaml-6.0.3-cp314-cp314-win_amd64.whl (156 kB)
Installing collected packages: PyYAML
Successfully installed PyYAML-6.0.3
```

```
>> pip install -r .\requirements.txt
Collecting PyYAML==6.0.1 (from -r .\requirements.txt (line 2))
  Downloading PyYAML-6.0.1.tar.gz (125 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: PyYAML
  Building wheel for PyYAML (pyproject.toml) ... done
  Created wheel for PyYAML: filename=pyyaml-6.0.1-cp314-cp314-win_amd64.whl size=45186 sha256=5d9780d2eacfbba1a7cc136954c25e9858791c2b7947f42b1581fabce0e9d3fa
  Stored in directory: c:\users\adars\appdata\local\pip\cache\wheels\2d\a7\37\e5c4c5bfa292b13c7ef6f3cc55596744c49fde136b66814325
Successfully built PyYAML
Installing collected packages: PyYAML
  Attempting uninstall: PyYAML
    Found existing installation: PyYAML 6.0.3
    Uninstalling PyYAML-6.0.3:
      Successfully uninstalled PyYAML-6.0.3
Successfully installed PyYAML-6.0.1
```