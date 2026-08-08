from services.rl_agent import RouteOptimizer
import time

def demo_agent():
    print("Initializing Deep Q-Learning Agent...")
    optimizer = RouteOptimizer()
    
    start_id = 0 # Gandhipuram
    end_id = 6   # Tidel Park
    soc = 15     # Low Battery
    
    print(f"\n🚀 Scenario: Navigate Gandhipuram -> Tidel Park with {soc}% Battery")
    print("--------------------------------------------------")
    
    start_time = time.time()
    result = optimizer.find_optimal_route(start_id, end_id, soc)
    duration = time.time() - start_time
    
    print(f"✅ Route Found in {duration:.4f} seconds")
    print(f"Path: {result['route']}")
    print(f"Est. Time: {result['estimated_time']} mins")
    print(f"Final Battery: {result['final_soc']}%")
    
    if any("Charging" in step for step in result['route']):
         print("\n⚡ Intelligence Check: Agent correctly identified low battery and stopped to charge!")
    else:
         print("\n⚠️ Intelligence Check: Agent risked it without charging.")

if __name__ == "__main__":
    demo_agent()
