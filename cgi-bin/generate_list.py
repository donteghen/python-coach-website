#! /usr/local/bin/python3
import athletemodel, ui, cgitb
cgitb.enable()


athletes = athletemodel.get_names_from_db_store()
page = ''
page += ui.start_response()
page += ui.include_header('The coach\'s management app')
page += ui.para('Select an athlete from this list to work with:')
page += ui.start_form('generate_timing_data.py')
for athlete in athletes:
    page += ui.radio_button('selectedAthlete', str(athlete["id"]), athlete["name"])
page += ui.end_form('Select')    
page += ui.include_footer({"home": "/index.html"})    
print(page)