# Hacking Lab KRACK attack on Mininet-Wifi

## Installation guide for KALI:

1. Download "Mininet-Wifi" as described in README
2. Open installation script: `vim util/install.sh`
3. Replace 'Debian' with 'Kali': `:%s/Debian/Kali/g`
4. Save and exit: `:write` , `:quit`
5. Continue installation (including option `-l` to get 'wmediumd'): `sudo util/install.sh -Wnfvl`
6. Start Openvswitch service: `sudo service openvswitch-switch start`
6. Test correct installation: `sudo mn --test pingall`

## Init network & testing vulnerability

Short video available at: https://www.youtube.com/watch?v=aA4notyZph0

1. Run script: `sudo python krack-mininet-wifi.py`
2. Open console for sta1: `xterm sta1 sta1`
3. Run test: `sta1 ./krack.py wpa_supplicant -Dnl80211 -i sta1-wlan0 -c sta1_0.staconf`
4. Open WPA client in first sta1 console: `wpa_cli`
5. Ping AP from second sta1 console: `ping 10.0.0.101`
6. Print infos on first sta1 console: `status` , `scan_results`
7. Associate with another AP: `roam 02:00:00:00:00:01`
8. Observe results of connected sta1 which can now ping and shows vulnerability in main console
