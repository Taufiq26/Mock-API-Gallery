# Build with Flask and Python3

## 1. Create an environment
Mac/Linux:
```
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv
```

Windows:
```
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

## 2. Activate the environment
Mac/Linux:
```
$ . .venv/bin/activate
```

Windows:
```
> .venv\Scripts\activate
```

## 3. Install the libraries
```
$ pip install -r requirements.txt
```

## 4. Run the Flask
```
$ flask --app app.py --debug run
```
### On Production
Run:
```
> pip3 install gunicorn
> gunicorn -b 0.0.0.0:5000 app:app --daemon
```
Stop:
```
> sudo lsof -i :5000
> sudo kill -9 <PID>
```