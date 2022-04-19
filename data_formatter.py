import json
import csv

with open('kegg_pathway.json') as json_file:
    kegg_pathway = json.load(json_file)



reformatted_data = open('reformatted_data.csv')

csv_writer = csv.writer(reformatted_data)

print(kegg_pathway)
