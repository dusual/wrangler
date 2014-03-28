import bottle
from bottle import response, route, request, redirect
from bottle import static_file
import json
import csv

@route('/')
def index():
    redirect('/wrangler/index.html')



@route('/jsontocsv', method='POST')
def jsontocsv():
    f =  request.body
    data = json.load(f)
    f.close()
    fieldnames = data[0].keys()
    
    with open('./wrangler/lyra/src/data/new.csv','w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    return "done"

@route('/wrangler/<filename:path>')
def send_static(filename):
        return static_file(filename, root='./wrangler/')




bottle.run(port='8080')

                                                                        

