//Channel name for devices to receive from
var channel = 'hello';
// Init keys at admin.pubnub.com
var pubnub = PUBNUB.init({
    publish_key: 'pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b',
    subscribe_key: 'sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe'
});

pubnub.subscribe({
    channel: channel,
    message: receive //WHY THE FUCK DOES THE FUCKING FUNCTION HAVE TO FUCKING BE CALLED IN THIS BACKWARDS ASS WAY FUCK
});

function receive(txt) {
    var text = txt.toString();
    //var channelText = channel.toString();
    document.getElementById("channelOutput").value += "[" + channel + "]: " + text + "\n";
}

function sendMessage() {
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