import sys, json

def print_help(filename):
    """ Prints out help """
    print("Usage: filename import|export first_file second_file")

def extract_json(json_data):
    """ Extracts json data and creates list for csv """
    translations = {
        "title" : "Formularname",
        "field" : "Frage",
        "choice" : "Antwort",
        "nextButton" : "Vorwärts-Button",
        "previousButton" : "Zurück-Button",
        "button" : "Button"
    }
    csv_list = ['"ID";"Type";"Translation";"Text"']
    # print(data["0"]["title"])
    # print(data["0"]["button"]["text"])
    # print(data["0"]["fields"][0])
    csv_list.append('"0";"button";"{}";"{}"'.format(translations["button"],data["0"]["button"]["text"]))
    # print("Current list: {}".format(csv_list))
    nr_fields = len(data["0"]["fields"])
    # print("Number of fields: {}".format(nr_fields))
    for field in data["0"]["fields"]:
        
        # Is it a field for user input?
        if len(field["label"]) > 0:
            # print("Label: {}, ID: {}".format(field["label"],field["id"]))
            csv_list.append('"{}";"field";"{}";"{}"'.format(field["id"],translations["field"],field["label"]))
            for choice in field["choices"]:
                # print("Choice: {}".format(choice["text"]))
                csv_list.append('"{}";"choice";"{}";"{}"'.format(field["id"], translations["choice"],choice["text"]))
        
        # Is it a page separator with buttons?
        if field["type"] == "page":
            # print("Next Button: {}".format(field["nextButton"]["text"]))
            # print("Next Button: {}".format(field["previousButton"]["text"]))
            csv_list.append('"{}";"nextButton";"{}";"{}"'.format(field["id"],translations["nextButton"],field["nextButton"]["text"]))
            csv_list.append('"{}";"previousButton";"{}";"{}"'.format(field["id"],translations["previousButton"],field["previousButton"]["text"]))

    return csv_list



# Check command line options
nr_arguments = len(sys.argv)
print("There are {} arguments: {}".format(nr_arguments,sys.argv))

# Check the options
if nr_arguments != 4:
    print_help(sys.argv[0])

elif "import" in sys.argv:
    print("You want to import, he?")
    import_file = sys.argv[2]
    print("Import file: {}".format(import_file))
    
    # Open json file
    with open(import_file, "r") as im_file:
        data = json.load(im_file)
        csv_list = extract_json(data)
        
        # Print csv list
        for row in csv_list:
            print(row)

    # Write csv file
    csv_file = sys.argv[3]
    with open(csv_file,"w") as of_file:
        # Writing Byte Order Mark (BOM)
        of_file.write('\ufeff')
        for row in csv_list:
            of_file.write(row+"\n")
    print("CSV written.")


else:
    print(sys.argv)

