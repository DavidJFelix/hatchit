#Hatchit

This is the web application and backend for apps to interface with for the Hatchit application.

##Running

The stack for this application is:

* Linux (Currently Ubuntu 12.04 LTS)
* Nginx reverse proxy and uWSGI container
* Python 3.3+
* Flask + SQLAlchemy + Jinja2
* PostgreSQL

###Using Vagrant

1. Download vagrant from http://www.vagrantup.com/downloads.html
2. `vagrant init hashicorp/precise64` to download an Ubuntu 12.04 vbox image
3. `vagrant up` to turn on the virtual machine
    1. When not ssh'd into the machine you can type `vagrant suspend` or `vagrant halt` to turn off the VM
4. `vagrant ssh` to ssh into the created VM and use it


###Installation in Ubuntu

1. `sudo apt-get install python3 python3-dev virtualenvwrapper postgresql-client-9.3 libpgsql-dev git` to install dependencies
    1. Note: virtualenvwrapper is a set of functions for bash, so you may need to reload your profile using `source ~/.bashrc`
    2. Note: virtualenvwrapper functions can be buggy within screen, tmux and zsh
2. Configure git properly using github guides.
3. `git clone https://github.com/Automato/hatchit.git` to get the code
4. `cd hatchit`
5. `mkvirtualenv -p /usr/bin/python3 -r requirements.txt hatchit` to create a virtualenv for hatchit
    1. The shell should automatically switch to the flock virtual env, it is indicated parenthetically at the front of your command prompt
    2. To switch env, use `workon hatchit`
    3. To get rid of virtual envs, use `deactivate` to leave the virtual env then `rmvirtualenv hatchit` to remove it from disk
6. `cd src/` to switch to the source directory
7. `./hatchit.py` to run the application, where it will begin running however it's setup.
8. 

##Setup Nginx Reverse proxy

-- coming soon --

##Setup postgreSQL database

-- coming soon --
