#!/usr/bin/env python


from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b",
                subscribe_key="sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe")

channel = "hello"
message = "Literally testing please work"

pubnub.publish(
    channel = channel,
    message = message)
