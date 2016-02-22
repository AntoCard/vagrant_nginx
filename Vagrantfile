Vagrant.configure("2") do |config|

    config.vm.box = "puppetlabs/ubuntu-14.04-64-nocm"
    config.vm.network :forwarded_port, guest: 80, host: 8080, auto_correct: true
    config.vm.provision :shell, path: "bootstrap.sh"
    config.ssh.insert_key = false

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "install_nginx_apps.yml"
        ansible.verbose = "v"
    end

    config.vm.provision "shell" do |s|
        s.inline = "nc $1"
        s.args   = ["-vz localhost 80"]
    end

end
