import datetime
from flask import Flask, render_template
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
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times

@app.route('/queue_add')
def root():
    # Store the current access time in Datastore.
    store_time(datetime.datetime.now(tz=datetime.timezone.utc))

    # Fetch the most recent 10 access times from Datastore.
    times = fetch_times(10)

    return render_template(
        'index.html', times=times)
            
            
            rs_level,users=use.check_ready()
            if rs_level:
                found=1
                users_mentions=[]
                for user in users:
                    users_mentions.append('<@'+user+'>')
                res_msg = str(users_mentions).strip("[']")+' ready for '+str(rs_level) +". Where ya bitches off to?",found
        else:
            print('found is not 0',found)
            res_msg= "you're already in a queue for "+str(rs_active_queue)
        if found==0:
            await queue_init(ctx)
        else:
            await ctx.send(res_msg)
