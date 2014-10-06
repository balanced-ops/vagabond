# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

HOST_PROJECT_PATH = File.expand_path('../../', __FILE__)
puts HOST_PROJECT_PATH
GUEST_PROJECT_PATH = "/opt/"


begin
  Vagrant.require_plugin('nugrant')
rescue => ex
  warn "[\e[1m\e[31mERROR\e[0m]: Please run: vagrant plugin install nugrant"
  raise
end


##
# This function create synced folders and link them to the
# `GUEST_PROJECT_PATH` on the guest vm.
#
# The yaml definition that it understands is this:
#
#     synced_folders:
#       - folder_1
#       - folder_...
#
# @param config A vagrant config object
# @return nil
def setup_custom_synced_folders(config)
  return unless config.user.has_key?("synced_folders")
  config.user.synced_folders.each do |host_folder|
    target = File.join(GUEST_PROJECT_PATH, File.basename(host_folder))
    puts "Syncing #{host_folder} to #{target}"
    config.vm.synced_folder host_folder, target
  end
end

##
# This function returns the provider overrides in your user
# .vagrantuser file. An example is like this:
#
#    providers: {
#     virtualbox: {
#       memory: 4096,
#       cpus: 2
#     },
#     aws: {
#       region: us-west-1,
#       availability_zone: us-west-1a,
#       ssh_key: ~/.ssh/id_rsa.pub,
#       flavor_id: m3.2xlarge,
#       iam_profile_name: some-profile,
#     }
#   }
#
# @param provider the provider config (i.e. virtualbox, etc.)
# @param config the vagrant configuration
# @return the configuration provider
def get_provider_overrides(provider, config)
  return unless config.user.has_key?('providers')
  return unless config.user.providers.has_key?(provider)
  return config.user.providers[provider]
end


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = config.user.fetch("box", "precise64")
  config.vm.hostname = config.user.fetch("hostname", "localhost")

  setup_custom_synced_folders(config)

  config.vm.synced_folder "#{HOST_PROJECT_PATH}", "/vagrant"

  config.vm.provider :virtualbox do |vb|
    overrides = get_provider_overrides("virtualbox", config)
    vb.customize [
      "modifyvm", :id, "--memory", overrides.fetch("memory", "3072")
    ]
    vb.customize [
      "modifyvm", :id, "--cpus", overrides.fetch("cpus", "2")
    ]
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "#{HOST_PROJECT_PATH}/playbook.yml"
    # ansible.verbose = 'vvvv'
    # ansible.hosts = 'all'
  end

end
