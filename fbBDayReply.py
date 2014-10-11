import requests
import json

# unix time stamp for 7 October, 2014
AFTER = 1412611593
TOKEN = 'XXXXX'

def get_posts():
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
            "filter_key = 'others' AND source_id = me() AND "
            "created_time > AFTER LIMIT 200")

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    # for res in result['data']:
    # 	get_school = requests.get(res['actor_id'] + "?fields=name,first_name,education&access_token="+TOKEN)
    # 	#if get_school["education"][1]['school']['name'] == "Delhi College of Engineering"
    return result['data']

def commentall(wallposts):
    for wallpost in wallposts:

        try:
            r = requests.get('https://graph.facebook.com/%s' % wallpost['actor_id'])
            url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
            user = json.loads(r.text)
            if wallpost['actor_id'] == 1347153329 or wallpost['actor_id'] == 1673833632:
                message = "Thanks " + user['first_name'] + " sir :)"
            else:
                message = "Thanks " + user['first_name'] + " :)"
            print message
            payload = {'access_token': TOKEN, 'message': message}
            s = requests.post(url, data=payload)
            payload = {'access_token': TOKEN}
            t = requests.post("https://graph.facebook.com/"+wallpost['post_id']+"/likes", data=payload)
            print "Wall post %s done" % wallpost['post_id']
        except:
            print "could not print"	        

if __name__ == '__main__':
    commentall(get_posts())