# Configure Kubernetes on a Raspberry Pi cluster

## Preparing the servers

- Hardware
  - 5 x Raspberry Pi 4 (8GB RAM + 1 SD memory card 128GB)
  - 1 x 8 ports switch 10/100Mbps (Yes, you could use a switch with 1Gb ports, but for a lab, this is just fine)
  - Couple of laptops to remote the cluster
  - Use [Raspberry Pi imager](https://www.raspberrypi.com/software/) to install Ubuntu server 24 LTS on the SD cards.

- Configuration
  - Kubernetes
    - 1 x Master
    - 2 x Workers
  - Servers
    - 1 x Storage and Files
    - 1 x Observability and Services

### All

- Configure static IP address. Use [Netplan](https://netplan.readthedocs.io/en/stable/examples/#how-to-configure-a-static-ip-address-on-an-interface)

### Kubernetes

#### Install Kubernetes with Ansible, run these playbooks
  - basic_pkg.yml
  - public_key_for_k8s.yml
  - add_k8s_apt_repo.yml
  - installK8s.yml
  - enable_IPv4.yml

### Servers : Storage and Files 

- 