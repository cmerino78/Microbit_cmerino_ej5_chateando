def on_button_pressed_a():
    radio.set_group(5)
    radio.send_string("HOLA")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)
