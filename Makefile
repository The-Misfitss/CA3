install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	flake8 functions.py test.py  # Specify the Python files to lint here

test:
	pytest -vv --cov=functions test.py