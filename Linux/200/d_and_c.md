# Domains & Competencies

<https://training.linuxfoundation.org/certification/certified-it-associate/>

## Linux Fundamentals

### Linux Operating System

- Linux is distributed under the GUN General Public License, version 2 (GPLv2)
- Loadable Kernel Module (LKM)
  - Device drivers
    - Kernel Driver
    - Types: Character , block, and network
  - Filesystem drivers
  - System calls
  - Kernel Module
    - `insmod`, `modprob`, and `rmmod`
    - Have separate address spaces
    - Have higher execution privileges
    - Do not execute sequentially
    - Use different header files
- Processes
- memory Management
- File Management
- Input/Output
  - Devices and Devices Drivers
- Interpreting user commands
- Resource allocation

### File Management Commands

- Backup
  - `tar`
  - `rsync`
- File System Type
  -`lsblk`
  - <https://www.kernel.org/doc/html/latest/admin-guide/devices.html>
  - Linux Filesystem Hierarchy Standard (FHS)
  - <https://www.pathname.com/fhs/>
- Disk Formatting Utilities
  - `fdisk`, `sfdisk`, `parted`, `gnome-disk`, and `gparted`
- Directories and Files
  - `man hier`
    - `tree -L 1 -d /`
  - `ls li FILENAME`
  - `stat FILENAME`

### System Commands or Linux Commands

- Terminal emulator
  - xterm
  - konsole
  - Terminator
  - gnome-terminal
  - gnome-shell-extension
- General Commands
  - cat
  - cd
  - find
  - grep
  - info
  - pwd
  - ls
  - grep
  - df
  - man man
  - find
  - mount
  - sudo
- Systems Administrator Commands
  - systemctl
  - apt
  - chgrp
  - chmod
  - fdisk
  - iostat
  - ps
  - vmstat
  - yum/dnf
  - zypper
- Network Administrator Commands
  - dig
  - ip
  - netstat
  - ping
  - traceroute
- User Administration Commands
  - adduser
  - userdel
  - usermod
  - deluser
- Others
  - id
  - blkid
  - ss
  - free
  - firefox/lynx

### General Network Commands

- IP Addressing and Subnetting for New Users
  <https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html>

## System Administration Fundamentals

### System Administration Tasks

### Networking

- NetworkManager
  - nmcli
  - nmtui
  - nm-connection-editor
- nmcli
  - nmcli device show
- ip
  - ip route
  - ip addr show
- ipcalc 1.1.1.1/26  
- host
  - host www.home.cl
- dig
  - dig www.home.cl
  /etc/resolv.conf

### Troubleshooting

- Is the adapter enabled?
  - ip
    - ip link
    - ip link set up|down DEVICE
    - ethtool -i DEVICE
    - lshw -C network
    - lshw -json -C disk
- Local configuration
  - IP Address
  - Netmask
  - Route
  - DHCP Client
    - dhclient -v DEVICE
    - cd /var/lib/dhclient
    - cat dhclient.leases
    - sip addr show
- Verify connection
  - Local system
  - Default route
  - Remote host
    - ping -c 4 127.0.0.1
    - ping -c 4 local_IP
    - ping -c 4 GW_IP
    - ping -c 4 remote_IP
    - elinks -dump URL
    - lynx -dump URL

- Verify Server functions
  - Daemons are active
  - Correct port is open
  - Localhost for function check
  - Check firewall
    - systemctl 
    - systemctl status boot.mount
    - ss -tlapn
    - curl 127.0.0.1.:1236
    - sudo iptables -vnL

## Cloud Computing Fundamentals

### Cloud Computing Fundamental

- Increased Performance and Agility
- Cost Savings
- Easy Access to Resources
- Maintenance Offloaded to Provided
- Multi-tenancy
- Increased Reliability
- Increased Security

### Performance / Availability

- On-Premises
  - Network, Storage, Servers, Virtualization, OS, Middleware, Runtime, Data, Applications
- Infrastructure as a Service (IaaS)
  - OS, Middleware, Runtime, Data, Applications
  - Rackspace, Azure, AWS, GCE, Digital Ocean
- Platformas a Service (PaaS)
  - Data, Applications
  - Heroku, OpenShift, Apache Stratos, AWS Elastic Beanstalk, Google App Engine
- Software as a Service (SaaS)
  - All above managed by the provider
  - Gmail, Slack, O365, DropBox, HubSpot
- Function as a Service (FaaS)
  - Specifuc function that runs once or multiple times

### Serverless

### Cloud Cost and Budgeting

## Security Fundamentals

### Security Basics

### Data Security

### Network Security

### System Security

## DevOps Fundamentals

### DevOps Basics

- SRE

### Containers

### Deployment Environments

### Git Concepts

## Supporting Applications and Developers

### Software Project Management

### Software Application Architecture

### Functional Analysis

### Open-source Software and Licensing