import re
import matplotlib.pyplot as plt

fname = "mbox.txt"
fhand = open(fname)

days = []
months = []

for line in fhand:
	line = line.rstrip()
	email = re.search('^From\\s+\\S+\\s+(\\w{3})\\s+(\\w{3})', line)
	if email:
		day = email.group(1)
		month = email.group(2)
		days.append(day)
		months.append(month)

plt.figure()
plt.hist(months, bins = 12, color = 'skyblue', edgecolor = 'black')
plt.xlabel('Name of Month')
plt.ylabel('Number of Emails')
plt.title('Number of Emails Sent by Each Month')
plt.savefig('month_histogram.png', dpi = 200)
plt.show()

plt.hist(days, bins = 7, color = 'orange', edgecolor = 'black')
plt.xlabel('Days of the Week')
plt.ylabel('Number of Emails')
plt.title('Number of Emails Sent by Each Day')
plt.savefig('day_histogram.png', dpi = 200)
plt.show()
