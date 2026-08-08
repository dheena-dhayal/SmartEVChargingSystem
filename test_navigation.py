import urllib.request
import json
import time

def test_route_plan():
    url = 'http://127.0.0.1:5000/navigation/plan'
    payload = {
        'start_id': 0,
        'end_id': 6,
        'current_soc': 15 
    }
    
    print(f"Testing Route Planner (Target: {url})")
    print(f"Scenario: Driving from Home(0) to Office(6) with 15% Battery")
    print("-" * 50)
    
    try:
        req = urllib.request.Request(
            url, 
            data=json.dumps(payload).encode('utf-8'), 
            headers={'Content-Type': 'application/json'}
        )
        
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            
        print("✅ SUCCESS: Route Calculated by AI Agent")
        print(f"Estimated Time: {result['estimated_time']} mins")
        print(f"Final SOC: {result['final_soc']}%")
        print("Route Path:")
        for i, step in enumerate(result['route']):
            print(f"  {i+1}. {step}")
            
    except Exception as e:
        print(f"❌ FAILED: {e}")

if __name__ == "__main__":
    time.sleep(2)
    try:
        print("Checking server health...")
        with urllib.request.urlopen("http://127.0.0.1:5000/") as r:
            print(f"Server is UP: {r.status}")
    except Exception as e:
        print(f"Server is DOWN: {e}")
        exit(1)
        
    test_route_plan()
