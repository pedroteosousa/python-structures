lint:
	pylint strukturen tests

test:
	python3 -m unittest discover

publish:
	rm -rf dist/
	python3 setup.py sdist bdist_wheel
	twine upload dist/*