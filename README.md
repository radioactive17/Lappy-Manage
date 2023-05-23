# Lappy-Manage
  
Lappy-Manage provides a user-friendly and comprehensive solution for individuals seeking to purchase a laptop. By providing a range of parameters, users can confidently choose a laptop that best suits their needs, without being overwhelmed by technical specifications.

## Install Dependencies
Go to the directory containing requirements.txt 
```bash
pip install -r requirements.txt
```

## Setup Database
You code wont be executed until you set up your database.
Following are the steps to setup your database for PostgreSQL. 
1. Create a database named Lappy in the PostgreSQL
2. Change the settings.py file in lappy_manage directory accordingly. 
```python
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'Lappy',
       'USER': os.environ.get('DB_USER'),
       'PASSWORD': os.environ.get('DB_PASS'),
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}
```
Note: Different Databases require differnet setup. Pleae setup your database accordingly.

## Run the program
After installing the dependencies and setting up the database you should be good to go and execute the program.  
Make sure you are in the directory containing manage.py file and Run the following command line to bring up the sever 
```bash
python manage.py runserver
```
If everything went smoothly, you should see the below screen.   
  
![cmd](https://github.com/radioactive17/Cricbee/blob/main/Readme%20images/cmd.png?raw=true)

If you run into errors. Please look online for solutions

## Few Snippets of the application
<img src="readme images/fig1.png" width="750">
<img src="readme images/fig2.png" width="750">
<img src="readme images/fig3.png" width="750">

## Dataset
The Lappy Manage project obtained its laptop dataset from Kaggle, which contains information about various laptops, including brand, model, processor type, screen size, RAM, storage capacity, and price. The dataset was collected by the website PriceSpy in August 2020, with the goal of providing consumers with information about different laptop models and their prices. It is unclear who collected the raw data that PriceSpy used to compile the dataset, but it is likely that the data was gathered from various online retailers and laptop manufacturers.
The dataset can be found on: https://www.kaggle.com/datasets/dhanushbommavaram/laptop-dataset

## Developers
Jignesh Nagda | Chinmay Lotankar | Dinesh Mannari
