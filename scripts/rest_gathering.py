#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import tweepy
import argparse
import json
import datetime

def getkey():
    p = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'DATA', 'keys.txt'))
    arq = open(p, 'r')
    chave = arq.read().splitlines()[0]
    arq.close()

    return chave

client = tweepy.Client(bearer_token=getkey(), wait_on_rate_limit=False)

def add_args():
    parser = argparse.ArgumentParser(description='Coleta tweets de acordo com a query, data e limites.')
    parser.add_argument('-q', '--query', metavar='', required=True)
    parser.add_argument('-s', '--start_time', metavar='', required=True, help='"YYYY-MM-DDTHH:mmZ"  UTC')
    parser.add_argument('-u', '--end_time', metavar='', required=True, help='"YYYY-MM-DDTHH:mmZ" UTC')
    parser.add_argument('-m', '--maxtweets', metavar='', type=int, default=100)
    parser.add_argument('-l', '--language', metavar='')
    parser.add_argument('-o', '--outfile', metavar='', default="output.json")
    return parser.parse_args()

def date_check(since, until):
    now = datetime.datetime.utcnow()

    if since > until:
        sys.stdout.write("'since' parameter cannot be newer than 'until'.\nQuitting...")
        sys.exit(0)

def main():
    args = add_args()

    date_check(datetime.datetime.strptime(args.start_time, '%Y-%m-%dT%H:%MZ'), datetime.datetime.strptime(args.end_time, '%Y-%m-%dT%H:%MZ'))
    args.start_time = args.start_time[:-1]+':00Z'
    args.end_time = args.end_time[:-1]+':00Z'

    arq = open(args.outfile, 'w')
    
    arq.write("[\n")
    counter = 1

    for tweet in tweepy.Paginator(client.search_all_tweets, args.query, max_results=100, end_time=args.end_time, start_time=args.start_time, tweet_fields=['created_at', 'lang', 'public_metrics', 'author_id', 'entities']).flatten():
        id = tweet.id
        text = tweet.text
        created_at = tweet.created_at
        lang = tweet.lang

        if args.language == 'pt and en':
            lang_lst = args.language.split(' and ')
            if lang not in lang_lst:
                continue

        elif args.language != 'None' and lang != args.language:
            continue

        author_id = tweet.author_id
        rt_count = tweet.public_metrics['retweet_count']

        urls = []
        if tweet.entities != None and 'urls' in tweet.entities.keys():
            for url in tweet.entities['urls']:
                urls.append(url['url'])

        line = {'id' : id, 'text' : text, 'created_at' : created_at, 'lang' : lang, 'author_id' : author_id, 'retweet_count' : rt_count, 'urls': urls}
        line['created_at'] = line['created_at'].strftime('%Y-%m-%dT%H:%M:%SZ')

        if counter == 1:
            arq.write(json.dumps(line)+'\n')

        elif counter >= args.maxtweets:
            break

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