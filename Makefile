
install:
	python -m venv .env
	pip install --upgrade pip &&\
	pip install -r requirements.txt\
	
lint:
	pylint --disable=R,C,W1203,W1202 **.py

test:
	python -m pytest test_hello.py
