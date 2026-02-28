# CarPi-Dashboard
cp setup_nat.sh /usr/local/bin/

cp nat-routing.service /etc/systemd/system/

cp nat_iface.conf /etc/

cp 10-network-interface-names.rules /etc/udev/rules.d/

cp .xprofile ~/

apt update
apt upgrade
apt full-upgrade
apt update
apt upgrade
apt full-upgrade
apt install vlc python3-vlc python3-pyqt5 python3-pyqt5.qtwebengine python3-full hostapd dnsmasq network-manager iptables libvlc-dev rtl-sdr gpsd python3-musicbrainzngs libdvd-pkg
sudo dpkg-reconfigure libdvd-pkg speech-dispatcher
