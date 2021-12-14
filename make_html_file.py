import json
from yattag import Doc
import csv
import argparse

class Config(object):
    filename = None

    def __init__(self, filename):
        self.filename = filename

def generatehtml(rows):
    doc, tag, text = Doc().tagtext()
    global count
    #print(rows)
    with tag('html'):
        with tag('head'):
            doc.asis('<meta charset="utf-8">')
            doc.asis('<meta name="viewport" content="width=device-width, initial-scale=1">')
            doc.asis('<link rel="stylesheet" href="./test.css">')
        with tag('body'):
            #Parameters
            title = 'Parameters: '
            # title = title + ' Score_Max is ' + str(config.scoremax)
            # title = title + ' Dedup_Score_Threshold is ' + str(config.dedupscore)

            with tag('h3'):
                text(title)
            with tag('table'):
                with tag('thead'):
                    with tag('tr'):
                        with tag('th'):
                            text('No.')
                        with tag('th'):
                            text('Time')
                        with tag('th'):
                            text('ユーザ画像')
                        with tag('th'):
                            text('結果個数')
                        with tag('th'):
                            text('結果1')
                        with tag('th'):
                            text('結果2')
                        with tag('th'):
                            text('結果3')
                        with tag('th'):
                            text('結果4')
                        with tag('th'):
                            text('結果5')
                        with tag('th'):
                            text('結果6')
                        with tag('th'):
                            text('結果7')
                        with tag('th'):
                            text('結果8')
                        with tag('th'):
                            text('結果9')
                        with tag('th'):
                            text('結果10')
                        with tag('th'):
                            text('結果11')
                        with tag('th'):
                            text('結果12')
                with tag('tbody'):
                    for row in rows:
                        # Merge 3 lines to one.
                        for t in range(3):
                            if t == 0:
                                with tag('tr'):
                                    for i in range(len(row)):
                                            if i == 0:
                                                with tag('td',rowspan='3'):
                                                    text(row[i])
                                            elif i == 1:
                                                with tag('td',rowspan='3'):
                                                    text(row[i])
                                            elif i == 2:
                                                with tag('td',rowspan='3'):
                                                    doc.stag('img', src=row[i])
                                            elif i == 3:
                                                with tag('td',rowspan='3'):
                                                    text(row[i])
                                            else:
                                                with tag('td'):
                                                    text(row[i][t])
                            elif t == 1:
                                with tag('tr'):
                                    for i in range(len(row)):
                                        if i > 3:
                                            with tag('td'):
                                                doc.stag('img', src=row[i][t])
                            elif t == 2:
                                with tag('tr'):
                                    for i in range(len(row)):
                                        if i > 3:
                                            with tag('td'):
                                                text(row[i][t])

    result = doc.getvalue()
    return result

def main(config,filenumber):
    f = open(config.filename,'r')
    Lines = f.readlines()

    allrecords = []
    count = 0
    for line in Lines:
        count += 1
        #[no, timestamp, imageurl, result_number, [result_set1], [result_set2], ...,]
        #result_set = [im_name, url, score]
        jsonline = json.loads(line.strip())

        resultsize = len(jsonline["result_im_urls"])

        oneRecord = []
        oneRecord.append(count)
        oneRecord.append(jsonline["timestamp"])
        oneRecord.append(jsonline["im_url"])
        oneRecord.append(resultsize)

        orgnizedResults = []
        for index, value in enumerate(jsonline["result_im_names"]):
            oneResults = []
            oneResults.append(value)
            oneResults.append(jsonline["result_im_urls"][index])
            oneResults.append(jsonline["scores"][index])
            orgnizedResults.append(oneResults)

        oneRecord.extend(orgnizedResults)
        allrecords.append(oneRecord)
    #Export HTML
    html = generatehtml(allrecords)
    with open("Interior_Result_Q1_sample500.html", mode='w') as f:
        f.write(html)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Uploadsearch query with results')
    parser.add_argument('--filename', required=True, dest='filename', type=str,
                        help='please enter filename')

    args = parser.parse_args()
    
    config = Config(filename=args.filename)
    main(config,10)
