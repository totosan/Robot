#!/bin/bash
sudo pip install Jetson.GPIO
sudo groupadd -f -r gpio
sudo usermod -a -G gpio toto
# https://github.com/NVIDIA/jetson-gpio