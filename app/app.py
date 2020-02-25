import flask 
from string import Template
from flask import request
from flask import render_template
from flask import redirect
import os
from datetime import datetime
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

app = flask.Flask(__name__)
app.config['StorageName'] = os.environ.get('StorageName')
app.config['StorageKey'] = os.environ.get('StorageKey')

#StorageName = os.environ.get('StorageName')
#StorageKey = os.environ.get('StorageKey')
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # render a template

@app.route('/badCode')
def badCode():
    return render_template('index.html', formError = "Incorrect Code, Please try again.")

@app.route('/user/<variable>', methods=['GET'])
def userpage(variable):
    table_service = TableService(account_name=app.config['StorageName'], account_key=app.config['StorageKey'])
    name= variable.lower()
    try:
        details = table_service.get_entity('weddingtable', 'Invites', name)
        print(details)
        return render_template("user.html",People1=details.Names, People2=details.Names2, hide=details.Hide, userCode = variable, commentmessage=details.Message)
    except:
        return redirect('/badCode')


@app.route('/locations')
def locations():
    return render_template('locations.html',HomeLink="./")

@app.route('/locations/<UserCode>')
def authedUser(UserCode):
    link = "../user/" + UserCode
    return render_template('locations.html',HomeLink=link)

@app.route('/code', methods=['POST'])
def handle_userCode():
    codepath = '/user/' + request.form['personalCode']
    return redirect(codepath)

@app.route('/Thankyou/<UserCode>')
def thank(UserCode):

    codepath = '/user/' + UserCode
    return render_template('thankyou.html', HomeLink=codepath)

@app.route('/RSVP', methods=['POST'])
def handle_RSVP():
    print('User Code Is: {}'.format(request.form['userCode']))
    table_service = TableService(account_name=app.config['StorageName'], account_key=app.config['StorageKey'])
    now = datetime.now()
    time = now.strftime("%m-%d-%Y %H-%M-%S")
    rsvp = {'PartitionKey': 'rsvp', 'RowKey': time ,'GroupID': request.form['userCode'],
        'comments': request.form['comment'], 'Status': request.form['action']}
    print(rsvp)
    table_service.insert_entity('weddingrsvptable', rsvp)
    redirectlink = '/Thankyou/{}'.format(request.form['userCode'])
    return redirect(redirectlink)

app.run(host='0.0.0.0', port=80, debug=True)