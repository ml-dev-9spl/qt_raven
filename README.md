# QtRaven


## PyQt5 Installation

```bash
sudo apt-get update
sudo apt-get install qt5-default
sudo apt-get install sip-dev

cd /usr/src
sudo wget https://www.riverbankcomputing.com/static/Downloads/sip/4.19.21/sip-4.19.21.tar.gz
sudo tar xzf sip-4.19.21.tar.gz
cd sip-4.19.21
sudo python3 configure.py --sip-module PyQt5.sip
sudo make -j 4
sudo make install

cd /usr/src
sudo wget https://www.riverbankcomputing.com/static/Downloads/PyQt5/5.13.2/PyQt5-5.13.2.tar.gz
sudo tar xzf PyQt5-5.13.2.tar.gz 
cd PyQt5-5.13.2/
sudo python3 configure.py
sudo make -j 4
sudo make install
```

## OpenCV Installation

```bash
pip install opencv-contrib-python==4.1.0.25
```

## RFID Pin Configuration

```
+-----------+--------+---------+---------------+
| RC522 Pin | Color  | Pi3/Pi4 | GPIO Pi3      |
+-----------+--------+---------+---------------+
| 3.3V      | Blue   | 1/1     | 3.3V          |
+-----------+--------+---------+---------------+
| RST       | Yellow | 22/21   | GPIO25        |
+-----------+--------+---------+---------------+
| GND       | Orange | 6/9     | GND           |
+-----------+--------+---------+---------------+
| IRQ       | Green  | NA      | NA            |
+-----------+--------+---------+---------------+
| MISO      | Red    | 21/35   | GPIO9         |
+-----------+--------+---------+---------------+
| MOSI      | Brown  | 19/38   | GPIO11        |
+-----------+--------+---------+---------------+
| SCK       | Black  | 23/40   | GPIO11        |
+-----------+--------+---------+---------------+
| SDA       | White  | 24/36   | GPIO8         |
+-----------+--------+---------+---------------+
```

## RFID Pin Configuration in Pi4 B Model

#### Change bus and device value in MFRC522.py file as below
```
def __init__(self, bus=1, device=2, spd=1000000, pin_mode=10, pin_rst=-1, debugLevel='WARNING'):
```

#### Append following lines in /boot/config.txt file

```
dtoverlay=spi1-1cs
dtoverlay=spi1-2cs
dtoverlay=spi1-3cs
```

Above code will enable LCD touch configuration and RFID both
