#!/bin/bash

cd ~
wget https://github.com/Merical/education_ai/blob/master/requirement/ubuntu16.04_sources.list
echo update sources.list
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo cp ./ubuntu16.04_sources.list /etc/apt/sources.list
sudo apt-get update
sleep 3
sudo apt-get install build-essential git python-dev python-pip python-numpy -y
