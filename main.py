from interestModel import main
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    graph_html = None

    if request.method == "POST":
        principal = int(request.form['principal'])
        rate = float(request.form['rate']) / 100
        deposits = int(request.form['deposits'])
        time = int(request.form['time'])

        amount = []
        fig = main(principal, rate, deposits, time, amount)
        graph_html = fig.to_html(full_html=False)

    return render_template("index.html", graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)
