function set_pin() {
    
    serial.writeLine("setting pin")
    while (input.buttonIsPressed(Button.AB)) {
        
    }
    t_ = input.runningTime()
    while (true) {
        if (input.runningTime() - t_ > 3) {
            if (Math.round(input.runningTime() / 100) % 10 == 5) {
                led.setBrightness(255)
                soroban.showNumber(npin)
            } else if (Math.round(input.runningTime() / 100) % 10 == 0) {
                led.setBrightness(127)
                soroban.showNumber(npin)
            }
            
            if (input.runningTime() - t_ > 5) {
                break
            }
            
            if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
                t_ = input.runningTime()
            }
            
        } else {
            if (input.buttonIsPressed(Button.A)) {
                serial.writeLine("Button A pressed")
                npin += 1
                soroban.showNumber(npin)
                t_ = input.runningTime()
            }
            
            if (input.buttonIsPressed(Button.B)) {
                t_ = input.runningTime()
                serial.writeLine("Button B pressed")
                npin = 0
                soroban.showNumber(npin)
            }
            
        }
        
    }
}

let mode = 0
let npin = 0
let t_ = 0
serial.writeLine("started...")
basic.forever(function on_forever() {
    
    if (input.logoIsPressed()) {
        mode = (mode + 1) % 1
    }
    
    if (input.buttonIsPressed(Button.AB)) {
        set_pin()
    }
    
})
