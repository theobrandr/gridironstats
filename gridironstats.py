from playbook import pregame
from playbook import load
from playbook import extract
from playbook import reporting
from playbook import transform
import argparse
from datetime import date
from datetime import datetime

parser = argparse.ArgumentParser(description='gridironstats Arguments')
parser.add_argument("-s", "--skip_extract", action='store_true',
                    help="Skip the data extraction process if new data is not needed")

args = parser.parse_args()

if args.skip_extract:
   skip_extract = 1
else:
    skip_extract = 0

def extract_espn_data():
    extract.espn_nfl_teams()
    extract.espn_nfl_team_roster()
    extract.espn_nfl_scoreboard()
    extract.espn_nfl_athletes()
    extract.espn_nfl_team_stats()
    extract.espn_nfl_athlete_stats()
    extract.espn_nfl_team_roster_stats()
    transform.espn_team_stats_oponent()

def nfl_reporting():
    reporting.espn_figure_teams_average_score_bar()
    reporting.espn_figure_teams_cat_scores_wide_table()
    reporting.espn_figure_teams_cat_scores_long_table()
    reporting.espn_export_to_csv()


if __name__ == '__main__':
    print("Gridiron Stats: Your Playbook to Success through Sports Data ETL's and Reporting.")
    # Prepare and check the ETL is ready to run

    pregame.check_sqllite_db()

    if skip_extract == 1:
        nfl_reporting()

    elif skip_extract == 0:
        extract_espn_data()
        nfl_reporting()

    exit()
