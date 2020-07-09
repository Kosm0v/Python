from math import floor
def duty_free(price, discount, holiday_cost):
  return floor(holiday_cost/(price*discount/100))