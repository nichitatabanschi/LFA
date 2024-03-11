# graph_drawer.py
import networkx as nx
import matplotlib.pyplot as plt

class GraphDrawer:
    @staticmethod
    def draw(states, transitions):
        G = nx.DiGraph()
        G.add_nodes_from(states)
        for state in transitions:
            for symbol in transitions[state]:
                for next_state in transitions[state][symbol]:
                    G.add_edge(state, next_state, label=symbol)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
