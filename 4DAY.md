# Day 4 - Python Modules and `pip`
Language popularity is strongly correlated to **batteries included** and **package management**.

### Batteries Included
Almost anything you need, in order to be productive is included in the standard library.
---
https://stackoverflow.com/questions/32917376/parsing-a-csv-file-in-python-and-saving-to-a-dictionary-which-is-in-turn-saved-t/32917811#32917811

My task is to read the input `DATAFILE`, line by line, and for the first **4 lines** (not including the header) split each line on **","** and then for each line, create a **dictionary** where the **key** is the header title of the field, and the **value** is the value of that field in the row.

The function parse_file() should return a list of dictionaries, each data line in the file being a single list entry.

Field names and values should not contain extra whitespace, like spaces or newline characters.

My question is this program generates **data(list)** that has the same value in all its list entries that is the last line of the csv file.


movie                            |   director               |   time_min
---------------------------------|--------------------------|-----------
Marvin's Room                    |   Jerry Zaks             |   98      
Tucker and Dale vs Evil          |   Eli Craig              |   89      
Quills                           |   Philip Kaufman         |   124     
The Man from Earth               |   Richard Schenkman      |   87      
The Quest                        |   Jean-Claude Van Damme  |   95      
The Nine Lives of Fritz the Cat  |   Robert Taylor          |   77      
```python
#!/usr/bin/env python

import csv

def parse_file(DATAFILE, lines):
    file_descriptor = open(DATAFILE, 'r') # open the file and read from it
    data = csv.reader(file_descriptor)    # treat file like csv
    header = next(data)                   # extract csv header
    return_collection = list() # create empty return list, to be added to

    for line_number, row in enumerate(data):
        if (line_number >= lines):
            break  # restricts number of lines

        d = dict() # every element in list should be a dictionary
        for index, key in enumerate(row):
            d[header[index]] = key  # assign 'key' 'value' mapping

        return_collection.append(d) # add dictionary to list

    file_descriptor.close() # close file when you are done with it
    return return_collection

list_of_dictionaries = parse_file('./example-files/movies.csv', 4)
for dictionary in list_of_dictionaries:
    for key in dictionary:
        print(key, ':', dictionary[key], end='\t\t')
    print(end='\n')
```
### Package Management
Anything you need that isn't provided, is easy to get. `pip` interfaces with the python package index to gain you access to user developed libraries.
---
```bash
$ pip install --user pillow
```
```python
#!/usr/bin/env python

from PIL import Image

filename = './example-files/lena_color.gif'
image = Image.open(filename)

outname, ext = filename.rsplit('.', 1)
size = (128, 128)
image.thumbnail(size)
image.save(outname + '.thumbnail.' + ext)
```
