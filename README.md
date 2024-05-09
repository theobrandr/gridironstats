# gridironstats
ETL for NFL/Professional Football Data and Analytics

# Blitzanalytics
Your Playbook to Success through NFL/Professioanl football Data ETL's and Reporting.
The program will extract 5 years of NFL data, transform the data, load the data into a local database, and automatically generate reports.  

**Program Status**
<br>
- [50%] National Football League Data
- [0%] National Football League Matchup Reporting
- [0%] National Football League Team Reporting

**Getting Started**
<br>
  If you don't already have the additional packages installed you will need to install them with pip
  - pip install -r requirements.txt

**Usage**
<br>
  gridironstats.py

**Program Arguments***
  python gridironstats.py [-s]
  -s, --skip_extract: Skip the data extraction process if new data isn't required.


**File Storage**
  In order to avoid re-pulling all previous years cfb data with every run of the script, a local sqlite database will be created in the directory the script is run from. 


**National Football League**
