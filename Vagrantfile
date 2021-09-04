# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    # config.vm.box = "vinik/hackbox-kali:0.1.1627163680"
    config.vm.box = "vinik/hackbox-kali"
    config.vm.synced_folder "./data", "/vagrant_data"
    config.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.memory = "8192"
    end
end
