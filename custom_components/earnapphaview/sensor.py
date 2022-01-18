""" import app """
from earnapp import earnapp
import logging
from datetime import datetime, timedelta
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
	CONF_TOKEN,
)

from .const import (
    DOMAIN,
    __name__,
)


SCAN_INTERVAL = timedelta(seconds=3600)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_TOKEN): cv.string,
    }
)


""" True Configuration """


user = earnapp.User()

if CONF_TOKEN == True:
	loggedIn = user.login(CONF_TOKEN)

if loggedIn == True:
    print("Successfully logged in!")

class EarnAppObject:
	

	DonneesMoney = user.money()
	DonneesUserData = user.userData()
	#DonneesDevices = user.devices()
	DonneesAppVersions = user.appVersions()
	DonneesPaymentMethods = user.paymentMethods()
	DonneesTransactions = user.transactions()
	#DonneesShowDevice = user.showDevice()

	print("---------- Money ----------")
	for cle, valeur in DonneesMoney.items():
    	print(cle + " Valeur : " + str(valeur))

	print("---------- UserData ----------")
	for cle, valeur in DonneesUserData.items():
    	print(cle + " Valeur : " + str(valeur))

	print("---------- Devices ----------")
	#for cle, valeur in DonneesDevices.items():
	#    print(cle + " Valeur : " + str(valeur))

	print("---------- AppVersions ----------")
	for cle, valeur in DonneesAppVersions.items():
    	print(cle + " Valeur : " + str(valeur))

	print("---------- PaymentMethods ----------")
	for cle, valeur in DonneesPaymentMethods.items():
    	print(cle + " Valeur : " + str(valeur))
	
	#print("---------- Transactions ----------")
	#for cle, valeur in DonneesTransactions.items():
	#    print(cle + " Valeur : " + str(valeur))

	print("---------- ShowDevice ----------")
	#for cle, valeur in DonneesShowDevice.items():
	#    print(cle + " Valeur : " + str(valeur))

else:
    print("Failed to log in")



