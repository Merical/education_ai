#!/bin/bash

echo update sources.list
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo cp ./ubuntu16_04_sources.list /etc/apt/sources.list
sudo apt-get update
sleep 3
sudo apt-get install build-essential git python-dev python-pip python-numpy -y
