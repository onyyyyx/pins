def set_pin():
    global t_, npin
    serial.write_line("setting pin")
    while input.button_is_pressed(Button.AB):
        pass
    t_ = input.running_time()
    while True:
        if input.running_time() - t_ > 3:
            if Math.round(input.running_time() / 100) % 10 == 5:
                led.set_brightness(255)
                soroban.show_number(npin)
            elif Math.round(input.running_time() / 100) % 10 == 0:
                led.set_brightness(127)
                soroban.show_number(npin)
            if input.running_time() - t_ > 5:
                break
            if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                t_ = input.running_time()
        else:
            if input.button_is_pressed(Button.A):
                serial.write_line("Button A pressed")
                npin += 1
                soroban.show_number(npin)
                t_ = input.running_time()
            if input.button_is_pressed(Button.B):
                t_ = input.running_time()
                serial.write_line("Button B pressed")
                npin = 0
                soroban.show_number(npin)
mode = 0
npin = 0
t_ = 0
serial.write_line("started...")

def on_forever():
    global mode
    if input.logo_is_pressed():
        mode = (mode + 1) % 1
    if input.button_is_pressed(Button.AB):
        set_pin()
basic.forever(on_forever)
