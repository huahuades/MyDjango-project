import csv

with open('test.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['title','content'])