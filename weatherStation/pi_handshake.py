<<<<<<< HEAD
#!/usr/bin/python
=======
#!/usr/bin/env python
>>>>>>> f725b4180361e48e17b0b6ba589de21cd5f9198a

from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

message = ""

while message != "%exit":
    channel = "hello"
    message = raw_input("Enter a message to send: ")

    pubnub.publish(
        channel = channel,
        message = message)

