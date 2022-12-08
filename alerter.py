from checkAlertBreach import checkAlert
from alerterSend import alerterSendNetwork
from checkBreachInCelcius import checkThresholdInCelcius
from farenheitToCelcius import getCelciusFromFarenheit

# for convertion of farenheit to celcius
assert getCelciusFromFarenheit(210.2) == 99, f'convertion from farenheit to celcius failed'
# for threshold breach
assert checkThresholdInCelcius(getCelciusFromFarenheit(210.2)) == False, "99c/210.2f is below defined threshold value" 
assert checkThresholdInCelcius(getCelciusFromFarenheit(212)) == False, "100c/212f is equal to defined threshold value"
assert checkThresholdInCelcius(getCelciusFromFarenheit(213.8)) == True, "101c/213.8f is above threshold"
# for alertFailureCount
checkAlert(210.2) 
checkAlert(212) 
checkAlert(213.8) 
from checkAlertBreach import alertFailureCount
print(f'{alertFailureCount} alerts send failed.')
assert alertFailureCount == 1, f'alert fail count not incremented {alertFailureCount} times.'
assert alerterSendNetwork(213.8) != 500, f'unexpected failure code from network stub. Expected 500 for non-ok'
print("All is well!!")