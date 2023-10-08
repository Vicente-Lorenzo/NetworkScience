import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


airlines_data = pd.read_csv("data/airlines.csv")
airlines_data = airlines_data[["src_iata", "src_id", "dest_iata", "dest_id"]]

G = nx.DiGraph()

for _, row in airlines_data.iterrows():
    G.add_edge(row['src_iata'], row['dest_iata'], src_id=row['src_id'], dest_id=row['dest_id'])

nx.draw(G, with_labels=True)
plt.show()
