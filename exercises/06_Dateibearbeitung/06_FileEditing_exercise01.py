with open("bookstore.xml", "r") as xml_file:
    all_lines = xml_file.readlines()
    books = []
    book = False
    for line in all_lines:
        if "<book>" in line:
            book = True
            d1 = dict()
        if book:
            if "<title>" in line:
                start = line.find("<title>") + len("<title>")
                end = line.find("</title>")
                d1["title"] = line[start:end]
            elif "<author>" in line:
                start = line.find("<author>") + len("<author>")
                end = line.find("</author>")
                d1["author"] = line[start:end]
            elif "<year>" in line:
                start = line.find("<year>") + len("<year>")
                end = line.find("</year>")
                d1["year"] = line[start:end]
            elif "<price>" in line:
                start = line.find("<price>") + len("<price>")
                end = line.find("</price>")
                d1["price"] = line[start:end]
        if "</book>" in line:
            book = False
            books.append(d1)

    with open("bookstore.json", "w+") as json_file:
        json_file.write("{\n")
        json_file.write('   "books": [\n')
        json_file.write("       {\n")
        test = books[0].keys()
        
        json_file.write(f'        "{list(books[0].keys())[0]}": "{books[0]["title"]}",\n        "{list(books[0].keys())[1]}": "{books[0]["author"]}",\n        "{list(books[0].keys())[2]}": "{books[0]["year"]}",\n        "{list(books[0].keys())[3]}": "{books[0]["price"]}"\n')
        json_file.write("       },\n")
        json_file.write("       {\n")
        json_file.write(f'        "{list(books[1].keys())[0]}": "{books[1]["title"]}",\n        "{list(books[1].keys())[1]}": "{books[1]["author"]}",\n        "{list(books[1].keys())[2]}": "{books[1]["year"]}",\n        "{list(books[1].keys())[3]}": "{books[1]["price"]}"\n')
        json_file.write("       }\n")
        json_file.write("   ]\n") 
        json_file.write("}\n")

    pass
