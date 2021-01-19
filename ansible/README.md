# Ansible Notes

Ansible is an open source configuration management tool. 

[Go here for ansbile documentation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

___

## Setting up your device

Generate an SSH Key on a local device

`ssh-keygen -t rsa`

Copy the public key to the device

`ssh-copy-id -p 22 root@192.168.1.1`

On cisco device to resolve no matching key exchange method found.

`ssh  -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc -l username 192.168.1.1`

___

## Installing Ansible

>NOTE: Before installing Ansible. First create a virtual environment
cd to your desired directory

```python
python3 -m venv venv
```

Install ansible on MAC `This should be done via pip`

```python
python3 -m pip install ansible
```

Note if netmiko is nornir is not installed you will have to install paramiko. This is already a preq for the packages mentioned.

```python
python3 -m pip install paramiko
```

___

## Configure an Ansible playbook

create a `host` file and add the device configurations

```yaml
[servers]
server01 ansible_host=192.168.0.20 ansible_port=20001 ansible_user=root
server02 ansible_host=192.168.0.20 ansible_port=20002 ansible_user=root
```

>Note if you communicating with older devices for the key exchange

```yaml
[servers]
server01 ansible_host=192.168.0.20 ansible_port=20001 ansible_user=root ansible_ssh_common_arg="-o HostKeyAlgorithms=ssh-rsa -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes256-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha2-512"
server02 ansible_host=192.168.0.20 ansible_port=20002 ansible_user=root ansible_ssh_common_arg="-o HostKeyAlgorithms=ssh-rsa -o KexAlgorithms=diffie-hellman-group1-sha1 -o Ciphers=aes256-cbc,3des-cbc -o MACs=hmac-md5,hmac-sha2-512"
```

Test Ansible connection to the devices

`ansible all -i hosts -m ping`

Create template file (Optional) 

`network-interface.tmpl`

Create your ansibile playbook

`configure-servers.yml`

To run the playbook

`ansible-playbook -i hosts configure-servers.yml`

Run the playbook and save to a log file

`ansible-playbook -i hosts configure-servers.yml > ansible.log`
