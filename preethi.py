
#import modules
import pandas as pd
import numpy as np
import csv
import fileinput
import re
import string
import time
import psutil

start = time.time()

#Reading the find_words.txt file
words_txt = open("find_words.txt","r")
find_words = words_txt.read()  
words_txt.close()
find_words_inlist = find_words.split()

#Reading the find_words.txt file 
frequency = {}
shakes_text = open("t8.shakespeare.txt", 'r')
text_string = shakes_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

#Reading the dictionary.csv file
with open('french_dictionary.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

#creating an english list 
tot_english = []
for word in match_pattern:
    if word in find_words_inlist :
        tot_english.append(word)
english = set(tot_english)
english = list(english)

#creating an french list 
french = []
for x in english:
    for key, value in dict_from_csv.items():
        if x in key:
            french.append(value)
            
#creating an frequency list for all words           
frequency = {}
for y in tot_english:
    count = frequency.get(y,0)
    frequency[y] = count + 1
     
frequency_list = frequency.keys()
f = []
for z in frequency_list:
    f.append(frequency[z])

#zipping to list of lists 
final = list(zip(english,french,f))

#frequency.csv  
header = ['English Word', 'French Word', 'Frequency']
with open('frequency.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)


    writer.writerow(header)
    
    for row in final:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')

#t8.shakespeare.translated.txt  
test_str = text_string
print("The original string is : " + str(test_str))
  
lookp_dict = dict_from_csv
  
temp = test_str.split()
res = []
for wrd in temp:
      
    res.append(lookp_dict.get(wrd, wrd))
      
res = ' '.join(res)

f = open("t8.shakespeare.translated.txt", "w")
f.write(str(res))
f.close()

# performance.txt 
time_taken = time.time()-start
memory_taken = psutil.cpu_percent(time_taken)
f = open("performance.txt", "w")
f.write(f'Time to process: 0 minutes {time_taken} seconds\nMemory used: {memory_taken} MB')
f.close()
