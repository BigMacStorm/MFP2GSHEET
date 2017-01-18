import pygsheets
import myfitnesspal
from datetime import date

gc = pygsheets.authorize()
client = myfitnesspal.Client('hellbound911@live.com')

originDate = date(2017, 1, 17)
today = date.today()

dayOffset = today - originDate
print "day offset: " + dayOffset