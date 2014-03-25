import bottle
from bottle import response, route
from bottle import static_file


@route('/jsontocsv')
def jsontocsv(request=None, method=['GET', 'POST']):
    import pdb; pdb.set_trace()
    print request
    return '123'


@route('/wrangler/<filename:path>')
def send_static(filename):
        return static_file(filename, root='./wrangler/')




bottle.run(port='8080')

                                                                        

