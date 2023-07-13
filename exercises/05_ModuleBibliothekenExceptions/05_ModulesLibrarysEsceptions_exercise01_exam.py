# task 1 anagram
# open textfile with contextmanager
import os
path = os.path.dirname(os.path.realpath(__file__))

with open(path+"\\anagram.txt", "r") as infile, open(path +"\\anagram_output.txt", "w") as outfile:
    words = infile.readlines()
    words = [w.rstrip() for w in words]
    ana_dict = dict()

    for word in words:
        wordflag = True
        for key in ana_dict.keys():
            if sorted(list(key)) == sorted(list(word)):
                ana_dict[key] +=1
                wordflag = False
        if wordflag:
            ana_dict[word] = 1
    
    for k,v in ana_dict.items():
        outfile.write(f"{k};{v}\n")

            
            