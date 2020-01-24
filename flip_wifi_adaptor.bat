@echo off
netsh interface show interface
echo disabling the interfaces
timeout 5
netsh interface set interface "Wi-Fi" disable
echo enabling the interfaces
timeout 5
netsh interface set interface "Wi-Fi" enable
