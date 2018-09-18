huawei-sw-interface_telnet
=========

This ansible role gathering Huawei Switches interfaces information via telnet, the project is aiming to provide the same facts(ansible_net_interfaces) as cisco-ios.

Requirements
------------

Ansible, git, python2

ansible version = 2.6.2
git version = 1.8.3.1-14
python2 version = 2.7.5
python2-pip version = 8.1.2-6
    re (python build-in)
    sys (python build-in)
    json (python build-in)

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variabl$

{{ inventory_hostname }} auto defined according to your playbook yml file

Inside default/main.yml, you will find the variable to make this role useful:

{{ usr }} username of telnet credential
{{ pwd }} password of telnet credential

Change the variable in format "var: value", example as follows:

'''
usr: username
pwd: password
'''

Tree
----

├── defaults
│   └── main.yml
├── files
│   ├── facts
│   └── interfaces.py
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
├── temp
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

Directories Hightlights
-----------------------

├── files
│   ├── facts
│   └── interfaces.py

/files: python scripts
/files/facts: information gathered storage

├── temp 

/temp: temporary storage for scripts


Installing
----------

Expecting the ansible directory is /etc/ansible

'''
#/etc/ansible/roles/
#mkdir huawei-sw-facts_telnet
#cd huawei-sw-facts_telnet
#git clone https://ssunlau/ansible-role-huawei-sw-interface_telnet.git
'''

Example Playbook
----------------

'''
 - hosts: CN2_EU_Huawei_telnet
   gather_facts: false
   connection: local
   roles:
   - role: huawei-sw-interface_telnet                    
'''

License
-------

This project is licensed under the MIT License

Author Information
------------------

* **Chun Lau** [Sonne](https://github.com/ssunlau)

