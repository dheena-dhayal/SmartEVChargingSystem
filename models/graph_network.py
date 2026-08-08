import math

class Node:
    def __init__(self, id, name, x, y, is_charging_station=False):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.is_charging_station = is_charging_station

class Edge:
    def __init__(self, start_node, end_node, distance, traffic_factor=1.0):
        self.start_node = start_node
        self.end_node = end_node
        self.distance = distance
        self.traffic_factor = traffic_factor  # 1.0 = normal, >1.0 = heavy traffic

class GraphNetwork:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self._init_mock_data()

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_edge(self, u_id, v_id, distance, traffic=1.0):
        if u_id in self.nodes and v_id in self.nodes:
            self.edges.append(Edge(self.nodes[u_id], self.nodes[v_id], distance, traffic))
            # Undirected graph for simplicity, add reverse edge
            self.edges.append(Edge(self.nodes[v_id], self.nodes[u_id], distance, traffic))

    def _init_mock_data(self):
        # Create a simple city grid for Coimbatore
        # Nodes: 0 (Gandhipuram), 1 (Ukkadam), 2 (RS Puram), 3 (Brookefields), 
        #        4 (Peelamedu), 5 (Saravanampatti - Charging), 6 (Tidel Park)

        # Coordinates are approximate relative x,y for graph calc (not exact lat/long here, but consistent with real world topology)
        self.add_node(Node(0, "Gandhipuram", 0, 0))          # Center
        self.add_node(Node(1, "Ukkadam", 2, -5))             # South
        self.add_node(Node(2, "RS Puram", -3, 1))            # West
        self.add_node(Node(3, "Brookefields Mall", -1, -2))  # Near Center/West
        self.add_node(Node(4, "Peelamedu", 8, 2))            # East (Airport road)
        self.add_node(Node(5, "Saravanampatti", 6, 8, is_charging_station=True)) # North-East (Tech hub)
        self.add_node(Node(6, "Tidel Park", 12, 3))          # Far East

        # Edges (approx dist km)
        self.add_edge(0, 1, 4, 1.5)  # Gandhipuram -> Ukkadam (Heavy Traffic)
        self.add_edge(0, 2, 3, 1.0)  # Gandhipuram -> RS Puram
        self.add_edge(0, 4, 6, 1.2)  # Gandhipuram -> Peelamedu (Avinashi Rd)
        self.add_edge(0, 5, 8, 1.1)  # Gandhipuram -> Saravanampatti (Sathy Rd)
        
        self.add_edge(1, 3, 3, 1.2)  # Ukkadam -> Brookefields
        self.add_edge(2, 3, 2, 1.0)  # RS Puram -> Brookefields
        self.add_edge(3, 0, 2, 1.5)  # Brookefields -> Gandhipuram (Cross Cut/100ft)

        self.add_edge(4, 6, 5, 1.0)  # Peelamedu -> Tidel Park
        self.add_edge(4, 5, 7, 1.0)  # Peelamedu -> Saravanampatti
        self.add_edge(5, 6, 9, 1.0)  # Saravanampatti -> Tidel Park (Ring roadish)

    def get_neighbors(self, node_id):
        neighbors = []
        for edge in self.edges:
            if edge.start_node.id == node_id:
                neighbors.append((edge.end_node, edge))
        return neighbors

    def get_node(self, node_id):
        return self.nodes.get(node_id)
