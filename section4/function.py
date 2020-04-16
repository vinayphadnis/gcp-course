import flask
def hello_world(request):

    email = request.args.get('email')
    if '@' in email:
        if '.' in email:
            resp = "Email is valid"  
        else:
            resp = 'Email is invalid'  
    else:
        resp = 'Email is invalid'
    response = flask.jsonify({'response': resp})
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response