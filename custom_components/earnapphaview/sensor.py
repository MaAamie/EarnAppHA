""" import app """
from earnapp import earnapp

""" import ha """
#from homeassistant.components.sensor import SensorEntity
#from homeassistant.components.sensor import PLATFORM_SCHEMA

DOMAIN = 'earnapphaview'


user = earnapp.User()
print(user)

loggedIn = user.login("")

if loggedIn == True:
    print("Successfully logged in!")
else:
    print("Failed to log in")

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


