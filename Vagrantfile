Vagrant.configure("2") do |config|
  config.vm.define "centos7" do |centos7|
    centos7.vm.box = "centos/7"
    centos7.vm.hostname = "centos7-vm1"
    centos7.vm.network :private_network, ip: "192.168.0.101"
    centos7.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
  end