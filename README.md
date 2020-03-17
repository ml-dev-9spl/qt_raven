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
