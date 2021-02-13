from bottle import route, run, template, get, post, request, static_file

@route('/')
def hello():
        return "Hello World!"

@route('/api/<inputname>')
def hello(inputname):
        return template('<b>api {{name}}</b>!',name=inputname)

@get('/plus') # or @route('/plus')
def login():
    return '''
        <form action="/plus" method="post">
            A: <input name="numberA" type="text" />
            B: <input name="numberB" type="text" />
            <input value="Plus" type="submit" />
        </form>
    '''

@post('/plus') # or @route('/plus', method='POST')
def do_login():
    numberA = int(request.forms.get('numberA'))
    numberB = int(request.forms.get('numberB'))
    return template('Answer is {{ans}}',ans=numberA+numberB)

@get('/test/<filename>')
def server_static(filename):
    return static_file(filename, root='html/')

run(host='192.168.4.42', port=50000, debug=True)