lint:
	-pylint structures/*
	-pylint tests/*

test:
	-python3 -m unittest discover