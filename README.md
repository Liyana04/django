This is a simple example for python and django using sqlite3 as database

-Possible error for futture reference
when error no modules name ‘pandas’or anything not found, need to run ‘pip install pandas’ in vscode
jupyter short-cut, ‘a’ to create new sell above, ‘b’ to create new cell below, double click ‘d’ will delete the cell, shift + tab to show tooltip,
if run pip then stumble open this error
pip : The term 'pip' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again. At line:1 char:1 + pip install django
it means, that there is no .venv(virtual environment) folder and you need to either find a way tofirst add a new python file>click save, then add .venv folder ‘py -m venv venv‘ then you will see python 3.13.3 (.venv) at the bottom of vscode, then kill the terminal then open a new one, then can simply run any ‘pip’ command. can follow this or if above don’t work, then can run ‘py -m ensurepip --default-pip’ then run ‘py -m pip install django’
-to create a new django project run ‘py -m django startproject <project-name> .’
‘python3’ in mac, ‘python’ in windows
-to run django server, ‘python manage.py runserver’
