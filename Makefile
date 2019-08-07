build:
	python3 setup.py bdist

clean:
	python3 setup.py clean
	rm -rf build/ dist/ blackjack.egg-info/

install:
	python3 setup.py install
	rm -rf build/ dist/ blackjack.egg-info/

status:
	pip3 show blackjack

test:
	python3 setup.py test

uninstall:
	pip3 uninstall blackjack

.PHONY: build
