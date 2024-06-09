# Software Engineering II
## UFMG 2024/01 
Software Engineering II - Practical Assignment 5&6  
Bernardo Franco Tormin

## System explanation

- The current purpose of this software is to provide to the user a simple year-month summary of him/her income x expenditures;
- The input will be a json file inside the folder data with the year-month-income and year-month-expenditure;
- The output will be a terminal message with a summary of its total income, total expenditure, balance and also the most significant income and expenditure for the choosen year-month;
- The user will have a few arguments options to make the software give him/her the expected output.

## Language

- Python

## System limitations

- It is intended to be running with Python3.10.14. If the user try using another version, it is not guarantee to properly work with it. Additionally, all versions for all libraries used in this project must be the ones in the requirements.txt file.

## Makefile

- Make sure you have the make command installed in your machine and has it defined in your environment variable path, otherwise it it is not going to work;
- The command **make save** will save all libraries utilized in the project;  
- The command **make install** will install all dependecies necessaries to run the code.
  
When using **make save** and **make install**, make sure that you are on you virtual environment.  

# Guide on how to run step-by-step the code  

## Before running the code  

1. You must ensure that you have the Visual Code installed in your machine or another application that can run a python code;  
2. You must ensure that you have Python 3.10.14 installed in your computer. It is not guaranteed that this will work with older versions (you can find it in here: https://www.python.org/downloads/release/python-31014/);  
3. You must create a virtual environment with Python 3.10.14  and chose it to use as your interpreter (Ctrl+Shift+P -- Python Interpreter) for running the application;  
4. You must get inside your new virtual environment and use the command **make install** to install all dependecies necessaries to run the code;  
5. If the make command is not working, you can install it manually or using the line **pip install -r requirements.txt**. 