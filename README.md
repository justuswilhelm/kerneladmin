# Kernel Admin

Ansibel Recipe

## Requirements

+ ansible
+ git

## Install on fresh Debian

```
git clone git@github.com:justuswilhelm/kerneladmin "$HOME/kerneladmin"
cd "$HOME/kerneladmin"
printf "[debian]\nlocalhost ansible_connection=local" > hosts
ansible-playbook site.yml -i hosts -l debian -e git_email=$YOUR_EMAIL -K
```

## Install on macOS

Make sure to install
- Homebrew: [https://brew.sh/](https://brew.sh/), and
- Ansible: [https://www.ansible.com/](https://www.ansible.com/) by running

```
brew install ansible
```

Then, run the following in your terminal

```
git clone git@github.com:justuswilhelm/kerneladmin "$HOME/kerneladmin"
cd "$HOME/kerneladmin"
printf "[darwin]\nlocalhost ansible_connection=local" > hosts
ansible-playbook site.yml -i hosts -l darwin -e git_email=$YOUR_EMAIL -K
```
