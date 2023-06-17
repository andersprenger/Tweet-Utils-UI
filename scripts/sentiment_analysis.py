import sys
import argparse
import json
import pathlib

from scripts.modules.sentiment_classifier import SentimentClassifier

sys.path.append("..")


def add_args():
    parser = argparse.ArgumentParser(
        description='Classify tweets as positive, negative, or neutral with machine learning techniques.')
    parser.add_argument('-i', '--infile', metavar='', required=True,
                        help='Input JSON file to be cleaned. Has to contain a key named text')
    parser.add_argument('-o', '--outfile', metavar='', default='output_clean.json',
                        help='Filename for the resulting output. Default is "output_clean" in the input file '
                             'extension format')
    return parser.parse_args()


def write_json(outfile, data):
    json_string = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    with open(outfile, 'w', encoding='utf8') as f:
        f.write(json_string)
    sys.stdout.write('All done. File written to ' + outfile)


def write_file(infile, outfile, data):
    if outfile != 'output_sentiments.json':
        extension = pathlib.Path(outfile).suffix
    else:
        extension = pathlib.Path(infile).suffix
        outfile = 'output_clean' + extension

    if extension == '.json':
        write_json(outfile, data)
    else:
        sys.stdout.write('Output file must be in JSON format\nQuitting...')


def predict(infile, outfile):
    print('Loading model...')
    classifier = SentimentClassifier()

    print('Loading data...')
    with open(infile, 'r', encoding='utf8') as f:
        data = json.load(f)

    new_data = []

    count = 0
    for tweet in data:
        print('Processing tweet ' + str(count) + ' of ' + str(len(data)))
        count += 1

        temp_request = classifier.predict(tweet)
        sentiment = temp_request['results']

        new_tweet = {}

        for value in tweet:
            new_tweet[value] = tweet[value][0]

        if sentiment == 1:
            new_tweet['emotion'] = 'positive'
        if sentiment == 0:
            new_tweet['emotion'] = 'neutral'
        if sentiment == 2:
            new_tweet['emotion'] = 'negative'

        new_data.append(new_tweet)

    write_file(infile, outfile, new_data)


def main():
    args = add_args()
    predict(args.infile, args.outfile)


if __name__ == "__main__":
    main()
