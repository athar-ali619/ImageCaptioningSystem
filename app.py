from flask import Flask, render_template, redirect, request, jsonify
import untitled0
import os
from os.path import join, realpath, dirname

images_path = join(dirname(realpath(__file__)), 'static/imageData/')
app = Flask(__name__)

app.config["folder"] = images_path

@app.route('/', methods=["GET", "POST"])
def index():
    # return 'Hello World'
    if request.method == "POST":

        return redirect("/predictios")
    
    else:

        return render_template('index.html')


@app.route("/predictions", methods=["POST"])
def predict():
    fileuploaded = request.files["image"]
    filename = fileuploaded.filename
    fileuploaded.save(os.path.join(app.config['folder'], str(filename)))
    pic = 'soccer1.jpg'
    newpic = os.path.join(app.config['folder'], str(filename))
    print(newpic)
    untitled0.encoding_test[pic] = untitled0.encode(newpic)
    image1 = untitled0.encoding_test[pic].reshape((1,2048))
    print(image1)
    

    print("Greedy Search:",untitled0.greedySearch(image1))
    greedy = untitled0.greedySearch(image1)
    print("Beam Search, K = 3:",untitled0.beam_search_predictions(image1, beam_index = 1))
    beemindex1 = untitled0.beam_search_predictions(image1, beam_index = 1)
    print("Beam Search, K = 5:",untitled0.beam_search_predictions(image1, beam_index = 2))
    beemindex2 = untitled0.beam_search_predictions(image1, beam_index = 2)
    print("Beam Search, K = 7:",untitled0.beam_search_predictions(image1, beam_index = 3))
    beemindex3 = untitled0.beam_search_predictions(image1, beam_index = 3)

    # print("Beam Search, K = 5:",beam_search_predictions(image1, beam_index = 2))
    # print("Beam Search, K = 7:",beam_search_predictions(image1, beam_index = 3))
    # print("Beam Search, K = 11:",beam_search_predictions(image1, beam_index = 9))

    return jsonify({"data": "true", "beamindex1": beemindex1, "beamindex2": beemindex2, "beamindex3": beemindex3, "greedy": greedy})

if __name__== "__main__":
    app.run()

