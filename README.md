# Example Package
Packaging on Windows10

## 安裝虛擬環境virtualenv
pycharm可以做類似的事
>pip install virtualenv

## 進入虛擬環境
>virtual env packaging

>cd packaging

## 進行版本控制
>git init

## 安裝相關套件
>python -m pip install setuptools wheel twine
## 升級最新套件 (optional)
>python3 -m pip install --user --upgrade setuptools wheel

## 確認__INIT__.py、setup.py、README.md、LICENSE和模組都ready後
under packaging/
>python3 setup.py sdist bdist_wheel

## 生成dist/
source code archive
>packaging-example-0.0.1.tar.gz 
build distribution
>packaging_example-0.0.1-py3-none-any.whl 

## upload to TestPyPI
>python3 -m pip install --user --upgrade twine
>python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
## pip install your package
>python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username
## test installed or not?
>python
>import example_pkg
>example_pkg.name
'example_pkg'
## Python Package Index
>Note: Test PyPI isn't permanent and trasfer to use https://pypi.org to upload to the real Python Package Index

[Reference](https://packaging.python.org/tutorials/packaging-projects/)
