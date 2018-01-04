# Hacking Lab KRACK attack on Mininet-Wifi

## Installation guide for KALI:

1. Download our version of "Mininet-Wifi" on Github: `git clone https://github.com/abiri/mininet-wifi`
2. Continue installation (including option `-l` to get 'wmediumd'): `sudo util/install.sh -Wnfvl`
3. Start Openvswitch service: `sudo service openvswitch-switch start`
4. Test correct installation: `sudo mn --test pingall`

## Switch WPA Supplicant Version
(started with clean VM)
1. `sudo gpt-get install get`
2. `git clone https://github.com/intrig-unicamp/mininet-wifi`
3. `cd mininet-wifi`
4. Replace Debian with Kali
5. `vim util/install.sh`
6. search for wpa_supplicant
  `/wpa_supplicant`
  and comment out 2 times the 3 lines from 
  `pushd' to 'sudo make && make install`
 save with
 `:wq`
7. download old wpa_supplicant from `ww.w1.fi/releases`
8. run install script: `sudo util/install.sh -WnfvL`
9. Replace all files in `mininet-wifi/hostap` with the folders fromthe old wpa_supplicant
10. go to hostap folder: `cd hostap/wpa_supplicant`
11. `cp defconfig .config`
12. `sudo make && make install`

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

### Observe traffic

Before reading traffic with wireshar, start the default interface **hwsim0** as described in the manual (p. 31):

`mininet-wifi> sh ifconfig hwsim0 up`
