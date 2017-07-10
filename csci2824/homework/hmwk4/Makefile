all: Problem2.cpp Problem3.cpp
	g++ Problem2.cpp -o Problem2
	g++ Problem3.cpp -o Problem3

run: Problem1.py Problem2 Problem3 Problem4.py Problem5.py
	@echo "Running Problem 1"
	python Problem1.py
	@echo "\nRunning Problem 2"
	./Problem2
	@echo "\nRunning Problem 3"
	./Problem3
	@echo "\nRunning Problem 4"
	python Problem4.py
	@echo "\nRunning Problem 5"
	python Problem5.py

