# TimeKeeper-QGIS-Plugin
QGIS Plugin for Time Keeping

This is a QGIS Plugin for time tracking using PyQT. There is also a sample but customizable backend using FastAPI, Sqlite, and SqlAlchemy.

## Getting started
* Create a virtual environment for this project and install dependencies
```
virtualenv .venv
```

* Activate the virtual environment
```
source .venv/bin/activate
```

* Install the dependencies
```
pip install -r requirements.txt
```

* Run the application
```
uvicorn app.main:app --reload
```

And finally, the application will run on the following URL: http://127.0.0.1:8000 go to http://127.0.0.1:8000/docs for endpoint documentation.

#### Using the Plugin

Compile plugin
```
cd time_keeper/
pyrcc5 -o resources.py resources.qrc
```

Copy folder into QGIS
```
cp -r /mnt/c/Users/Winston/Documents/GitHub/TimeKeeper-QGIS-Plugin/time_keeper /mnt/c/Users/Winston/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/time_keeper
```
