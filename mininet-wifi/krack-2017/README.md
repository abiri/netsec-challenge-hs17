Short video available at: https://www.youtube.com/watch?v=aA4notyZph0

Installation guide for KALI:

1. Install "Mininet-Wifi" as described in README
2. Open installation script: `vim util/install.sh`
3. Replace 'Debian' with 'Kali': `:%s/Debian/Kali/g`
4. Save and exit: `:write` , `:quit`
5. Continue installation: `sudo util/install.sh -Wnfv`
6. Start Openvswitch service: `sudo service openvswitch-switch start`
6. Test correct installation: `sudo mn --test pingall`
