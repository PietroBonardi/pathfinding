run: 
	python3 main.py
	
local: 
	pip3 install -e ./src
	pip3 install -r requirements.txt

test:
	pytest --cov=src/pathfinder/data_structure