## Synopsis

Use Vagrant and Ansible to create 3 vm's with a Hello world Flask app and Nginx load balancing between them,

## Installation

cd into directory and `vagrant up`

## Usage
Use any of this ip's: 192.168.1.44-46 port 80

## Tests

An inline script will check every box port 80 and output if it is listening.

A Python script runs at the end of provisioning and checks every box http response for a "Hello World!" string

## Comments and caveats

Due to a misunderstanding, the three vm's are identical and all load balance between each other with healthchecks. Realized too late one was supossed to be a dedicated Nginx LB.

The inline script that checks port 80 will randomly output a failure followed by a success if the connection is successful.

The Python script `test_response.py` is commented in the Vagrantfile due to being executed before any other provisioning step. Has to be fixed.

## License

GPL
