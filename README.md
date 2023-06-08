<h1 align="center">Vbchecker</h1>
<h2 align="center">CVE-2016-6195 Exploit</h2>
<h3 align="center">Inspired by <a href='https://github.com/Ishanoshada'>Vbully</a></h2>

**Disclaimer:** I take no responsibility for whatever you decide to do with this code, there are still many websites running vulnerable vbulletin versions and I recommend them to always stay with the latest update. Use at your own discretion.

# Vbchecker
This is a simple python script that utilizes the CVE-2016-6195 vulnerability, the only difference is it has the functionality to choose a custom Table and or Column Name.

```
usage: vbchecker.py [-h] --url URL --dump {1,2,3} [--table TABLE] [--column COLUMN]

CVE-2016-6195 exploit

options:
  -h, --help       show this help message and exit
  --url URL        Enter url
  --dump {1,2,3}   1.) Enumerate Tables 2.) Enumerate Columns 3.) Dump Users,Password & Hash/Salt
  --table TABLE    Enter table name
  --column COLUMN  Enter column name
  ```
  
Install Libraries:
  
    pip install -r requirements.txt
