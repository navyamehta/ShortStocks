import newsbot
import newsresults
import classifier
import trainer
import chooser
from flask import Flask, request, render_template
from sklearn.neural_network import MLPClassifier
import getall
    

app = Flask(__name__)

@app.route('/search', methods=["GET"])
def my_form():
    return render_template('WebPage1.html')

@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['query']
    articles = newsbot.getnews(text)
    tag2d = []
    for lst in articles:
        tag2d.append(classifier.classifier(lst))
    full = getall.getall("Navya")
    X = full[0]
    y = full[1]
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 40, 10, 2), random_state=1)
    clf.fit(X, y)
    relevance_array = clf.predict(tag2d)
    artprint = newsresults.show_news(text)
    finalarr = chooser.chooser(relevance_array, artprint)
    disp1 = finalarr


    return render_template('WebPage2.html', disp1 = disp1), 200
