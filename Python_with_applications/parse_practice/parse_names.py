import csv

young_subscribers = []
            
with open('newsletter_subscribers.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    for line in csv_reader:
        age = int(line['age'])
        if age <= 30:
            young_subscribers.append(line)


with open('young_subs_2.csv', 'w', newline='') as young_subs_2_csv:
    fieldnames = ('name', 'email', 'age', 'referred_by')
    csv_writer = csv.DictWriter(young_subs_2_csv,fieldnames=fieldnames)
    csv_writer.writeheader()
    for sub in young_subscribers:
        csv_writer.writerow(sub)

