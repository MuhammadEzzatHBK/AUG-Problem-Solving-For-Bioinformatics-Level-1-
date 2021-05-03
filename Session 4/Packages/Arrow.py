import arrow

print('Egypt: ', arrow.now()) #Time of Egypt +02:00
print('Greenwich: ', arrow.utcnow(), '\n') #Greenwich Time +00:00

print(arrow.now().ctime()) #Date & Time
print('Date is: ', arrow.now().date()) #Date only
print('Day number: (', arrow.now().isoweekday(), ') in the week\n') #Number of Today in Week

print('Hour ago: ', arrow.now().shift(hours = -1)) #Time from an hour ago