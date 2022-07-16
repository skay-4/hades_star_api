from threading import local
from flask import Flask, render_template,request
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client(project='skaynet-356400')


def store_time_OLD(dt):
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815})


def fetch_times(limit):
    queues=db.collection(u'red_star_queues')
    docs = queues.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

@app.route('/queue_add')
def root():

    args = request.args
    if 'lvl' in request.args:
        lvl=args.get('lvl')
        print(lvl)
    else:
        print('400')
        return 400

    if 'user_id' in request.args:
        user=args.get('user_id')
    else:
        user='api_user'
    
    # Fetch the most recent 10 access times from Datastore.
    limit=10
    times = fetch_times(limit)
    print(str(times))
    print('break')
    return str(times)

app.run(host='localhost',port=8080)

'''
data_structure={id:entity_id,
                rs_level:rs_level,
                users=[user1,user2,user3]}
'''
            
#TODO: See about adding libs to .gitignore