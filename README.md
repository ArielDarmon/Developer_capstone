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

python3 -m pip install -U -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
# python3 manage.py migrate --run-syncdb

# superuser
python3 manage.py createsuperuser

python3 manage.py runserver

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