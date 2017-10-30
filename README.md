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
git clone git@github.com:justuswilhelm/kerneladmin "$HOME/kerneladmin"
cd "$HOME/kerneladmin"
printf "[debian]\nlocalhost ansible_connection=local" > hosts
ansible-playbook site.yml -i hosts -l debian -e git_email=$YOUR_EMAIL -kK
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

Then, run the following in your terminal

```
git clone git@github.com:justuswilhelm/kerneladmin "$HOME/kerneladmin"
cd "$HOME/kerneladmin"
printf "[darwin]\nlocalhost ansible_connection=local" > hosts
ansible-playbook site.yml -i hosts -l darwin -e git_email=$YOUR_EMAIL -kK
```
