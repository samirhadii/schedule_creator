from restaurants import get_restaurants
from bars import get_bars
from shopping_malls import get_shopping
import random


def set_schedule(coordinates, desired_price, radius):
    schedule = {"11:00 AM": "", "12:00 PM": "", "1:00 PM": "", "2:00 PM": "",
                "3:00 PM": "", "4:00 PM": "", "5:00 PM": "", "6:00 PM": "", "8:00 PM": ""}

    restaurant = random.choice(get_restaurants(
        coordinates, desired_price, radius))
    shopping = random.choice(get_shopping(coordinates, radius))
    bar = random.choice(get_bars(coordinates, desired_price, radius))

    #get random lunch time from list
    lunch = ["11:00 AM", "12:00 PM", "1:00PM"]
    lunchtime = random.choice(lunch)
    schedule[lunchtime] = restaurant

    #get random midday time from list
    midday = ["2:00 PM ", "3:00 PM", "4:00 PM"]
    midday_time = random.choice(midday)
    schedule[midday_time] = shopping

    #get random night time from list
    night = ["6:00 PM ", "7:00 PM", "8:00 PM"]
    night_time = random.choice(night)
    schedule[night_time] = bar

    return schedule



#print(set_schedule("33.952095,-83.375293", 2, 5000))
