import pygsheets
import myfitnesspal
from datetime import date, timedelta

gc = pygsheets.authorize()
print "Google Sheets Auth sucessful"
client = myfitnesspal.Client('hellbound911@live.com')
print "MFP Auth sucessful"

originDate = date(2017, 1, 17)
today = date.today()

dayOffset = abs(today - originDate)
print "day offset: " + str(dayOffset.days)

#grab mfp data for yesterday
yesterday = date.today() - timedelta(days=1)
mfpData = client.get_date(yesterday.year, yesterday.month, yesterday.day)
weight = client.get_measurements('Weight')
 
#update the cells
wks = gc.open_by_key('1Ld1TnVGJUkJ3VJHTvN6jlgi5-DGQJbnuxYJk3j1hZWs')
sh = wks[0]
sh.update_cell("B"+str(1+dayOffset.days), weight.items()[0][1])
sh.update_cell("C"+str(1+dayOffset.days), mfpData.totals['carbohydrates'])
sh.update_cell("D"+str(1+dayOffset.days), mfpData.totals['fat'])
sh.update_cell("E"+str(1+dayOffset.days), mfpData.totals['protein'])

