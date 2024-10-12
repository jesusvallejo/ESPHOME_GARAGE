
#ifndef CC1101TRANSCIVER_H
#define CC1101TRANSCIVER_H

#include <ELECHOUSE_CC1101_SRC_DRV.h>

#include "esphome/components/remote_transmitter/remote_transmitter.h"

#define get_cc1101(id) (*((CC1101 *)id))

class CC1101 : public PollingComponent, public Sensor
{
    int _SCK;
    int _MISO;
    int _MOSI;
    int _CSN;
    int _GDO0;
    float _FREQ;
    int _MOD;
    esphome::remote_transmitter::RemoteTransmitterComponent *_remote_transmitter;

    void setup()
    {
        pinMode(_GDO0, OUTPUT);
        ELECHOUSE_cc1101.setSpiPin(_SCK, _MISO, _MOSI, _CSN);
        ELECHOUSE_cc1101.Init();
        ELECHOUSE_cc1101.setMHZ(_FREQ);
        ELECHOUSE_cc1101.setModulation(_MOD);
        ELECHOUSE_cc1101.setCCMode(0);
        ELECHOUSE_cc1101.setPktFormat(3);
        ELECHOUSE_cc1101.SetTx();
    }

public:
    CC1101(int SCK, int MISO, int MOSI, int CSN, int GDO0, float FREQ, int MOD,
           esphome::remote_transmitter::RemoteTransmitterComponent *remote_transmitter)
        : PollingComponent(100)
    {
        _SCK = SCK;
        _MISO = MISO;
        _MOSI = MOSI;
        _CSN = CSN;
        _GDO0 = GDO0;
        _FREQ = FREQ;
        _MOD = MOD;
        _remote_transmitter = remote_transmitter;
    }

    void beginTransmission()
    {
        _remote_transmitter->setup();
    }
    void update() override {}
};

#endif