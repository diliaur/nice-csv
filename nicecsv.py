# make CSVs with large text strings into a nice human-readable file
# separate by comma, each entry separated by newline

# TO USE
#	Open terminal in directory program is stored.
#	Type: "python nicecsv.py [fileToParse.csv]" and hit enter.
#   nicecsv.py will create a file with the HTML formatted results: "csvResult.html"

import sys
import csv
import datetime

print "file to parse:",str(sys.argv[1]) # program name is argv[0]
newFile = open("csvResult.html","w")

# set up the new HTML file
beginHTML = "<html><head><title>CSV output</title></head><body>"
newFile.write(beginHTML)

with open(sys.argv[1],'rb') as csvFile:
	reader = csv.reader(csvFile, delimiter=',', quotechar='"')
	header = reader.next()
	#print header
	#print "---"
	for row in reader:
		#print row
		rowMax = len(row)
		for item in range(0,rowMax):
			#print "<p>"
			#print "<b>",header[item],"</b>"
			#print row[item]
			#print "<br />"
			#print "</p>"
			frankenRow = "<p><b>" + header[item] + "<br /></b>" + row[item] + "<br /></p>"
			#print frankenRow
			newFile.write(frankenRow)
		#end
		newFile.write("<hr>")
	#end
#end

#close out the document
endHTML = "</body></html>"
newFile.write(endHTML)

newFile.close() #close the file to finish writing
print "done"