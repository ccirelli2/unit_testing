'''
Ref:
- Serious Python_ Black-Belt Advice on Deployment, Scalability, Testing, and More
- https://docs.pytest.org/en/6.2.x/contents.html

Unit Testing Hierarchy
- Store tests inside test modules that mirror your module structure.
- This means that the tests for mylib/foobar.py should be stored in
  tests/test_foobar.py.

Pytests:
- installed with pip.
- provides the pytests command which will load every file that starts with
    test_ and then execute all functions within.
- terminal command:  use pytest -v
    the -v flag tells pytest to be verbose and print each test on a new line.


'''





