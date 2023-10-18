#! /usr/local/bin/python3
import cgi, ui, athletemodel, cgitb
cgitb.enable()
form_data = cgi.FieldStorage()
athlete_id = form_data["selectedAthlete"].value
athlete_detail = athletemodel.get_athlete_from_db_by_id(int(athlete_id))
page = ''

page += ui.start_response()
page += ui.include_header('Timing results for {}'.format(athlete_detail["name"]))
page += ui.para('Timing data for {}'.format(athlete_detail["name"]))
page += ui.u_list(athlete_detail["top3"])
page += ui.include_footer({"home": "/", "Select another ahthlete": "generate_list.py", "add athlete time record": "process_time.py"})
print(page)
