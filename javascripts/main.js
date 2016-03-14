//after many failed attempts of only using one .js file, I am only using Pubnub stuff in the html doc and dealing with it
function testFunc() {
    var Text = "Literally a test";

    //Channel name for devices to receive from
    var channel = 'hello';
    // Init keys at admin.pubnub.com
    var p = PUBNUB.init({
        publish_key: 'pub-c-8f6fa682-0e7f-4766-ab33-a00525d8738b',
        subscribe_key: 'sub-c-db86ff84-e60a-11e5-a25a-02ee2ddab7fe'
    });
    // Sending data
    p.publish({
        channel: channel,
        message: Text
    });
}
