#!/usr/bin/python3
import os

import requests

###################################
## Datei holen und herunterladen ##
###################################

url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Fallzahlen_Kum_Tab.xlsx?__blob=publicationFile'
r = requests.get(url, allow_redirects=True)


with open('Fallzahlen_Kum_Tab.xlsx', 'wb') as f:
    os.chmod("Fallzahlen_Kum_Tab.xlsx", 436)
    f.write(r.content)
    f.close()

###########################################################
## Das Lesen von Excel-Dateie wird mit PHP programmiert  ##
###########################################################

# path = "Fallzahlen_Kum_Tab.xlsx"
# wb_obj = openpyxl.load_workbook(path)

# Read the active sheet:
#sheet = wb_obj["LK_7-Tage-Fallzahlen"]

#objects = []
#for x in xrange(4, 172):
#    cell_value = sheet.cell(5,x)
#    #print(str(x) + " -- " + str(5))
#    if(cell_value.value is not None):
#        #print(cell_value.value)
#        objects.append(cell_value.value)

#performance = []
#for x in xrange(1, 172):
#    cell_value = sheet.cell(205,x)
#    print(str(205)  + " -- " + str(x))
#    if(cell_value.value is not None):
#        print(cell_value.value)
#        performance.append(cell_value.value)


#os.remove("Fallzahlen_Kum_Tab.xlsx")


# y_pos = np.arange(len(objects))

#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
#
# plt.show()
