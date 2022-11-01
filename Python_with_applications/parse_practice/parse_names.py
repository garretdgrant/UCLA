"""modules used to parse and turn into json"""
import csv
import json

old_subs = []
def parse_csv():

    with open('newsletter_subscribers.csv','r', encoding='UTF-8') as subs:
        csv_reader = csv.DictReader(subs)

        for line in csv_reader:
            print(line)

    
parse_csv()
