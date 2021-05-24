import tweepy
import time
import config
print('twitter bot')


auth= tweepy.OAuthHandler(config.CONSUMER_KEY,config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

ID_FILE = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# 1396429656123924482 for testing
def reply_to_tweets():
    print('replying...')
    last_seen_id = retrieve_last_seen_id(ID_FILE)
    mentions = api.mentions_timeline(since_id = last_seen_id)

    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(mention.id,ID_FILE)
        if '@joeybot404' in mention.text.lower():
            print(str(mention.id) +' '+ mention.text)
            api.update_status(status = '@'+mention.user.screen_name +' shilling',in_reply_to_status_id = mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
    

#test_screen_name = "ephyrl"
#test_user = api.get_user(screen_name = test_screen_name)
#api.send_direct_message(recipient_id = test_user.id, text = "sml jetzt")