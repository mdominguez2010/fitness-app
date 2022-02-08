install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-azure:
	pip install --upgrade pip &&\
		pip install -r requirements-azure.txt

format:
	black *.py
	
lint:
	python -m pylint --load-plugins pylint_flash_sqlalchemy main.py
	
test:
	python -m pytest -vv --cov=main test_main.py
	
all: install format lint test