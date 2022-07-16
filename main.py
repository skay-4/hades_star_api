import datetime
from threading import local
from flask import Flask, render_template,request
from google.cloud import datastore

app = Flask(__name__)
datastore_client = datastore.Client()


def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind='red_star_queues')
    #query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times

@app.route('/queue_add')
def root():
    # Store the current access time in Datastore.
    #store_time(datetime.datetime.now(tz=datetime.timezone.utc))
    args = request
    print(args)
    # Fetch the most recent 10 access times from Datastore.
    limit=10
    times = fetch_times(limit)

    return times

app.run(host='localhost',port=8080)

'''
data_structure={id:entity_id,
                rs_level:rs_level,
                users=[user1,user2,user3]}
'''
            
