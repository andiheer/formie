import sys, json

def print_help(filename):
    """ Prints out help """
    print("Usage: filename import|export first_file second_file")


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
    csv_list = ['"ID","Type","Text"']

    # Open json file
    with open(import_file, "r") as im_file:
        data = json.load(im_file)
        print(data["0"]["title"])
        print(data["0"]["button"]["text"])
        print(data["0"]["fields"][0])
        csv_list.append('"0","button","{}"'.format(data["0"]["button"]["text"]))
        print("Current list: {}".format(csv_list))
        nr_fields = len(data["0"]["fields"])
        print("Number of fields: {}".format(nr_fields))
        for field in data["0"]["fields"]:
            
            # Is it a field for user input?
            if len(field["label"]) > 0:
                print("Label: {}, ID: {}".format(field["label"],field["id"]))
                csv_list.append('"{}","field","{}"'.format(field["id"],field["label"]))
                for choice in field["choices"]:
                    print("Choice: {}".format(choice["text"]))
                    csv_list.append('"{}","choice","{}"'.format(field["id"],choice["text"]))
            
            # Is it a page separator with buttons?
            if field["type"] == "page":
                print("Next Button: {}".format(field["nextButton"]["text"]))
                print("Next Button: {}".format(field["previousButton"]["text"]))
                csv_list.append('"{}","nextButton","{}"'.format(field["id"],field["nextButton"]["text"]))
                csv_list.append('"{}","previousButton","{}"'.format(field["id"],field["previousButton"]["text"]))

        # Print csv list
        for row in csv_list:
            print(row)


else:
    print(sys.argv)

