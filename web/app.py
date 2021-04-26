"""
Melodie Collins' Flask API.
"""

from flask import Flask, abort, render_template
import os

app = Flask(__name__)

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html')

@app.errorhandler(403)
def error_403(e):
    return render_template('403.html')

@app.route("/<path:f_name>")
def respond(f_name):
    '''
    If page starts with (~ // ..) respond with 403 forbidden error.
    '''
    if (("~" in f_name) or ("//" in f_name) or (".." in f_name)):
        abort(403)

    '''If path/to/name.html is in document path (from DOCROOT), send contents of name.html
    or name.css with proper http response. Else, respond with 404 not found error.
    '''
    if (f_name[-5:] == ".html" or f_name[-4:] == ".css"):
        '''Make list of names of files and directories in current working directory. If
        name of file in list, open and read it.
        '''
        if f_name in os.listdir(os.curdir):
            f=open(f_name, 'r')
            return f.read()
        else:
            abort(404)
    else:
        return "Invalid input!\n"

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
