from farenheitToCelcius import getCelciusFromFarenheit

#global varibles
ALERT_TEMPERATURE_THRESHOLD_CELCIUS = 100

def checkThresholdInCelcius(celcius):
    print("checThresholdInCelcius : ",celcius)
    return celcius > ALERT_TEMPERATURE_THRESHOLD_CELCIUS