function set_pin() {
    
    serial.writeLine("setting pin")
    soroban.showNumber(npin)
    while (input.buttonIsPressed(Button.AB)) {
        
    }
    while (true) {
        if (input.buttonIsPressed(Button.AB)) {
            basic.clearScreen()
            return
        } else {
            if (input.buttonIsPressed(Button.A)) {
                npin += 0 - 1
                soroban.showNumber(npin)
                while (input.buttonIsPressed(Button.A)) {
                    
                }
            }
            
            if (input.buttonIsPressed(Button.B)) {
                npin += 1
                soroban.showNumber(npin)
                while (input.buttonIsPressed(Button.B)) {
                    
                }
            }
            
        }
        
    }
    serial.writeLine("pin set" + ("" + npin))
    while (input.buttonIsPressed(Button.AB)) {
        
    }
}

let mode = 0
let npin = 0
serial.writeLine("started...")
basic.forever(function on_forever() {
    
    if (input.logoIsPressed()) {
        mode = (mode + 1) % 1
    }
    
    if (input.buttonIsPressed(Button.AB)) {
        set_pin()
    }
    
})
