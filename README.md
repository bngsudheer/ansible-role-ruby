Role Name
=========

Install Ruby 2.2, Ruby 2.3 or Ruby 2.4 on CentOS 7. The role utilizes Red Hat software collections.

Description
============

After running the role, the selected version of Ruby will be enabled for new login shell. If you are already logged onto the server, you will not see updated Ruby version. Logout and log back in and you will see newer Ruby version.

```sh
ruby --version
```

Requirements
------------

None. We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/) to enable EPEL.


Role Variables
--------------

| Variable | Default Value | Description | Required? |
|----------|---------------|---------|-----------|
| ruby_version | 2.4 | Ruby version | No |
| ruby_install_globally | true | Whether to enable the designated Ruby version to all users | No |
| ruby_enable_users | [] | Enable the designated Ruby version to specified users | No |

Dependencies
------------

None. We recommend using the role [CentOS Base](https://galaxy.ansible.com/bngsudheer/centos_base/).

Example Playbook
----------------

    - hosts: servers
      vars:
        ruby_version: 2.3
      roles:
         - bngsudheer.ruby

License
-------

BSD

Author Information
------------------

Sudheer Satyanarayana.
* [Twitter](https://twitter.com/bngsudheer)
* [GitHub](https://github.com/bngsudheer)
* [Work](https://www.gavika.com/)
