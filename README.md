# ESPHOME_GARAGE
Show case to emulate a Clemsa MV12 remote via ESPHOME

Compatibility:
It only works with ESP32 and CC1101 transceiver.
How to compile:
On home assistant add the file editor and the ESPHome add-on.
Using the file editor addon, add the cc1101.h file to the /homeassistant/esphome/cc1101.h directory.
Add a new device with the provided yaml as a guide/template using the ESPHome add-on.
Garage raw signal:
You will need to know the signal of your garage remote/receiver. The timmings of the signal, the modulation, etc. I recommend using URH https://github.com/jopohl/urh to decode the signal.
The garage has to have a static code ( not the safest ).
Multiple switches could be added in case your remote has multiple( and in use) buttons.
You could record the signal using URH and an inexpensive sdr-rtl, and use the provided python encode script to encode the signal for ESPHOME.

