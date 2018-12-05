#!usr/bin/python
# dummy.py

import sys
import json

txtDir = sys.argv[1]
inpDir = sys.argv[2]
outDir = sys.argv[3]

# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read().replace('\n', ' ')
    # close the file
    file.close()
    return text

## load publications
file = 'publications.json'
pubJsonTxt = load_doc(inpDir+file)
pubJson = json.loads(pubJsonTxt)

# Read Files
# files = []
# for i in pubJson[:5]:
#     files.append(load_doc(txtDir+i['text_file_name']))
# files[4]

datasetcit = []
data_set_mentions = []
methods = []
research_fields = []
for pub in pubJson[:5]:
    row = {}
    row["publication_id"]= pub['publication_id']
    row["data_set_id"]= 100
    row["score"]= 1
    row["mention_list"]= ["survey 2000", "2010 study"]
    datasetcit.append(row)
    row = {}
    row["publication_id"]= pub['publication_id']
    row["mention_list"]= ["survey 2000", "2010 study"]
    row["score"]= 1
    data_set_mentions.append(row)
    row = {}
    row["publication_id"]= pub['publication_id']
    row["method"]= ["p value"]
    row["score"]= 1
    methods.append(row)
    row = {}
    row["publication_id"]= pub['publication_id']
    row["research_field"]= ["Science baby"]
    row["score"]= 1
    research_fields.append(row)

with open(outDir+'data_set_citations.json', 'w') as fp:
    json.dump(datasetcit, fp)

with open(outDir+'data_set_mentions.json', 'w') as fp:
    json.dump(data_set_mentions, fp)

with open(outDir+'methods.json', 'w') as fp:
    json.dump(methods, fp)

with open(outDir+'research_fields.json', 'w') as fp:
    json.dump(research_fields, fp)
