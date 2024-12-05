# OpenCV Classifier Research

This is intended to act as a testing environment to support ongoing research for the UWDB perception software. Currently developing for this branch using WSL (should work on Windows too) and Python, so instructions will reflect this. What language we actually end up using is (I think?) up for debate, but for ease of use I'll be using Python for research (as much as I despise Python runtime and dependency management).

## Setup Instructions.

- Ensure Python is installed. You can use `sudo apt install python3 python3-pip python3-venv` to install python, pip, and venv
- Create a new venv with `python3 -m venv myenv` and activate it with `source myenv/bin/activate` (you can replace myenv with the name of your choice). For Windows, use `./myenv/bin/Activate.ps1`.
- Install the necessary packages and dependencies with `pip install -r requirements.txt`
- Make sure not to commit the virtual environment, as it will end up being a lot of files and is easier for each user to maintain their own.
- Run scripts with Python!

Note: Currently having trouble getting virtual environment to work with Linux and Windows, I love dependency hell. For now, use in Linux if possible, or figure out how to get dependencies working in Windows at your own risk.