#!/bin/bash

echo update sources.list
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo cp ./ubuntu16_04_sources.list /etc/apt/sources.list
sudo apt-get update
sleep 3
sudo apt-get install build-essential git python-dev python-pip python-numpy -y
sudo add-apt-repository ppa:graphics-drivers/ppa -y
sudo apt-get update
ubuntu-drivers devices
sudo apt-get install nvidia-*
sudo reboot
mkdir ~/.pip
cp ./pip.conf ~/.pip/
pip install -r python27_requirements.txt
sh ./Anaconda3.sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
conda create -n ML python=3.5 -y
conda activate ML
conda install jupyter notebook matplotlib -y
conda insall pytorch-cpu torchvision-cpu -c pytorch
pip install opencv-contrib-python opencv-python

