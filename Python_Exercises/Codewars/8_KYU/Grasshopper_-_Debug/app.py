def convertToCelsius(temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius

def weather_info(temp):
    c = convertToCelsius(temp)
    if (c < 0):
        return ("{c} is freezing temperature".format(c = c))
    else:
        return ("{c} is above freezing temperature".format(c = c))
