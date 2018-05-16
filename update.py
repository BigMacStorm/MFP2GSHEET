import pygsheets
import myfitnesspal
import config
from datetime import date, timedelta

gc = pygsheets.authorize()
client = myfitnesspal.Client("hellbound911@live.com")

originDate = date(2018, 5, 13)
today = date.today()

dayOffset = abs(today - originDate)

mfpData = client.get_date(today.year, today.month, today.day)
weight = client.get_measurements('Weight')
 
# update the cells
wks = gc.open_by_key('1Ld1TnVGJUkJ3VJHTvN6jlgi5-DGQJbnuxYJk3j1hZWs')
sh = wks[0]
sh.update_cell("A"+str(dayOffset.days+1), "=A"+str(dayOffset.days)+"+1")
sh.update_cell("B"+str(dayOffset.days+1), list(weight.items())[0][1])
sh.update_cell("C"+str(dayOffset.days+1), mfpData.totals.get('carbohydrates', 0))
sh.update_cell("D"+str(dayOffset.days+1), mfpData.totals.get('fat', 0))
sh.update_cell("E"+str(dayOffset.days+1), mfpData.totals.get('protein', 0))

