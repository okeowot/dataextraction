import re
import argparse
import urllib.request
from pypdf import PdfReader

def fetchincidents(url):
  # url = "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-23_daily_arrest_summary.pdf"
   headers = {}
   headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
   data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
   return data

def extractincidents(data):
    fixed_text = []
    with open("myfile.pdf", "wb") as f:
    	f.write(data)                   # you can use the open() function with the wb mode to open a file in binary write mode and write the contents of the file-like object to it)
    reader = PdfReader("myfile.pdf")
    number_of_pages = len(reader.pages) #get the number of pages of the PDF file.
    print("pages read")
    for page_number in range(number_of_pages - 1):   #for loop to print data on pages of PDF.
       page = reader.pages[page_number]   #reads data on each page of PDF
       page_text = page.extract_text()  #extract text from all the pages
       print(page_text)
      # if page_number == 0 and not page_text[page_number].isdigit():
       #   fixed_text.append(page_text)
       #   print(page_text)
        #  print(fixed_text)
#          print("here")
   #       continue
     #  print("continued")
     #  if page_number > 0 and page_text[page_number].isdigit():
     #       fixed_text[-1] = fixed_text[-1] + page_text.strip()
     #       print("page starts with numbers")
     #  else:
     #       fixed_text.append(page_text.strip())
     #       print("page doesn't start with numbers")
  #  fixed = '\n'.join(fixed_text)

    #   split_into_lines = page_text.splitlines() #split page_text into lines
    #  result = [] 


       # prev_was_number = False
       # if not lines[0].isdigit() and result:
        #    result[-1] += "here" + lines
        #    prev_was_number = False
       # else:
 #   print(fixed)
 #            print("SEPERATION")
#             result.append(lines)
        #     prev_was_number = True
#          print(x)
  #    print(result)
        #regex = "stop"
        #edited_lines = re.findall(regex, lines)
        #pattern = re.compile
        #regex = "stop"
        #edited_lines = re.findall(regex, line_string)
        #print(lines[0]) 
    #print(edited_lines)
#     print(edited_pages.extract_text())
# page = reader.pages[page_number]   #reads data on each page of PDF
   # page_text = page.extract_text()  #extract text from all the pages
     #  print(page_text)
      # if page_number == 0 and page_text[page_number][0].isdigit():
       #   fixed_text.append(page_text[page_number])
        #  print("here")
         # continue



 # page = reader.pages[page_number]   #reads data on each page of PDF
   # page_text = page.extract_text()  #extract text from all the pages
     #  print(page_text)
      # if page_number == 0 and page_text[page_number][0].isdigit():
       #   fixed_text.append(page_text[page_number])
        #  print("here")
         # continue
