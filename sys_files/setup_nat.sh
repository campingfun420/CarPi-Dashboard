#!/bin/bash

CONFIG_FILE="/etc/nat_iface.conf"
DEFAULT_IFACE="wlan1"

# Use configured interface or default
if [ -f "$CONFIG_FILE" ]; then
  OUT_IFACE=$(cat "$CONFIG_FILE")
else
  OUT_IFACE=$DEFAULT_IFACE
fi

# Flush iptables rules
iptables -F
iptables -t nat -F

# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# NAT masquerading
iptables -t nat -A POSTROUTING -o "$OUT_IFACE" -j MASQUERADE
