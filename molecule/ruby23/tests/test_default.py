import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_ruby_23_installed(host):
    ruby = host.package("rh-ruby23")
    assert ruby.is_installed

def test_ruby_23_available(host):
    ruby = host.check_output('source /etc/profile.d/enableruby23.sh && which ruby')
    assert ruby == '/opt/rh/rh-ruby23/root/usr/bin/ruby'
