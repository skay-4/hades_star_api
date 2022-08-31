from threading import local
from flask import Flask, render_template,request
from requests.models import Response
import pandas as pd
from google.cloud import firestore
import pandas as pd
app = Flask(__name__)
db = firestore.Client(project='skaynet-356400')



def store_data(rs_level):
    queue_type='network'
    #queue_type='standard'
    doc = db.collection(1).document(1)
    doc.set({
        u'create_time': firestore.SERVER_TIMESTAMP,
        u'queue_type':queue_type,
        u'red_star_level':rs_level,
        u'users': ['api_user','api_user']})



def check_if_in_queue(user_id):
    queues_obj=db.collection('red_star_groups').where(u'users', u'array_contains', user_id)
    queues= queues_obj.stream()
    for queue in queues:
        queue_id=f'{queue.id}'
        queue_dict=queue.to_dict()
        print(queue_id)
        print(queue_dict)


@app.route('/queue_add') #This may happen in the discord bot
async def queue_add():
    args = request.args
    if 'lvl' in request.args and 'room_left' in request.args:
        lvl=args.get('lvl')
        print(lvl)
    else:
        res_json={'response':{'status':400,'content':{'error':'missing parameter'}}}
        return res_json

    if 'users' in request.args:
        users=args.get('users')
        users.split(',')
    else:
        user='api_user'
    return {'response':{'status':200,'content':{'today':'2022-08-31'}}}
    




@app.route('/player_request')
async def player_request():
    args = request.args
    if 'number' in args and 'lvl' in args:
        number=args.get('number')
        lvl=args.get('lvl')
        queues_obj=db.collection('red_star_groups').where(u'red_star_level', u'==', 5)
        queues=pd.DataFrame()
        for t in queues_obj.stream():
            queues=pd.concat((queues,pd.DataFrame(t.to_dict())),axis=0)
        queues['create_time']=queues['create_time'].apply(pd.to_datetime)
        for row in queues.sort_values(by='create_time',ascending=True):
            group_size=len(row[1]['users']) #stop the loop when it finds a matching group
            #Remove from database if it matches
    else:
        print('missing argument: number')
    return '200 2022-08-31'

app.run(host='localhost',port=8080)

'''

'''
            
#TODO: See about adding libs to .gitignore
'''
FLOW:
Create group of 1, 2, or 3 people, 
Respond to queue requests w/any matching group
That bot sends a discord link



Discord bot puts groups in the database

This bot checks the noSQL database for groups when its called

NOW: accept request and create group
'''