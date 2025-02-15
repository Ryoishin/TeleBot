#!/bin/bash
clear
echo "
 _____    _      _           _   
|_   _|__| | ___| |__   ___ | |_ 
  | |/ _ \ |/ _ \ '_ \ / _ \| __|
  | |  __/ |  __/ |_) | (_) | |_ 
  |_|\___|_|\___|_.__/ \___/ \__|

"
# Termux session string generator for Ryoishin
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/TeamRyoishin/Ryoishin/master/resources/ryoishin-setup.py
pip install telethon
python ryoishin-setup.py