#! /usr/local/bin/python3

import ui, sqlite3, cgitb, athletemodel

cgitb.enable()
page = ''
page += ui.start_response('text/html')

athletes = athletemodel.get_names_from_db_store()

page+= ui.include_header("Add an Athlete's time record")
page += ui.para("Select an athlete from the list and enter the new time record")
page += ui.skipLines(1)
page += ui.start_form('add_timing_data.py')
for athlete in athletes:
    page += ui.radio_button('athlete', str(athlete["id"]), athlete["name"])
page += ui.skipLines(2)    
page += ui.create_inputs(['time'])
page += ui.skipLines(1)
page += ui.end_form("Confirm")   
print(page)