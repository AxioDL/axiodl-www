virtualenv .venv
. .venv/bin/activate --prompt=axiodl-www-virtualenv
pip install -r ./requirements.txt
exec python ./manage.py migrate
exec python ./manage.py createsuperuser
