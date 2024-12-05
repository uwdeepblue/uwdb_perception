# Denoising technique research

This is intended to act as a testing environment to support ongoing research for the UWDB perception software. Currently developing for this branch using WSL (should work on Windows too) and Python, so instructions will reflect this. What language we actually end up using is (I think?) up for debate, but for ease of use I'll be using Python for research. Focus here is on implementing and comparing different techniques for denoising, allowing us to make accurate classifications of underwater objects. The actual amount of denoising necessary will depend on the camera in use, but this will be a good environment to determine how we want to process our images before classification.

## Setup Instructions.

- Ensure Python is installed. You can use `sudo apt install python3 python3-pip python3-venv` to install python, pip, and venv
- Create a new venv with `python3 -m venv myenv` and activate it with `source myenv/bin/activate` (you can replace myenv with the name of your choice). For Windows, use `./myenv/bin/Activate.ps1`.
- Install the necessary packages and dependencies with `pip install -r requirements.txt`
- Make sure not to commit the virtual environment, as it will end up being a lot of files and is easier for each user to maintain their own.
- Run scripts with Python!