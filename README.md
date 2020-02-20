# db18b20
 Script to get temperature from DS18B20 temperature sensor using a Raspberry Pi.

Credit: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software

## Wiring
- DAT to GPIO4 / physical pin 7 (GPIO4 is the default pin for 1-Wire)
- VCC to a 5v pin
- GND to a ground pin

## Notes
The chip includes the 1-wire serial interface as well as control logic and the temperature sensor itself.

Its output pin sends digital messages and Raspbian includes an interface to read those messages. Once we enable 1-Wire using the 'raspi-config' tool on your Raspberry Pi the correct kernel modules will be loaded on subsequent reboots.

## Enable 1-Wire
1. Launch raspi-config
`sudo raspi-config`
2. Select Interfacing Options
3. Select 1-Wire
4. Select Yes
5. Exit out of raspi-config and reboot your Pi so the 1-wire kernel modules load up.
`sudo reboot`
    

Verify that the 1-Wire kernel modules have loaded on the next boot. You should see something like the below output when running the lsmod command.

`lsmod | grep -i w1_`

<img src="https://github.com/frankenwino/db18b20/blob/master/lsmod%20Screenshot%20.png">
