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

## 3. Install Flask
```
$ pip install Flask
```

## 4. Run the Flask
```
$ flask --app app.py run
```