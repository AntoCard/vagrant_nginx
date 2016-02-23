Vagrant.configure("2") do |config|
  app_servers = { :app1 => '192.168.1.44',
                  :app2 => '192.168.1.45',
                  :app3 => '192.168.1.46'
                }

  app_servers.each do |app_server_name, app_server_ip|
    config.vm.define app_server_name do |app_config|
       app_config.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
       app_config.vm.host_name = app_server_name.to_s
       app_config.vm.network "private_network", ip: app_server_ip
       app_config.vm.provision :shell, path: "bootstrap.sh"
       app_config.ssh.insert_key = false

       app_config.vm.provision "ansible" do |ansible|
           ansible.playbook = "install_nginx_apps.yml"
           ansible.verbose = "v"
       end

       app_config.vm.provision "shell" do |s|
           s.inline = "nc $1"
           s.args   = ["-vz localhost 80"]
       end
    end
  end

  # can't get this to run after provisioning
  # config.vm.provision :shell, path: "test_response.py"
end
