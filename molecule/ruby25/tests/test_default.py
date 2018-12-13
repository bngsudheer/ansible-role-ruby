import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_ruby_25_installed(host):
    ruby = host.package("rh-ruby25")
    assert ruby.is_installed
    assert ruby.version == "2.5"

def test_ruby_25_available(host):
    ruby = host.check_output('source /etc/profile.d/enableruby25.sh && which ruby')
    assert ruby == '/opt/rh/rh-ruby25/root/usr/bin/ruby'
