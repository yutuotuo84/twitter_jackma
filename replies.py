import tweepy
import json

API_Key = 
API_Secret = 
Access_Token = 
Access_Token_Secret = 

# get credentials at developer.twitter.com
auth = tweepy.OAuthHandler(API_Key, API_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth)

# update these for whatever tweet you want to process replies to
name = "JackMa"
tweet_id = "1239388330405449728"

replies = tweepy.Cursor(api.search, q='to:{} filter:replies'.format(user_name)), tweet_mode='extended').items()
f = open('./replies.json', 'w', encoding='utf-8')

while True:
    try:
        reply = replies.next()
        if hasattr(reply, 'in_reply_to_status_id_str'):
            if str(reply.in_reply_to_status_id_str) == tweet_id:
               logging.info("reply of :{}".format(reply.full_text))
               json.dump(reply._json, f)

    except tweepy.RateLimitError as e:
        logging.error("Twitter api rate limit reached".format(e))
        time.sleep(60)
        continue

    except tweepy.TweepError as e:
        logging.error("Tweepy error occured:{}".format(e))
        break

    except StopIteration:
        break

    except Exception as e:
        logger.error("Failed while fetching replies {}".format(e))
        break

f.close()