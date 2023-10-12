#! /usr/local/bin/python3
import os 
import time 
import sys
import cgi, ui, cgitb
cgitb.enable()

print(ui.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR'] 
host = os.environ['REMOTE_HOST'] 
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())
form = cgi.FieldStorage()
for each_form_item in form.keys():
    print(each_form_item + '->' + form[each_form_item].value,  end=' ',  file=sys.stderr)    
print(host + ", " + addr + ", " + cur_time + ": " + method, file=sys.stderr)
print(file=sys.stderr)    
print('OK.')