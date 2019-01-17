import csv
import json
import os


def main():
    # CSV format = separators = , & separator number = .
    # Open the CSV
    f = open('Book1.csv', 'r')
    json_file = open('parsed.json', 'w')
    # Change each fieldname to the appropriate field name. I know, so difficult.  
    fieldnames = ("Number", "Lastname", "Firstname", "Age", "Sex")
    reader = csv.DictReader(f, fieldnames)
    # Parse the CSV into JSON

    cpt = 0
    json_file.write("[\n")
    for row in reader:
        if cpt != 0:
            json.dump(row, json_file)
        cpt += 1
    json_file.write("\n]")
    json_file.close()

    f1 = open('parsed.json', 'rt')
    content = f1.read()
    f1.close()

    content_final = content.replace("}{", "},\n{")

    f2 = open('parsed_final.json', 'w+')
    f2.write(content_final)
    f2.close()

    os.remove('parsed.json')

    print('\nJSON generated !')


if __name__ == "__main__":
    main()
