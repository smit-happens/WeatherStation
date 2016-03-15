//Channel name for devices to receive from
var channel1 = 'weather';
var channel2 = 'command';

// Init keys at admin.pubnub.com
var pubnub = PUBNUB.init({
    publish_key: 'pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b',
    subscribe_key: 'sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe'
});

pubnub.subscribe({
    channel: channel1,
    callback: receive //WHY THE FUCK DOES THE FUCKING FUNCTION HAVE TO FUCKING BE CALLED IN THIS BACKWARDS ASS WAY FUCK
});

pubnub.subscribe({
    channel: channel2,
    message: receive
});

function receive(txt, channel) {
    var output = document.getElementById("channelOutput");

    if(channel.indexOf("weather") != -1) {
        output.value += "[ weather ]: " + txt + "\n";
    }
    else if(channel.indexOf("command") != -1) {
        output.value += "[command]: " + txt + "\n";
    }

    output.scrollTop = output.scrollHeight;
}

function sendMessage(channel) {
    // Sending data
    var messageInput = document.getElementById("messageInput");
    var text = messageInput.value;

    pubnub.publish({
        channel: channel,
        message: text
    });

    document.getElementById("messageInput").value = "";
}

function sayHi(){
    var txtName = document.getElementById("txtName");
    var txtOutput = document.getElementById("txtOutput");
    var name = txtName.value;
    txtOutput.value = "Hi there, " + name + "!"
}