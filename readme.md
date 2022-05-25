# Prerequisites

Git, Terminal (e.g. cmder),
Python 3.10+,
PyCharm,
Up-to-date Firefox browsers (update the browser before running tests).

# Windows


Open command console in repository folder


Run command in terminal to install virtual environment
venv-install.bat


Run command in terminal to install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt


Open project in PyCharm
- Open command console in repository folder
- Run command in terminal to install virtual environment

	 venv-install.bat

- Run command in terminal to install requirements

     python -m pip install --upgrade pip
	 pip install -r requirements.txt

- Open project in PyCharm

# MacOS

- Open command terminal

- Run command in terminal to install virtual environment

	 python -m venv venv
	 source venv/bin/activate
	 pip install -r requirements.txt


# Start tests


- Open cmd terminal in repository folder

- Run command in terminal to start tests

     python -m pytest
