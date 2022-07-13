from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data ["tweet"]]
data['Negative'] = [sentiments.polarity_scorees(i)["neg"] for in in data ["tweet"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data ["tweet"]]