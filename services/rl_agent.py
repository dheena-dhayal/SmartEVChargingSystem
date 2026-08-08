import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from models.graph_network import GraphNetwork

# Hyperparameters
GAMMA = 0.99
EPSILON = 0.1
LR = 0.001

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

class DQNAgent:
    def __init__(self, state_dim, action_dim):
        self.action_dim = action_dim
        self.model = DQN(state_dim, action_dim)
        self.optimizer = optim.Adam(self.model.parameters(), lr=LR)
        self.criterion = nn.MSELoss()

    def get_action(self, state):
        # Epsilon-greedy implementation
        if random.random() < EPSILON:
            return random.randint(0, self.action_dim - 1)
        
        with torch.no_grad():
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            q_values = self.model(state_tensor)
            return torch.argmax(q_values).item()

    def train_step(self, state, action, reward, next_state, done):
        state = torch.FloatTensor(state).unsqueeze(0)
        next_state = torch.FloatTensor(next_state).unsqueeze(0)
        action = torch.LongTensor([action])
        reward = torch.FloatTensor([reward])
        
        q_value = self.model(state).gather(1, action.unsqueeze(1)).squeeze(1)
        next_q_value = self.model(next_state).max(1)[0]
        expected_q_value = reward + GAMMA * next_q_value * (1 - done)
        
        loss = self.criterion(q_value, expected_q_value.detach())
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

class RouteOptimizer:
    def __init__(self):
        self.graph = GraphNetwork()
        # State: [Current_Node_ID, Destination_Node_ID, SoC, Current_Traffic_Level]
        self.state_dim = 4
        # Actions: Max possible neighbors (simplified to fixed size for demo, say 10)
        self.action_dim = 10 
        self.agent = DQNAgent(self.state_dim, self.action_dim)

    def find_optimal_route(self, start_id, end_id, initial_soc):
        """
        Simulates a navigation episode using the DQN agent to find a path.
        In a real scenario, this would search the graph using Q-values.
        For this simplified demo, we use a heuristic guided by the "trained" network 
        (or just the graph logic if untrianed).
        """
        current_node = self.graph.get_node(start_id)
        path = [current_node.name]
        total_time = 0
        current_soc = initial_soc
        
        # Simple Greedy Search with "AI" heuristics (mocking the inference loop)
        visited = set()
        visited.add(current_node.id)
        
        step_limit = 20 # Safety break
        steps = 0

        while current_node.id != end_id and steps < step_limit:
            steps += 1
            neighbors = self.graph.get_neighbors(current_node.id)
            if not neighbors:
                break
            
            # Select best neighbor (Mocking AI selection based on minimize Cost)
            best_score = float('inf')
            best_edge = None
            best_neighbor = None

            for neighbor, edge in neighbors:
                if neighbor.id in visited:
                    continue # Skip visited nodes to prevent cycles

                # Cost function: Time + Energy Penalty
                # Time = Distance * Traffic
                travel_time = edge.distance * edge.traffic_factor
                energy_cost = edge.distance * 0.5 # kWh per unit distance
                
                score = travel_time
                
                # AI Logic: If SoC is low, prioritize charging stations
                if current_soc < 20: 
                    if neighbor.is_charging_station:
                        score -= 50 # Huge incentive to go here
                    else:
                        score += 100 # Penalty for risking it
                        
                if score < best_score:
                    best_score = score
                    best_edge = edge
                    best_neighbor = neighbor
            
            if best_neighbor:
                current_node = best_neighbor
                visited.add(current_node.id)
                path.append(current_node.name)
                current_soc -= best_edge.distance * 0.5
                total_time += best_edge.distance * best_edge.traffic_factor
                
                if current_node.is_charging_station and current_soc < 80:
                     # Simulate charging
                    current_soc = 90
                    path.append(f"Charging at {current_node.name}...")
            else:
                break # Dead end

        return {
            "route": path,
            "estimated_time": round(total_time, 2),
            "final_soc": round(current_soc, 1)
        }
