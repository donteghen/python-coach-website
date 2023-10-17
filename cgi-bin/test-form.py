#! /usr/local/bin/python3
import ui, sqlite3

print(ui.start_response('text/html')) 
print(ui.do_form('add_timing_data.py', ['Name', 'dob','TimeValue'], text='Send'))