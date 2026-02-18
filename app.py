from flask import *
import nltk
nltk.download("vader_lexicon")

from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
	if request.method == "POST":
		text = request.form.get("text")
		sia = SentimentIntensityAnalyzer()
		ps = sia.polarity_scores(text)
		msg = ""
		if ps["compound"] > 0.5:
			msg = "Thank u for Positive Review"
		elif ps["compound"] < -0.05:
			msg = "Sorry for this experience"
		else:
			msg = "Thank u for Review"
		return render_template("home.html",msg=msg)
	else:
		return render_template("home.html")


#app.run(debug=True,use_reloader=True)