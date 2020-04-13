import flask

def hello_world(request):

    name = request.args.get('name')
    if name:
        resp =  'Hello ' + name
    else:
        resp =  'Hello World'
    response = flask.jsonify({'response': resp})
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response