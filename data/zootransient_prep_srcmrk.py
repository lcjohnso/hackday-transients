# Zooniverse Transient Data Preparation Script
# Use CSV export: zoo_transients.csv
import pandas as pd

d = pd.read_csv('zoo_transients.csv')

with open("catmarkers.txt", "w") as file:
    for index,row in d.iterrows():
        projtxt = 'Discovered by: {}<br/>'.format(str(row['Project']))
        reflink = '<a href="'+str(row['Link'])+'">Reference Link</a>'
        if row['User IDs'] != row['User IDs']:
            body = projtxt + reflink
        else:
            body = projtxt + 'Volunteers: '+str(row['User IDs'])+'<br/>'+reflink
        name =  '{} {}'.format(str(row['Transient type']),str(row['Transient Name']))
        file.write("    cat_markers.addSources(A.marker({}, {}, {{popupTitle: '{}',popupDesc: '{}'}}));\n".format(row['RA'],row['Dec'],name,body))

sources = []
with open("catsources.txt", "w") as file:
    for index,row in d.iterrows():
        sources.append('A.source({}, {})'.format(row['RA'],row['Dec']))
    file.write("    cat_sources.addSources([{}]);".format(','.join(sources)))
