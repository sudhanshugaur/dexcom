# Pytest

The pytest framework makes it easy to write small, readable tests. For more please read : https://docs.pytest.org/en/7.2.x/ 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytest.

```bash
pip install pytest
```

## Usage

```
1. git clone https://github.com/sudhanshugaur/dexcom
2. cd dexcom/test_api
3. pytest test_sample.py

OR
1. git clone https://github.com/sudhanshugaur/dexcom
2. Using Pycharm, open the project and run it.
```
## Answer to Requirement#4
Yes, the endpoint /info does support the XML as its shown in the request header.
```
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
```
## Error Handling
I have written a afterhook in the confttest.py file which dumps all the failures in the file names failure.txt.
More option could have been explored via logger or pytest-expect python package 



