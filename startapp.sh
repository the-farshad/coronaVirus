. ./env_vars.bash &&
pipenv shell &&
python3 manage.py runserver 0:8000 &
curl http://192.168.100.20:8000/update
