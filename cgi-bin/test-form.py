#! /usr/local/bin/python3
import ui

print(ui.start_response('text/html')) 
print(ui.do_form('add_timing_data.py', ['TimeValue'], text='Send'))