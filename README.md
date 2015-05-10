Nand-Performance-Showing-via-Python-Excel
=========================================

This API series are intended for automatic process of raw data (mainly txt, pat files) and show results via excel or intrinsic python console.

### Features:
--1: Adding Tkinter/wxpython module  for user-friendly interface;

--2: Adding openpyxl module for saving processed data into excel file; 

--3: Adding os, glob. shutil module for file system operation;

--4: Adding functools for binary file operation;


#### API One: [Erase,Write,Read Analysis](https://github.com/jinstrong/Nand-Performance-Showing-via-Python-Excel/blob/master/Erase%2CWrite%2CRead%20Analysis.py)
Module used:glob, os, openpyxl, Tkinter;

Function:iterate in specified folder, process all txt files, and save result into excel files;   

Feature: warning mechanism for data errors;


####  API Two: [Dynamic Read Processing](https://github.com/hjq1990/Nand-Performance-Showing-via-Python-Excel/blob/master/Dynamic%20Read%20Processing%20Ver%201.py)
Module used: functools, openpyxl, math

Function: iterate in specified folder, process all pat files, and save result into excel files; 
Feature: 

####  API Three: [Bit Map Check From Memory](https://github.com/hjq1990/Nand-Performance-Showing-via-Python-Excel/blob/master/Bit%20Map%20Check%20From%20Memory)
Module used: openpyxl

Function: reads bit map of memory and show bad blocks


####  API Four: [Error Log Check](https://github.com/jinstrong/Nand-Performance-Showing-via-Python-Excel/blob/master/Error%20Log%20Check.py)
Module used: openpyxl, wx, glob, os, functools

Function: read binary file of error log, process, and save to excel file


####  API Five: [Data_Logs_Fetching_From_Server](https://github.com/jinstrong/Nand-Performance-Showing-via-Python-Excel/blob/master/Data_Logs_Fetching_From_Server.py)
Module used: os, shutil

Function: search within shared folder for test datalogs and save to specified dist when found

