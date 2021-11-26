from flask import *
import pickle
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def predict():
    for x in request.form.values():
        if not x:
            erreur = "Veuillez renseigner tout les champs"
            return render_template("index.html", erreur=erreur)


    int_features = [int(x) for x in request.form.values()]
    final_features = np.array(int_features)
    final_features = final_features.reshape(1,-1)

    prediction = model.predict(final_features)
    if prediction == 1:
        output ="le taux pourque vous ayez une maladie cardiaque est tres eleve veuillez contacter votre docteur au plus vite."
    elif prediction == 0:
        output = "le taux pourque vous ayez une maladie cardiaque est tres faible mais faire attention a votre consommation et consulter regulierement votre docteur."
    return render_template('index.html',predict_text='{}'.format(output))

