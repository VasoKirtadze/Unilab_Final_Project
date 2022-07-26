
## Setup & Run
To make the project run on your device you need have [Python 3.x installed](https://realpython.com/installing-python/).

### virtualenv
It's highly recommended to use virtual environments while working on the project. 
To set up the environment we will be using [venv](https://realpython.com/python-virtual-environments-a-primer/) module.

# On Windows:

#### Install
Installing virtualenv module:
```bash
pip install virtualenv
```

#### Set up
To set up the virtual environment, move to the chosen directory and use the following 
command(usually it is called venv, but you can use another name): 
```bash
virtualenv venv
```

#### Activate
Activating virtual environment:

```bash
venv\scripts\activate
```
If done correctly you should (venv) before your directory, for example:
<br> (venv) C:\Users\Name\Desktop\Project_dir



# On Linux or Mac:

#### Install
Installing virtualenv:
```bash
pip install virtualenv
```


### Activate

```bash
source venv/bin/activate
```

## Installing requirements
After activating venv, run the following command:
```bash
cd AthLead
pip install -r requirements.txt
```

### Run 
To run the application
```bash
python manage.py
```

## Go to  http://127.0.0.1:5000/

#### When you're done:
#### On Windows:
```bash
venv\scripts\deactivate
```
#### On Linux or Mac:
```bash
deactivate
```
