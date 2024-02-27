# Initialisation des variables
pin_mode = "read"  # Mode initial
selected_pin = 0   # Pin initial sélectionné
pin_value = 0      # Valeur initiale du pin

# Boucle principale
while True:
    # Mode de lecture
    if pin_mode == "read":
        pin_value = eval('pins.digital_read_pin(Digital.P%s)'%selected_pin)
        display.show(str(pin_value))
        sleep(1000)
    
    # Mode de configuration
    elif pin_mode == "set":
        display.show(str(selected_pin))
        if button_a.was_pressed():
            selected_pin -= 1
            if selected_pin < 0:
                selected_pin = 1
            display.show(str(selected_pin))
            sleep(500)
        elif button_b.was_pressed():
            selected_pin += 1
            if selected_pin > 1:
                selected_pin = 0
            display.show(str(selected_pin))
            sleep(500)
        elif button_a.is_pressed() and button_b.is_pressed():
            pin_mode = "read"
            sleep(500)
    
    # Délai pour éviter les rebonds des boutons
    sleep(20)
