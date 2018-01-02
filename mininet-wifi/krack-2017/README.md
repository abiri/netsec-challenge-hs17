# Hacking Lab KRACK attack on Mininet-Wifi

## Installation guide for KALI:

1. Download our version of "Mininet-Wifi" on Github: `git clone https://github.com/abiri/mininet-wifi`
2. Continue installation (including option `-l` to get 'wmediumd'): `sudo util/install.sh -Wnfvl`
3. Start Openvswitch service: `sudo service openvswitch-switch start`
4. Test correct installation: `sudo mn --test pingall`

## Init network & testing vulnerability

Short video available at: https://www.youtube.com/watch?v=aA4notyZph0

1. Download our attack scripts: `git clone https://github.com/abiri/netsec-challenge-hs17`
2. Run script: `sudo python krack-mininet-wifi.py`
3. Open console for sta1: `xterm sta1 sta1`
4. Run test: `sta1 ./krack.py wpa_supplicant -Dnl80211 -i sta1-wlan0 -c sta1_0.staconf`
5. Open WPA client in first sta1 console: `wpa_cli`
6. Ping AP from second sta1 console: `ping 10.0.0.101`
7. Print infos on first sta1 console: `status` , `scan_results`
8. Associate with another AP: `roam 02:00:00:00:00:01`
9. Observe results of connected sta1 which can now ping and shows vulnerability in main console
