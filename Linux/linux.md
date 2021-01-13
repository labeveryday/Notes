# Linux notes

To verify your linux download

```
echo "hash *file_name.iso" | shasum -a 1 --check
```

How to create a directory and change to it
```
mkdir mytest && cd mytest
```

### Configure Linux Dev Environment

Install Linux utilities

```
sudo apt update
sudo apt upgrade

sudo apt install curl

sudo apt install libssl-dev

sudo apt install build-essential

sudo apt install git

sudo apt-get install python3-venv

sudo apt install nodejs

sudo apt install npm

sudo apt install snapd

sudo snap install atom --classic

sudo snap install postman

sudo snap install ngrok

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt update

sudo apt install docker-ce

sudo usermod -aG docker $USER
```