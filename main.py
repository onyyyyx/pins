def set_pin():
    global npin
    serial.write_line("setting pin")
    soroban.show_number(npin)
    while input.button_is_pressed(Button.AB):
        pass
    while True:
        if input.button_is_pressed(Button.AB):
            basic.clear_screen()
            return
        else:
            if input.button_is_pressed(Button.A):
                npin += 0 - 1
                soroban.show_number(npin)
                while input.button_is_pressed(Button.A):
                    pass
            if input.button_is_pressed(Button.B):
                npin += 1
                soroban.show_number(npin)
                while input.button_is_pressed(Button.B):
                    pass
    serial.write_line("pin set" + str(npin))
    while input.button_is_pressed(Button.AB):
        pass
mode = 0
npin = 0
serial.write_line("started...")

def on_forever():
    global mode
    if input.logo_is_pressed():
        mode = (mode + 1) % 1
    if input.button_is_pressed(Button.AB):
        set_pin()
basic.forever(on_forever)
