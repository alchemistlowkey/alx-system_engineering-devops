Web stack debugging #4

# Install puppet-lint

sudo apt-get install -y ruby

sudo gem install puppet-lint -v 2.1.1

# Install apache benchmark tools

sudo apt-get install apache2-utils

# Install Nginx to use as the server for testing

sudo apt-get install nginx

sudo service nginx restart

# To check if the apache benchmark is installed

ab -V
