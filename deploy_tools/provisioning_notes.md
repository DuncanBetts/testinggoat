Provisioning a new site
=======================

## Required packages:

* nginx
* PyPy3
* virtualenv + pip
* Git

eg, on Debian:

    PyPy3:
        wget -O pypy.tar.bz2 https://bitbucket.org/pypy/pypy/downloads/pypy3-v5.8.0.tar.bz2
        mkdir /opt/pypy3
        tar jxf pypy.tar.bz2 -C /opt/pypy3
        rm pypy.tar.bz2
        sudo ln -s /opt/pypy3/bin/pypy3 /usr/local/bin/pypy3
        chown -R <username>:<usergroup> /opt/pypy3/

    pip:
        pypy3 -m ensurepip

    virtualenv:
        pypy3 -m pip install virtualenv

    git:
        sudo apt-get install git-core
        git config --global user.name "Joe Blaggs"
        git config --global user.email "joebl@ggs.com"

## NGINX, Virtual Host config:

* sudo apt-get install nginx
* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.co.uk

## Systemd gunicorn service:

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.co.uk
* replace SEKRIT with email password

## Folder structure

Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv
