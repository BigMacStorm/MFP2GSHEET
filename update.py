import pygsheets
import myfitnesspal
import config
from datetime import date, timedelta

gc = pygsheets.authorize()
print("Google Sheets Auth successful")
client = myfitnesspal.Client(config.username, config.password)
print("MFP Auth successful")

originDate = date(2017, 9, 30)
today = date.today()

dayOffset = abs(today - originDate)
print("day offset: " + str(dayOffset.days))

mfpData = client.get_date(today.year, today.month, today.day)
weight = client.get_measurements('Weight')
 
# update the cells
wks = gc.open_by_key('1Ld1TnVGJUkJ3VJHTvN6jlgi5-DGQJbnuxYJk3j1hZWs')
sh = wks[0]
sh.update_cell("B"+str(dayOffset.days), list(weight.items())[0][1])
sh.update_cell("C"+str(dayOffset.days), mfpData.totals.get('carbohydrates', 0))
sh.update_cell("D"+str(dayOffset.days), mfpData.totals.get('fat', 0))
sh.update_cell("E"+str(dayOffset.days), mfpData.totals.get('protein', 0))

