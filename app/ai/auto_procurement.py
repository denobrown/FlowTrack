import pandas as pd

def generate_purchase_orders(inventory):

    threshold = 50

    orders = []

    for i,row in inventory.iterrows():

        if row["stock"] < threshold:

            orders.append({
                "product":row["product"],
                "recommended_order":100 - row["stock"]
            })

    return pd.DataFrame(orders)