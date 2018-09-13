lint:
	-pylint sample/*
	-pylint tests/*

test:
	-python3 -m unittest discover