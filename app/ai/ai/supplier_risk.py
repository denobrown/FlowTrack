import pandas as pd

def risk_score(data):

    scores = []

    for i,row in data.iterrows():

        score = 100

        if row["payment_delay"] > 10:
            score -= 20

        if row["shipment_delay"] > 5:
            score -= 30

        scores.append(score)

    data["risk_score"] = scores

    return data