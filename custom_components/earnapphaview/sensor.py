""" import earnapp """

import earnapp

toke = ''

""" import HA """
#import homeassistant.helpers.config_validation as cv
#from homeassistant.components.sensor import PLATFORM_SCHEMA
#from homeassistant.const import (
#	CONF_TOKEN,
#)

""" const """

from const import (
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
    def __init__(self):
        self.euser = earnapp.User()

    def updatetoken(self, token):
        self.dataok = self.euser.login(token)
        print(self.dataok)

    def makeinfo(self):
        if(self.dataok):
            self.Money = self.euser.money()
            self.UserData = self.euser.userData()
            self.Devices = self.euser.devices()
            self.AppVersions = self.euser.appVersions()
            self.PaymentMethods = self.euser.paymentMethods()
            self.Transactions = self.euser.transactions()
            #self.ShowDevice = self.euser.showDevice()
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
        print(self.Devices)
        #for cle, valeur in self.Devices:
        #    print(cle + " Valeur : " + str(valeur))

        print("---------- AppVersions ----------")
        for cle, valeur in self.AppVersions.items():
            print(cle + " Valeur : " + str(valeur))

        print("---------- PaymentMethods ----------")
        for cle, valeur in self.PaymentMethods.items():
            print(cle + " Valeur : " + str(valeur))
    
        print("---------- Transactions ----------")
        print(self.Transactions)

        print("---------- ShowDevice ----------")
        #print(self.ShowDevice())
        #for cle, valeur in self.ShowDevice.items():
        #    print(cle + " Valeur : " + str(valeur))




earnobj = EarnAppObject()

earnobj.updatetoken(toke)

earnobj.makeinfo()

earnobj.prints()
