""" import app """
from earnapp import earnapp

""" import ha """
import homeassistant.helpers.config_validation as cv
#from homeassistant.components.sensor import SensorEntity
#from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)

DOMAIN = 'earnapphaview'

""" SCHEMA """

CONF_TOKEN = "token"
CONF_SCAN_INTERVAL = "scan_interval"

REQ_LOCK = threading.Lock()
CONFIG_SCHEMA = vol.Schema(
	{
		DOMAIN: Schema({
			vol.Required(CONF_TOKEN): cv.string,
			vol.Optional(CONF_SCAN_INTERVAL, default=3600): cv.positive_int,
		})
	},
	extra=vol.ALLOW_EXTRA,
)


""" True Configuration """

def setup(hass, config):
	conf = config[DOMAIN]
	comport = conf.get(CONF_TOKEN)
	comspeed = conf.get(CONF_SCAN_INTERVAL)

	rf = rcswitch.RCSwitch(comport, speed=comspeed)
	rf.libWaitForAck(True, timeout=1)

	def cleanup(event):
		rf.cleanup()

	def prepare(event):
		rf.prepare()
		rf.startReceivingThread()
		hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, cleanup)

	hass.bus.listen_once(EVENT_HOMEASSISTANT_START, prepare)
	hass.data[DOMAIN] = rf

	return True






user = earnapp.User()

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


