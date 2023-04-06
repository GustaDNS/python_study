from datetime import datetime, timedelta

today = datetime.now()
#print('Today is: ' + str(today))

#one_day = timedelta(days = 1)
#yesterday = today - one_day
#print('Yesterday was: ' + str(yesterday))

#one_week = timedelta(weeks = 1)
#last_week = today - one_week
#print('One week ago was: ' + str(last_week))


print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))
print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))


birthday = input('When is your bithday? (dd/mm/yyyy)')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print ('Birthday: ' + str(birthday_date))
one_day = timedelta(days=1)
birthday_eve =  birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))