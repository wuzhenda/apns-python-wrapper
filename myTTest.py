#encode:utf-8
import APNSWrapper
import binascii

user_tokenstr='a923791bd5b4e1e0fa8456dc9205553e4805f5aa9eb5d7cc7e8dbb179308f0b2'
user_pem='push_cert.pem'
deviceToken = binascii.unhexlify(user_tokenstr)

# create wrapper
wrapper = APNSWrapper.APNSNotificationWrapper(user_pem, True)

# create message
message = APNSWrapper.APNSNotification()
message.token(deviceToken)
message.badge(5)
message.alert("hellowrold 234234")

# add message to tuple and send it to APNS server
wrapper.append(message)
wrapper.notify()
