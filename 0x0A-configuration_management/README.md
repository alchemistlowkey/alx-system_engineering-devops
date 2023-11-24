Configuration management

Install puppet

$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet


Install puppet-lint
$ gem install puppet-lint


Download the Puppet repository, update your system packages, and install puppetserver:

sudo wget https://apt.puppet.com/puppet-release-bionic.deb
sudo dpkg -i puppet-release-bionic.deb
sudo apt update
sudo apt install puppetserver


Install Puppet Agent

sudo wget https://apt.puppet.com/puppet-release-bionic.deb
sudo dpkg -i puppet-release-bionic.deb
sudo apt update
sudo apt install puppet-agent
