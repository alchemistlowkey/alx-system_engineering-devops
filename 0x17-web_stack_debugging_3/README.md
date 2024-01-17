Web stack debugging #3

Concepts
https://intranet.alxswe.com/concepts/17
https://intranet.alxswe.com/concepts/68

Background Context
https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

How I solved it
Open ubuntu 14.04LTS
get the neccesary services/installation (LAMP)

apt-get install -y ruby
gem install puppet-lint -v 2.1.1
sudo apt-get update
sudo apt-get install ca-certificates
sudo wget https://apt.puppetlabs.com/puppet5-release-trusty.deb
sudo dpkg -i puppet5-release-trusty.deb
sudo apt-get update
sudo apt-get install puppet
puppet --version
sudo apt-get update
sudo apt-get install apache2
sudo service apache2 start
sudo apt-get install mysql-server
sudo apt-get install php5 libapache2-mod-php5 php5-mysql
sudo service apache2 restart

in another window go to this directory
cd /var/www/html/
touch wp-settings.php

to the first window where the puppet file was created, run puppet apply 0-strace_is_your_friend.pp
That will be all
