from farenheitToCelcius import getCelciusFromFarenheit
from checkBreachInCelcius import checkThresholdInCelcius
from alerterSend import alerterSendNetwork
# global variables
alertFailureCount = 0

def convertCheckAlert(farenheit):
    celcius = getCelciusFromFarenheit(farenheit)
    if checkThresholdInCelcius(celcius):
        return True, celcius
    return False, celcius

def checkAlert(farenheit):
    breached, celcius = convertCheckAlert(farenheit)
    if breached:
        returnCode = alerterSendNetwork(celcius)
        if returnCode != 200:
            global alertFailureCount
            alertFailureCount += 1 
            print("alertFailureCount : ", alertFailureCount)