import re
import argparse
import urllib.request
from pypdf import PdfReader
import sqlite3

def fetchincidents(url):
   headers = {}
   headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
   data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
   return data

def extractincidents(data):
    with open("myfile.pdf", "wb") as f:
    	f.write(data)                   # you can use the open() function with the wb mode to open a file in binary write mode and write the contents of the file-like object to it)
    reader = PdfReader("myfile.pdf")
    number_of_pages = len(reader.pages) #get the number of pages of the PDF file.
    line_list = []
    new_list = []
    for page_number in range(number_of_pages):   #for loop to print data on pages of PDF
       page = reader.pages[page_number]   #reads data on each page of PDF
       page_text = page.extract_text()  #extract text from all the pages
       page_lines = page_text.splitlines()
       line_list.append(page_lines) #added newpages to line_list   
    line_list[0].pop(0)  #removed the date/time

    for listed_line in range(len(line_list)):
      for lines in range(len(line_list[listed_line])):
           pattern1 = r"NORMAN POLICE DEPARTMENT"
           pattern2 = r"Daily"
           if re.search(pattern1,line_list[listed_line][lines]): #fix for header
              line_fix = line_list[listed_line][lines]
              lines_fixing = re.sub(pattern1,' ',line_fix)
              line_list[listed_line][lines] = lines_fixing
           if re.search(pattern2,line_list[listed_line][lines]):   #fix for header
              line_list[listed_line].remove(line_list[listed_line][lines])
           if lines == len(line_list[listed_line]) - 1 and listed_line == len(line_list) - 1:  #fix for date and time in last line
              line_list[listed_line].remove(line_list[listed_line][lines])
#to remove line with double addresses
    for incidents in range(len(line_list) - 2 ):
       for incident_line in range(len(line_list[incidents]) - 2 ):
          pattern3 = r"^[a-zA-Z]"
          if re.search(pattern3,line_list[incidents][incident_line]):
              weird_address = line_list[incidents][incident_line]
              line_list[incidents].remove(line_list[incidents][incident_line - 1])
              line_list[incidents].remove(weird_address)
    list_strings = []
    for list in line_list:
       for item in list:
          list_strings.append(item) 
#    print(list_strings)
    return list_strings


def createdb():
  db_connect = sqlite3.connect('normanpd.db')
  db =  db_connect.cursor()
  db.execute('DROP TABLE IF EXISTS incidents')
  db.execute('CREATE TABLE incidents (incident_time TEXT, incident_number TEXT,  incident_location TEXT, nature TEXT,incident_ori TEXT)')
  db_connect.commit()
  db_connect.close()


def populatedb(incident_db, incidents):
    db_path = '/home/tolul/cs5293sp23-project0/project0/normanpd.db'
    conn_db = sqlite3.connect(db_path)
    movement = conn_db.cursor()
    pattern5 = r'^[A-Z][a-z]+(/.*)?$'
    for stringlines in incidents:
      string = stringlines.split()
      addy_string = string[3:len(string) - 1]
      incident_date_time = string[0] + " " + string[1]
      incident_number = string[2]
      incident_ori = string[-1]
      loop_once = True
      for events, types in enumerate(addy_string):
       found = re.search(pattern5, addy_string[events])   #SEARCHING FOR THE PATTERN 5 WHICH LOOKS FOR A CAPITAL LETTER FOLLOWED BY SMALL LETTER AND MAYBE THE OCCURENCE OF /
       if loop_once:
        if len(addy_string[events]) == 1 or found == None :
         continue 
        incident_address_list = addy_string[:events]
        incident_address = " ".join(incident_address_list)
        incident_ori_list = addy_string[events:]
        incident_nature = " ".join(incident_ori_list)
        loop_once = False
      incident_nature_cleanedup = incident_nature.replace("OK0140200" ,"COP DDACTS") # REMOVE ANY OCCURENCE OF THE NUMBER OK0140200 AND REPLACE IT WITH COP DDACTS
      #### THE FOLLOWING COMMANDS CONVERT THE STRINGS INTO LIST OF STRINGS
      incident_date_time_tuples = incident_date_time.strip(",").split(",")
      incident_number_tuples = incident_number.strip(",").split(",")
      incident_ori_tuples = incident_ori.strip(",").split(",")
      incident_address_tuples = incident_address.strip(",").split(",")
      incident_nature_cleanedup_tuples = incident_nature_cleanedup.strip(",").split(",")

##### THIS INSERTS THE DATA INTO DATABASE
      for x in range(len(incident_date_time_tuples)):
        movement.execute('INSERT INTO incidents (incident_time,incident_number,incident_location, nature, incident_ori) VALUES (?,?,?,?,?)', (incident_date_time_tuples[x], incident_number_tuples[x],incident_address_tuples[x],incident_nature_cleanedup_tuples[x], incident_ori_tuples[x]))
      conn_db.commit()



def status():
    db_path = '/home/tolul/cs5293sp23-project0/project0/normanpd.db'
    conn_db = sqlite3.connect(db_path)
    movement = conn_db.cursor()
    pattern = "SELECT nature, count(*) from incidents group by nature"
    stats =  movement.execute(pattern)
    rows = movement.fetchall()
    for row in rows:
       print(row[0], '|', row[1], sep = "")
