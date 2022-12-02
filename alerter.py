from farenheitToCelcius import getCelciusFromFarenheit
from alerterSend import alerterSendNetworkStub
from checkBreachInCelcius import checkThresholdInCelcius
# global variables
alertFailureCount = 0

# def sendAlertInCelcius(farenheit):
def checkAlert(farenheit):
    celcius = getCelciusFromFarenheit(farenheit)
    if checkThresholdInCelcius(celcius):
        returnCode = alerterSendNetworkStub(celcius)
        if returnCode != 200:
            # non-ok response is not an error! Issues happen in life!,  let us keep a count of failures to report
            # However, this code doesn't count failures!, Add a test below to catch this bug. Alter the stub above, if needed.
            assert returnCode == 500, f'unexpected failure code {returnCode} from network stub. Expected 500 for non-ok'
            global alertFailureCount
            alertFailureCount += 0  
# for convertion of farenheit to celcius
assert getCelciusFromFarenheit(210.2) == 99, f'convertion from farenheit to celcius failed'
# for threshold breach
assert checkThresholdInCelcius(getCelciusFromFarenheit(210.2)) == False, "99c/210.2f is below defined threshold" 
assert checkThresholdInCelcius(getCelciusFromFarenheit(212)) == False, "100c/212f is below defined threshold"
assert checkThresholdInCelcius(getCelciusFromFarenheit(213.8)) == True, "101c/213.8f is above threshold"
# for alertFailureCount
checkAlert(210.2) 
checkAlert(212) 
checkAlert(213.8) 
print(f'{alertFailureCount} alerts failed.')
assert alertFailureCount > 0, f'alert fail count not incremented {alertFailureCount} times.'
