import pandas as pd

def answer_query(query, orders, inventory):

    query = query.lower()

    if "unpaid" in query:

        unpaid = orders[orders["balance"] > 0]

        return unpaid[["po_number","supplier","balance"]]

    elif "low stock" in query:

        low = inventory[inventory["stock"] < 50]

        return low

    elif "shipments" in query:

        return "Shipment tracking available in the Shipments page."

    else:
        return "Sorry, I could not understand the query."