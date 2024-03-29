#!/usr/bin/env python2.6
#
#  tests.py
#  wrapper
#
#  Created by max klymyshyn on 11/15/09.
#  Copyright (c) 2009 Sonettic. All rights reserved.
#

from APNSWrapper import *

def badge(wrapper, token):
    message = APNSNotification()
    message.tokenBase64(token)
    
    message.badge(3)
    print message._build()
    wrapper.append(message)
    
def sound(wrapper, token):
    message = APNSNotification()
    message.tokenBase64(token)
    
    message.sound("default")
    print message._build()
    wrapper.append(message)
    

def alert(wrapper, token):
    message = APNSNotification()
    message.tokenBase64(token)
    
    alert = APNSAlert()
    alert.body("Very important alert message")
    
    alert.loc_key("ALERTMSG")
    
    alert.loc_args(["arg1", "arg2"])
    alert.action_loc_key("OPEN")
    
    message.alert(alert)
    
    # properties wrapper
    property = APNSProperty("acme", (1, "custom string argument"))    
    message.appendProperty(property)

    print message._build()
    wrapper.append(message)
   

def testAPNSWrapper():
    user_tokenstr='a923791bd5b4e1e0fa8456dc9205553e4805f5aa9eb5d7cc7e8dbb179308f0b2'
    deviceToken = binascii.unhexlify(user_tokenstr)
    user_pem='push_cert.pem'

    cert_path = user_pem
    
    """
    Method to testing apns-wrapper module.
    """

    encoded_token = deviceToken

    wrapper = APNSNotificationWrapper(cert_path, \
                sandbox = True, force_ssl_command = False)
    
    badge(wrapper, encoded_token)

    sound(wrapper, encoded_token)

    alert(wrapper, encoded_token)
            
    
    wrapper.notify()


    feedback = APNSFeedbackWrapper(cert_path, sandbox = True)
    feedback.receive()
    
    print "\n".join(["> " + base64.standard_b64encode(y) for x, y in feedback])
    

    
if __name__ == "__main__":
    testAPNSWrapper()
