#
# Twitter API REST Gathering Script
#
# Author: Anderson Sprenger, Pedro Wagner, Pedro Sanvido
# Date: May 23, 2023
#

import os
import sys
import argparse
import json
import datetime
import logging

from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened


def get_key():
    p = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DATA', 'keys.txt'))
    with open(p, 'r') as arq:
        chave = arq.read().splitlines()[0]
    return chave


def authenticate():
    key = get_key()
    return Twarc2(bearer_token=key)


def date_check(since, until):
    now = datetime.datetime.utcnow()
    if since > until:
        sys.stdout.write("'since' parameter cannot be newer than 'until'.\nQuitting...")
        sys.exit(0)


def collect_tweets(args, twarc):
    arq = open(args.outfile, 'w')
    arq.write("[\n")
    counter = 1

    if 'lang:' not in args.query:
        args.query = '(' + args.query + ')'
        if args.language == 'pt and en':
            args.query += ' (lang:pt OR lang:en)'
        elif args.language != 'None':
            args.query += ' lang:' + args.language

    search_count = twarc.counts_all(args.query, start_time=args.start_time, end_time=args.end_time)
    for page in search_count:
        search_count = page['meta']['total_tweet_count']
        break

    if search_count == 0:
        sys.stdout.write('\nThere are no tweets to collect. Finishing...')
        return
    elif search_count > args.maxtweets:
        sys.stdout.write('\nThe search resulted aproximately in %i tweets. Collecting %i of them...' % (
        search_count, args.maxtweets))
    else:
        sys.stdout.write('\nThe search resulted aproximately in %i tweets. Collecting all of them...' % search_count)

    search_results = twarc.search_all(query=args.query, start_time=args.start_time, end_time=args.end_time,
                                      tweet_fields="attachments,created_at,lang,author_id,public_metrics,entities",
                                      max_results=500)

    for page in search_results:
        for tweet in ensure_flattened(page):
            tweet_id = tweet['id']
            text = tweet['text']
            created_at = tweet['created_at']
            lang = tweet['lang']
            author_id = tweet['author_id']
            rt_count = tweet['public_metrics']['retweet_count']

            urls = []
            people_cited = []
            probability = 0.70  # add entities with 70% probability or more to be a person

            if 'entities' in tweet:
                if 'urls' in tweet['entities']:
                    for url in tweet['entities']['urls']:
                        urls.append(url['url'])

                if 'annotations' in tweet['entities']:
                    for annotation in tweet['entities']['annotations']:
                        if annotation['type'] == 'Person' and annotation['probability'] >= probability:
                            people_cited.append(annotation['normalized_text'])

            has_rich_media = False
            if 'attachments' in tweet:
                if 'media_keys' in tweet['attachments'] or 'poll_ids' in tweet['attachments']:
                    has_rich_media = True

            line = {
                'id': tweet_id,
                'text': text,
                'created_at': created_at,
                'lang': lang,
                'author_id': author_id,
                'retweet_count': rt_count,
                'urls': urls,
                'people_cited': people_cited,
                'has_rich_media': has_rich_media
            }
            line['created_at'] = datetime.datetime.strptime(line['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime(
                '%Y-%m-%dT%H:%M:%SZ')

            if counter == 1:
                arq.write(json.dumps(line) + '\n')
            elif counter >= args.maxtweets:
                break
            else:
                arq.write(',' + json.dumps(line) + '\n')

            sys.stdout.write("\rNumber of tweets collected so far...: %i" % counter)
            sys.stdout.flush()
            counter += 1

        if counter >= args.maxtweets:
            break

    arq.write("]")
    arq.close()
    sys.stdout.write('\nAll done! Finishing...')


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def add_args():
    parser = argparse.ArgumentParser(description='Coleta tweets de acordo com a query, data e limites.')
    parser.add_argument('-q', '--query', metavar='', required=True)
    parser.add_argument('-s', '--start_time', metavar='', required=True, help='"YYYY-MM-DDTHH:mmZ"  UTC')
    parser.add_argument('-u', '--end_time', metavar='', required=True, help='"YYYY-MM-DDTHH:mmZ" UTC')
    parser.add_argument('-m', '--maxtweets', metavar='', type=int, default=100)
    parser.add_argument('-l', '--language', metavar='')
    parser.add_argument('-o', '--outfile', metavar='', default="output.json")
    return parser.parse_args()


def main():
    setup_logging()
    args = add_args()

    date_check(datetime.datetime.strptime(args.start_time, '%Y-%m-%dT%H:%MZ'),
               datetime.datetime.strptime(args.end_time, '%Y-%m-%dT%H:%MZ'))
    args.start_time = args.start_time[:-1] + ':00Z'
    args.end_time = args.end_time[:-1] + ':00Z'

    twarc = authenticate()
    collect_tweets(args, twarc)


if __name__ == "__main__":
    main()
