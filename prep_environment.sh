virtualenv .venv
. .venv/bin/activate --prompt=axiodl-www-virtualenv
pip install -r ./requirements.txt
python ./manage.py initdata
#exec python ./manage.py createsuperuser
