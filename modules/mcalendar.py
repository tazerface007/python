from  calendar import Calendar

cal = Calendar()

iterator = cal.iterweekdays()

for i in iterator:
    print(i, end='')

print()
print(cal.getfirstweekday())

from calendar import HTMLCalendar
htmlcal = HTMLCalendar() 

html_output = htmlcal.formatmonth(2026,5)

print(html_output)
