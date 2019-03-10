#!/bin/bash

echo update sources.list
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo cp ./ubuntu16_04_sources.list /etc/apt/sources.list
sudo apt-get update
mkdir ~/.pip
cp ./pip.conf ~/.pip/
sh ./Anaconda3.sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
conda create -n ML python=3.5
conda install jupyter notebook matplotlib -y
