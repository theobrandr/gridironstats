# gridironstats
ETL for NFL/Professional Football Data and Analytics

# Blitzanalytics
Your Playbook to Success through NFL/Professioanl football Data ETL's and Reporting.
The progrma will extract 5 years of NFL data, transform the data, load the data into a local database, and automatically generate reports.  

**Program Status**
<br>
- [10%] National Football League Data
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
  python script_name.py [-cfb] [-nfl] [-p] [-r REPORT_WEEK] [-y REPORT_YEAR] [-t] [-d] [-s]
  
  -r REPORT_WEEK, --report_week REPORT_WEEK: Specify a week for reporting. The default week is the current week.
  -y REPORT_YEAR, --report_year REPORT_YEAR: Specify a year for reporting. The default year is the current year.
  -t, --season_type: Specify 'regular' for Regular Season or 'postseason' for PostSeason.
  -d, --delete_tables: Delete all DB tables if the database is consuming excessive space. Run the program with the -p flag afterward to re-populate the DB.
  -s, --skip_extract: Skip the data extraction process if new data isn't required.


**File Storage**
  In order to avoid re-pulling all previous years cfb data with every run of the script, a local sqlite database will be created in the directory the script is run from. 


**National Football League**
