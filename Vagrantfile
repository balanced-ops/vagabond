# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

::Dir.mkdir(host_cache_path) unless ::Dir.exist?(host_cache_path)


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "opscode-ubuntu-12.04"
  config.vm.box_url = ["https://opscode-vm-bento.s3.amazonaws.com",
                       "vagrant",
                       "virtualbox",
                       "opscode_ubuntu-12.04_chef-provisionerless.box"
                      ].join("/")
  config.vm.hostname = "localhost"

  # (ENV['VAGRANT_SYNC_FOLDERS'] || '').split(':').each do |host_folder|
  #   target = "#{guest_project_path}/#{File.basename(host_folder)}"
  #   puts "Syncing #{host_folder} to #{target}"``
  #   config.vm.synced_folder host_folder, target
  # end

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider :virtualbox do |p|
    p.customize ["modifyvm", :id, "--memory", "3072"]
    p.customize ["modifyvm", :id, "--cpus", "2"]
  end

end
