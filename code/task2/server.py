import os
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_captions', methods=['POST'])
def save_captions():
    caption = request.form['caption']

    with open('../../data/coco/example_captions.txt', 'a') as file:
        file.write(caption + '\n')

    image_path = "../../models/coco_AttnGAN2/example_captions"
    os.rmdir(image_path)
    os.system("python ../main.py --cfg cfg/eval_coco.yml --gpu -1")

    return render_template('index.html', image_path=os.path.join(image_path, '/0_s_0_g2.png'))

if __name__ == '_main_':
    app.run(port=80)