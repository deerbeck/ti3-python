# task 1 anagram
# open textfile with contextmanager

with open("anagram.txt", "r") as infile, open("anagram_output.txt", "w") as outfile:
    #read every line and comprehend a list from it 
    words = infile.read().splitlines()

    #create lists for easier readability and later filter case
    anagram_list = []
    filter_list = []

    for word in words:
        count = 0
        #add first found word of anagrams to the filter list
        if sorted(word) not in map(lambda x: sorted(x),filter_list):
            filter_list.append(word)
        for element in words:
            if sorted(word) == sorted(element):
                count += 1

        anagram_list.append((word,count))

    #filter the whole anagram list to only save the first appearence of the anagram
    for w,c in filter(lambda x:x[0] in filter_list ,anagram_list):
        outfile.write(f"{w};{c}\n")
    
    