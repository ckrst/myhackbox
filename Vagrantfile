# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "vinik/hackbox-kali"
    config.vm.box_version = "0.1.1650066008"
    
    config.vm.synced_folder "./data", "/vagrant_data"
    config.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.memory = "8192"
        # vb.memory = "4096"
    end
end
