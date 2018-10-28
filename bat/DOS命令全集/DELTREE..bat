@echo off

mkdir test
cd test
mkdir 1
mkdir 2
dir

cd ..
DELTREE /y E:\gitcode\newbie\bat\DOS命令全集\test

cd test
dir