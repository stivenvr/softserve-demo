from flask import Flask, render_template
import random

app = Flask(__name__)

#list of images
images = [
    "https://img.freepik.com/foto-gratis/adorable-gatito-domestico-espacio-copia_23-2149167112.jpg?w=1380&t=st=1681916315~exp=1681916915~hmac=56d331bda2dc74ac6a388d070bc8de8ff5bccfddf2b10ae90137a3426ef4ab5a",
    "https://img.freepik.com/foto-gratis/gatito-pared-monocromatica-detras-ella_23-2148955134.jpg?w=740&t=st=1681919149~exp=1681919749~hmac=a565aa15963d1ff85be98298344f3efa24e963211f7fb200072e876f95446291",
    "https://img.freepik.com/foto-gratis/gato-rojo-o-blanco-i-estudio-blanco_155003-13189.jpg?w=740&t=st=1681919181~exp=1681919781~hmac=009397d36fe56837bf9f1c81efc8d40211842df2c0e5812fce12feda9961c3a7",
    "https://img.freepik.com/foto-gratis/gatito_658691-468.jpg?w=1380&t=st=1681919204~exp=1681919804~hmac=d6d212bd752b9d7c723c039e60155b5f90ef9f27c2cf3acd921820fa1ad01c32"
]
    
@app.route('/')
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)