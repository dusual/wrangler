import bottle
from bottle import response, route, request
from bottle import static_file
import json
import csv

@route('/jsontocsv', method='POST')
def jsontocsv():
    f =  request.body
    data = json.load(f)
    f.close()
    fieldnames = data[0].keys()
    
    with open('./wrangler/csv/new.csv','w') as f:
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(data)


@route('/wrangler/<filename:path>')
def send_static(filename):
        return static_file(filename, root='./wrangler/')




bottle.run(port='8080')

                                                                        

