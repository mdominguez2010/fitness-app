install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-azure:
	pip install --upgrade pip &&\
		pip install -r requirements-azure.txt

format:
	black *.py
	
lint:
	pylint --disable=R,C main.py
	
test:
	python -m pytest -vv --cov=hello hello_test.py
	
all: install format lint test