input.onButtonPressed(Button.A, function () {
    radio.setGroup(5)
    radio.sendString("HOLA")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
