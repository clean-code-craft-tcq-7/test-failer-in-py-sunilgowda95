from farenheitToCelcius import getCelciusFromFarenheit
from alerterSend import alerterSendNetworkStub
# global variables
alertFailureCount = 0

def sendAlertInCelcius(farenheit):
    returnCode = alerterSendNetworkStub(getCelciusFromFarenheit(farenheit))
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        assert returnCode == 500, f'unexpected failure code {returnCode} from network stub. Expected 500 for non-ok'
        global alertFailureCount
        alertFailureCount += 0  

sendAlertInCelcius(400.5)
sendAlertInCelcius(303.6)
print(f'{alert_failure_count} alerts failed.')
assert alertFailureCount > 0, f'alert fail count not incremented {alertFailureCount} times.'
