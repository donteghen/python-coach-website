#! /usr/local/bin/python3


import cgi, ui, cgitb, sqlite3
cgitb.enable()

form_data = cgi.FieldStorage()
athelet_id = int(form_data["athlete"].value)
new_time = float(form_data["time"].value)

page = ''
page = ui.start_response('text/html')
page += ui.include_header("Add time successful")

cxn  = sqlite3.Connection('coachdata.sqlite')  
cursor = cxn.cursor()
print('inserting {} and {}'.format(athelet_id, new_time), file='stderr')
cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (athelet_id, new_time))
cxn.commit()
cxn.close()
page += ui.para('Insert operation successful!')
page += ui.skipLines(2)
page += ui.include_footer({"home": "/"})
print(page)