echo "Started backend application setup..."
ENV_DIR=./env

if [ -d "$DIR" ];
then
    # if virtualenv exists already
    # activate virtualenv
    # install dependencies for fastapi
    # run application
    source ./env/bin/activate
    pip install -r requirements.txt
    python ./backend/main.py
else
    # create virtualenv
    # activate virtualenv
    # install dependencies for fastapi
    # run application
    python3 -m venv env
    source ./env/bin/activate
    pip install -r requirements.txt
    python ./backend/main.py
fi


