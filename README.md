QM-ITL-Print
============

A Python application that will allow you to print in the ITL at Queen Mary from your laptop.

## Dependencies
- Paramiko

## Usage
Before you can execute this script you will have to set a path for where
your print files should be stored. By default it will attempt to put it in ``~/username/print/`. Optionally you can change the variable path.

When your path is correct everything is pretty straight forward

```
$ python print.py filename.pdf
```

You should then be prompted with a username and password. You should enter your ITL
username and password. It should look something like this ``eb309``. If the user details
are correct then the file with be uploaded to the school server. The script will
then login and query for available printers. After you have selected a printer it
will send the file for printing.

A little tip is to make an alias 

## Todo
- Make path if it doesn't exists
- Proper error messages on authentication failure and so on
- Make a "How it works" section in the README

## Known issues
- Might have some Windows issues due to the use of the SSH Protocol
- Known hosts might stop SSH operations if the host is not in the known_hosts file.