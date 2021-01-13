# Ansible Notes

Geneerate an SSH Key on a local device

`ssh-keygen -t rsa`

Copy the public key to the device 

`ssh-copy-id -p 20001 root@192.168.0.20`

create a `host` file and add the device configurations
```
[servers]
server01 ansible_host=192.168.0.20 ansible_port=20001 ansible_user=root
server02 ansible_host=192.168.0.20 ansible_port=20002 ansible_user=root
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

