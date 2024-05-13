from flask import Flask, request

app = Flask(__name__)

mock_user_id = "0ef8a3f7-2779-4208-95e4-5a5488e5e3c4"
mock_username = "demo_user"
mock_password = "d3m0password123"
mock_access_token = "hs0IcxqvC24SZDad5FGRbVHe2mH5x1dlkiBCDuxspsAipgaCvZFsyHJI5YBSvJAu"

@app.get("/")
def hello_world():
    res = {
        'message': 'Hello, World!'
    }

    return res

@app.post("/login")
def do_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == mock_username and password == mock_password:
        status = 200
        res = {
            'message': 'Welcome, Demo User',
            'access_token': mock_access_token
        }
    else:
        status = 401
        res = {
            'message': 'Wrong username and password combination!'
        }

    return res, status

@app.get("/profile")
def profile():
    token = request.headers.get('Authorization')

    if token == mock_access_token:
        status = 200
        res = {
            'name': 'Demo User',
            'address': 'Bandung, Jawa Barat, Indonesia',
        }
    else:
        status = 401
        res = {
            'message': 'You cannot access this API!'
        }

    return res, status

gallery_images = [
    {
        'id': '5a7bfe86-c31c-4c90-a616-35e689db342b',
        'name': 'Gundam Astray Red Frame',
        'image': 'https://gallery-api.baradeveloper.com/static/images/gundam-astray-red-frame.jpeg',
        'like': 1068,
        'comments': [
            {'name': 'Gunpla Mania', 'comment': 'Nice bild'},
            {'name': 'Newbie Builder', 'comment': 'Give me the link!'},
            {'name': 'Anomim Pilot', 'comment': 'Tha\'s my Gundam'},
        ]
    },
    {
        'id': '339caf3c-7fbe-4861-b13a-01da3c3225a2',
        'name': 'Beautiful Scenery',
        'image': 'https://gallery-api.baradeveloper.com/static/imagesbeautiful-scenery.jpeg',
        'like': 1350,
        'comments': [
            {'name': 'Veteran Painter', 'comment': 'Great art'},
            {'name': 'Anonim Painter', 'comment': 'Is that my painting?'},
            {'name': 'Guest634', 'comment': 'Do you have a prove?'},
            {'name': 'Van Gogh', 'comment': 'Nice one'},
        ]
    },
    {
        'id': '23facae8-9dae-468b-b568-607b4288dc36',
        'name': 'Tree Monster',
        'image': 'https://gallery-api.baradeveloper.com/static/images/tree-monster.jpeg',
        'like': 5001,
        'comments': [
            {'name': 'Fantasy Maniac', 'comment': 'Nice illustration'},
            {'name': 'Treant Protector', 'comment': 'My boy'},
            {'name': 'Groot', 'comment': 'I am Groot'},
        ]
    },
    {
        'id': 'a9e8cf84-420b-434d-8500-6123d30ef954',
        'name': 'Dragon Painting',
        'image': 'https://gallery-api.baradeveloper.com/static/images/dragon-painting.jpeg',
        'like': 6090,
        'comments': [
            {'name': 'Dragon Lover', 'comment': 'Awesome'},
            {'name': 'Handa', 'comment': 'Nice art bro'},
        ]
    },
    {
        'id': '4d319a8f-00fa-4056-aee1-7b471cbba6e1',
        'name': 'Axolotl Mage',
        'image': 'https://gallery-api.baradeveloper.com/static/images/axolotl-mage.jpeg',
        'like': 10000,
        'comments': [
            {'name': 'Animalia', 'comment': 'CUTEEE!!!'},
            {'name': 'Mage Association', 'comment': 'I have sent you an invitation letter, please check it'},
            {'name': 'Anonim Adventurer', 'comment': 'Wanna join my party?'},
        ]
    },
    {
        'id': '9c6ceb88-8f59-4581-b52c-e01517bf01e1',
        'name': 'Avatar Beasts',
        'image': 'https://gallery-api.baradeveloper.com/static/images/avatar-beasts.jpeg',
        'like': 4275,
        'comments': [
            {'name': 'Aang', 'comment': 'Accurate info 👍'},
            {'name': 'Zuko', 'comment': 'Is that my dragon?'},
            {'name': 'Toph Beifong', 'comment': 'What is that?'},
            {'name': 'Sokka', 'comment': '🤦'},
        ]
    },
    {
        'id': 'dde4b9ca-6483-4b5f-9dc0-efbae0d78ab1',
        'name': 'Wave Painting',
        'image': 'https://gallery-api.baradeveloper.com/static/images/wave-painting.jpeg',
        'like': 8009,
        'comments': [
            {'name': 'Surfer', 'comment': 'That wave must be great if real'},
            {'name': 'Jack Kahuna Laguna', 'comment': 'EZ'},
            {'name': 'Larry the Lobster', 'comment': 'Worth a try'},
        ]
    },
    {
        'id': 'c641799a-3865-41a1-82db-0f0ec0b25e86',
        'name': 'Bored Panda',
        'image': 'https://gallery-api.baradeveloper.com/static/images/bored-panda.jpeg',
        'like': 50768,
        'comments': [
            {'name': 'I am Panda', 'comment': 'MY FRIEEEEEEND'},
            {'name': '貓熊', 'comment': '你好'},
        ]
    },
    {
        'id': 'ea8b9a28-cf88-49d3-b591-e3e39c9f8715',
        'name': 'Tea Calligraphy',
        'image': 'https://gallery-api.baradeveloper.com/static/images/tea-calligraphy.jpeg',
        'like': 9234,
        'comments': [
            {'name': 'Handa', 'comment': 'What a calming calligraphy'},
            {'name': 'Uncle Iroh', 'comment': 'Sharing tea with a fascinating stranger is one of life\'s true delights.'},
        ]
    },
    {
        'id': 'dd1951a7-be43-4285-b1b9-a2a795eedaee',
        'name': 'Wanderer Cat',
        'image': 'https://gallery-api.baradeveloper.com/static/images/wanderer-cat.jpeg',
        'like': 7877,
        'comments': [
            {'name': 'Cat Folk', 'comment': 'Thas\'s me 😌'},
            {'name': 'Anonim Adventurer', 'comment': 'Wanna join my party?'},
            {'name': 'Adventurer Guild Official', 'comment': 'Hurry report your quest progress!'},
        ]
    },
]
@app.get("/gallery")
def gallery():
    return [
        {
            'id': d['id'],
            'name': d['name'],
            'image': d['image']
        } for d in gallery_images
    ]

@app.get("/gallery/<id>")
def gallery_detail(id):
  for image in gallery_images:
    if image['id'] == id:
      return image

  return {'message': 'Image Not Found!'}, 404