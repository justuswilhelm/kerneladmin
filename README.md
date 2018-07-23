# Kernel Admin

![popcorn](docs/popcorn.png)

Ansible Recipe

## Requirements

+ ansible
+ git

## Install on fresh Debian

### Installing Requirements

```
sudo apt install ansible git
```

### Installing Kernel Admin

```
(
set -ue
OS=debian
git clone https://github.com/justuswilhelm/kerneladmin.git "$HOME/kerneladmin" || echo "Already cloned"
cd "$HOME/kerneladmin"
printf "[$OS]\nlocalhost ansible_connection=local" > hosts
read -p "Git Username> " YOUR_GIT_NAME
read -p "Git Email> " YOUR_GIT_EMAIL
ansible-playbook site.yml -i hosts -kK \
    -l $OS \
    -e git_email="$YOUR_GIT_EMAIL" \
    -e git_name="$YOUR_GIT_NAME"
)
```

## Install on fresh Ubuntu

### Installing Requirements

```
sudo apt install ansible git
```

### Installing Kernel Admin

```
(
set -ue
OS=ubuntu
git clone https://github.com/justuswilhelm/kerneladmin.git "$HOME/kerneladmin" || echo "Already cloned"
cd "$HOME/kerneladmin"
printf "[$OS]\nlocalhost ansible_connection=local" > hosts
read -p "Git Username> " YOUR_GIT_NAME
read -p "Git Email> " YOUR_GIT_EMAIL
ansible-playbook site.yml -i hosts -kK \
    -l $OS \
    -e git_email="$YOUR_GIT_EMAIL" \
    -e git_name="$YOUR_GIT_NAME"
)
```

## Install on macOS

### Installing Requirements

Make sure to install

- Homebrew: [https://brew.sh/](https://brew.sh/), and
- Ansible: [https://www.ansible.com/](https://www.ansible.com/)

Homebrew can be installed by running

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Ansible can be installed by running

```
brew install ansible
```

Having trouble with XCode? Run this in your Terminal:

```
sudo xcodebuild -license accept
```

### Installing Kernel Admin

Then, run the following in your terminal

```
(
set -ue
OS=ubuntu
git clone https://github.com/justuswilhelm/kerneladmin.git "$HOME/kerneladmin" || echo "Already cloned"
cd "$HOME/kerneladmin"
printf "[$OS]\nlocalhost ansible_connection=local" > hosts
read -p "Git Username> " YOUR_GIT_NAME
read -p "Git Email> " YOUR_GIT_EMAIL
ansible-playbook site.yml -i hosts -kK \
    -l $OS \
    -e git_email="$YOUR_GIT_EMAIL" \
    -e git_name="$YOUR_GIT_NAME"
)
```

## Rerun Installation

Rerun the installation anytime after that by just typing

```
ansible-playbook $HOME/kerneladmin/site.yml -i $HOME/kerneladmin/hosts -kK
```
