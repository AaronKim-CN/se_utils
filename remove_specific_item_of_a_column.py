import csv
import os


def remove_items(input, output, schema, status, delimiter=','):
    """
    remove the row that contains the shopurls in the provided list
    """
    #global csv_reader, csv_writer, index

    try:
        csv_reader = csv.reader(open(input, 'r+'), delimiter=delimiter)
        csv_writer = csv.writer(open(output, 'w+'))
    except Exception as e:
        print(e)

    # get column index
    header = [h.strip() for h in next(csv_reader)]
    if schema in header:
        index = header.index(schema)
    else:
        print('remove_shopurls:invalid schema provided')
        return

    csv_writer.writerow(header)

    print('Removing false item rows...')
    skipcount = 0
    writecount = 0
    for r in csv_reader:
        if r[index] == status:
            skipcount += 1
            continue
        csv_writer.writerow(r)
        writecount += 1
   
    print('Written ' + str(writecount) + ' rows, removed ' + str(skipcount) + ' rows')

if __name__ == '__main__':
    remove_items('./input.csv', './output.csv', 'schema', 'itemname')