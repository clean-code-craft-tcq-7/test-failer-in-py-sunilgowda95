from alerterInCelcius import sendAlertInCelcius, alertFailureCount

sendAlertInCelcius(400.5)# alert_in_celcius(400.5)
sendAlertInCelcius(303.6)# alert_in_celcius(303.6)
print(f'{alertFailureCount} alerts failed.')
