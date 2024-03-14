# coding-project-template
git clone https://github.com/ArielDarmon/Developer_capstone.git

# #####################################
#
#            DJANGO
#
# #####################################

# launch
cd /home/project/Developer_capstone/server

pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate

py -m pip install -U -r requirements.txt
py manage.py makemigrations
py manage.py migrate
# py manage.py migrate --run-syncdb

# superuser
py manage.py createsuperuser

py manage.py runserver

# #####################################
#
#            NEW TERMINAL FOR REACT
#
# #####################################
cd /home/project/Developer_capstone/server/frontend

npm install
npm run build

# #####################################
#
#            MONGO DB
#
# #####################################
cd /home/project/Developer_capstone/server/database

docker build . -t nodeapp
docker-compose up