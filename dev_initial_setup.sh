# Assumes setuptools is already installed.
sudo easy_install pip
sudo pip install virtualenv

# Assumes mysqld running
mysql -u root -e "CREATE DATABASE harrison_question_1;"
mysql -u root -e "GRANT ALL ON harrison_question_1.* TO harrison@localhost IDENTIFIED BY 'h0tr0d';"
