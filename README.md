# Kernel Admin

![popcorn](docs/popcorn.png)

Ansible Recipe

## Requirements

+ ansible
+ git

## Install on fresh Debian

```
sudo apt install ansible git
```

```
git clone https://github.com/justuswilhelm/kerneladmin.git "$HOME/kerneladmin"
cd "$HOME/kerneladmin"
printf "[debian]\nlocalhost ansible_connection=local" > hosts
read YOUR_NAME
read YOUR_EMAIL
ansible-playbook site.yml -i hosts -kK \
    -l debian \
    -e git_email="$YOUR_EMAIL" \
    -e git_name="$YOUR_NAME"
```

## Install on fresh Ubuntu

```
sudo apt install ansible git
```

```
git clone https://github.com/justuswilhelm/kerneladmin.git "$HOME/kerneladmin"
cd "$HOME/kerneladmin"
printf "[ubuntu]\nlocalhost ansible_connection=local" > hosts
read YOUR_NAME
read YOUR_EMAIL
ansible-playbook site.yml -i hosts -kK \
    -l debian \
    -e git_email="$YOUR_EMAIL" \
    -e git_name="$YOUR_NAME"
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

Then, run the following in your terminal

```
git clone https://github.com/justuswilhelm/kerneladmin.git "$HOME/kerneladmin"
cd "$HOME/kerneladmin"
printf "[darwin]\nlocalhost ansible_connection=local" > hosts
read YOUR_NAME
read YOUR_EMAIL
ansible-playbook site.yml -i hosts -kK \
    -l darwin \
    -e git_email="$YOUR_EMAIL" \
    -e git_name="$YOUR_NAME"
```
