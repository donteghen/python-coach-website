#! /usr/local/bin/python3
import cgi, ui, athletemodel, cgitb
cgitb.enable()
form_data = cgi.FieldStorage()
athlete = form_data["selectedAthlete"].value

page = ''

page += ui.start_response()
page += ui.include_header('Timing reults for {}'.format(athlete))
page += ui.para('Timing data for {}'.format(athlete))
athlete_time = athletemodel.get_from_store()[athlete].top(top=4)
page += ui.u_list(athlete_time)
page += ui.include_footer({"home": "/", "Select another ahthlete": "generate_list.py"})
print(page)
