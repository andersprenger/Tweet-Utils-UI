import os
import sys
import tweepy
import argparse
import json

def getkey():
    p = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'DATA', 'keys.txt'))
    arq = open(p, 'r')
    chave = arq.read().splitlines()[0]
    arq.close()

    return chave


def add_args():
    parser = argparse.ArgumentParser(description='Coleta tweets de acordo com a query, data e limites.')
    parser.add_argument('-u', '--user', metavar='', required=True)
    parser.add_argument('-o', '--outfile', metavar='', default="output_profile.json")
    return parser.parse_args()


def main():
    args = add_args()
    arq = open(args.outfile, 'w')
    client = tweepy.Client(bearer_token=getkey(), wait_on_rate_limit=True)

    if not args.user.isdigit():
        args.user = client.get_user(username=args.user)
        args.user = args.user.data['id']

    arq.write("[\n")
    counter = 1

    for tweet in tweepy.Paginator(client.get_users_tweets, args.user, max_results=100, tweet_fields=['created_at', 'lang', 'public_metrics', 'author_id']).flatten():
        id = tweet.id
        text = tweet.text
        created_at = tweet.created_at
        lang = tweet.lang
        author_id = tweet.author_id
        rt_count = tweet.public_metrics['retweet_count']
        line = {'id' : id, 'text' : text, 'created_at' : created_at, 'lang' : lang, 'author_id' : author_id, 'retweet_count' : rt_count}
        line['created_at'] = line['created_at'].strftime('%Y-%m-%dT%H:%M:%SZ')
        
        if counter == 1:
            arq.write(json.dumps(line)+'\n')

        else:
            arq.write(','+json.dumps(line)+'\n')

        sys.stdout.write("\rNumber of tweets collected so far...: %i"%counter)
        sys.stdout.flush()
        counter += 1

    arq.write("]")
    arq.close()
    sys.stdout.write('\nAll done! Finishing...')

if __name__== "__main__":
    main()