from flask import Flask, render_template, request

app = Flask(__name__)

def recommend_crop(weather, soil):
    if weather == "rainy" and soil == "loamy":
        return "Rice"
    elif weather == "dry" and soil == "sandy":
        return "Millet"
    elif weather == "moderate" and soil == "clay":
        return "Wheat"
    else:
        return "Check local extension service for better advice."

@app.route('/', methods=['GET', 'POST'])
def home():
    crop = ""
    if request.method == 'POST':
        weather = request.form['weather']
        soil = request.form['soil']
        crop = recommend_crop(weather, soil)
    return render_template('index.html', crop=crop)

if __name__ == '__main__':
    app.run(debug=True)