QM-ITL-Print
============

A Python application that will allow you to print in the ITL at Queen Mary from your laptop.

## Depedencies
- Paramiko

## Usage
Before you can execute this script you will have to set a path for where
your print files should be stored. By default it will attempt to put it in ~/username/print/.

When your path is correct everything is pretty straight forward
```bash
$ python print.py filename.pdf
```
You should then be prompted with a username and password. You should enter your ITL
username and password. It should look something like this _eb309_. If the user details
are correct then the file with be uploaded to the school server. The script will
then login and query for available printers. After you have selected a printer it
will send the file for printing.

