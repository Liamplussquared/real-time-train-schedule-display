import requests
from xml.etree import ElementTree as ET


# using requests library to make the request
response = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode=mhide")
# need to parse XML document
root = ET.fromstring(response.content)

# store in tabular form
html = "<table> <tr> <th>Train code</th> <th>Origin</th> <th>Destination</th> <th> Destination time</th> " \
       "<th>Arrival</th> <th>Departure</th> </tr> "

# run through XML structure and dig out important information and store as row in html talbe
for child in root:
    html += "<tr>"
    for train in child:
        ele = train.tag[35:]
        if ele == 'Destinationtime':
            print("Destination time", train.text)
            html += "<td>" + train.text + "</td>"
        if ele == 'Origin':
            print("Origin:", train.text)
            html += "<td>" + train.text + "</td>"
        if ele == 'Destination':
            print("Destination:", train.text)
            html += "<td>" + train.text + "</td>"
        if ele == 'Traincode':
            print("Traincode is:", train.text)
            html += "<td>" + train.text + "</td>"
        if ele == 'Exparrival':
            print("Expected arrival:", train.text)
            html += "<td>" + train.text + "</td>"
        if ele == 'Expdepart':
            print("Expected departure:", train.text)
            html += "<td>" + train.text + "</td>"

    print("")
    html += "</tr>"

html += "<table>"

# print out html tag for the table
print(html)

