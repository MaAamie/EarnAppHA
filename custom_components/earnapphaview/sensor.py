""" import earnapp """

from earnapp import earnapp

CONF_TOKEN = ""

""" impot HA """
#import homeassistant.helpers.config_validation as cv
#from homeassistant.components.sensor import PLATFORM_SCHEMA
#from homeassistant.const import (
#	CONF_TOKEN,
#)

""" const """

from .const import (
    DOMAIN,
    __name__,
)

""" Schema """

#PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
#    {
#        vol.Required(CONF_TOKEN): cv.string,
#    }
#)


""" Objet """

class EarnAppObject:

    def __init__(self, CONF_TOKEN):
		self.euser = earnapp.User()
		self.DataOK = self.euser.login(self.CONF_TOKEN)

	def makeinfo(self):
		if(self.DataOK):
			self.Money = self.DataOK.money()
			self.UserData = self.DataOK.userData()
			#self.Devices = self.DataOK.devices()
			self.AppVersions = self.DataOK.appVersions()
			self.PaymentMethods = self.DataOK.paymentMethods()
			self.Transactions = self.DataOK.transactions()
			#self.ShowDevice = self.DataOK.showDevice()
			print("Successfully logged in!")
		else:
			print("Failed to log in")
	
	def prints(self):
		print("---------- Money ----------")
		for cle, valeur in self.Money.items():
    		print(cle + " Valeur : " + str(valeur))

		print("---------- UserData ----------")
		for cle, valeur in self.UserData.items():
    		print(cle + " Valeur : " + str(valeur))

		print("---------- Devices ----------")
		#for cle, valeur in self.Devices.items():
		#    print(cle + " Valeur : " + str(valeur))

		print("---------- AppVersions ----------")
		for cle, valeur in self.AppVersions.items():
    		print(cle + " Valeur : " + str(valeur))

		print("---------- PaymentMethods ----------")
		for cle, valeur in self.PaymentMethods.items():
    		print(cle + " Valeur : " + str(valeur))
	
		#print("---------- Transactions ----------")
		#for cle, valeur in self.Transactions.items():
		#    print(cle + " Valeur : " + str(valeur))

		print("---------- ShowDevice ----------")
		#for cle, valeur in self.ShowDevice.items():
		#    print(cle + " Valeur : " + str(valeur))

EarnAppObject.