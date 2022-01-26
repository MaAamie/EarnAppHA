""" import """
import earnapp

import voluptuous as vol
import logging

""" import HA """
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.const import (
    CONF_NAME,
    CONF_SCAN_INTERVAL,
    CONF_TOKEN,
    ATTR_ATTRIBUTION,
    ICON,
)


""" const """
from const import (
    DOMAIN,
    __name__,
    __version__,
    UP_INTERVAL,
)


""" Schema """
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_TOKEN): cv.string,
    }
)

_LOGGER = logging.getLogger(__name__)


""" Objet """
class EarnAppObject:
    def __init__(self, token, upinterval):
        self.updatetoken(token)
        self.upinterval = UP_INTERVAL

    def update(self):
        self.dataok = self.euser.login(self.token)
        print(self.dataok)
    
    def updatetoken(self, token):
        self.token = token

    def makeinfo(self):
        self.euser = earnapp.User()
        self.update()
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

    def moneyinfo(self):
        return self.Money.get('balance')

    def moneytotalinfo(self):
        return self.Money.get('earnings_total')

    def userdatalocale(self):
        return self.UserData.get('locale')

    def userdataname(self):
        return self.UserData.get('name')

    def userdatareferralcode(self):
        return self.UserData.get('referral_code')

    def userdataemail(self):
        return self.UserData.get('email')



''' setup plaform'''
def setup_platform(hass, config, add_entities):

    name = config.get(CONF_NAME)
    update_interval = UP_INTERVAL

    try:
        token = config.get(CONF_TOKEN)
        session = []
    except :
        _LOGGER.exception("miss token")
        return False
    earnobj = EarnAppObject(token, update_interval)
    earnobj.makeinfo()
    add_entities([EarnAppSensor(session, name, update_interval, earnobj )], True)





''' Entity '''
class EarnAppSensor(Entity):
    def __init__(self, session, name, upinterval, earnobj):
        """Initialize the sensor."""
        self.session = session
        self.name = name
        self.earnobj = earnobj
        self.attributes = None
        self.state = None
        self.update = Throttle(upinterval)(self._update)

    @property
    def name(self):
        """Return sensor name """
        return "SensorEarnApp"

    @property
    def state(self):
        """Return sensor state """
        return self._state

    @property
    def unit_of_measurement(self):
        """Return money unit of measurement """
        return "$"

    def _update(self):
        """Update device state."""
        self.earnobj.makeinfo()

    @property
    def icon(self):
        """Icon to use in the frontend."""
        return ICON