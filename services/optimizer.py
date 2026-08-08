from datetime import datetime, time

def get_grid_load():
    """
    Simulates grid load based on time of day.
    Returns: 'Low', 'Medium', 'High'
    """
    now = datetime.now().time()
    
    # Peak hours: 6 PM - 10 PM
    if time(18, 0) <= now <= time(22, 0):
        return 'High'
    # Medium hours: 8 AM - 6 PM
    elif time(8, 0) <= now < time(18, 0):
        return 'Medium'
    # Off-peak: 10 PM - 8 AM
    else:
        return 'Low'

def calculate_cost(duration_hours):
    """
    Calculates cost based on dynamic pricing.
    Base Rate: $0.15 / kWh
    Peak Multiplier: 1.5x
    """
    base_rate = 0.15
    load = get_grid_load()
    
    if load == 'High':
        rate = base_rate * 1.5
    elif load == 'Medium':
        rate = base_rate * 1.2
    else:
        rate = base_rate * 0.8  # Discount for off-peak
        
    # Avg EV charging speed assumption: 11kW per hour
    avg_power = 11.0 
    
    estimated_cost = duration_hours * avg_power * rate
    return round(estimated_cost, 2)

def find_best_slot():
    """
    Suggests the next best time slot for cost efficiency.
    """
    load = get_grid_load()
    if load == 'Low':
        return "Now (Best Rate!)"
    elif load == 'High':
        return "After 10:00 PM"
    else:
        return "After 10:00 PM (or Now for standard rate)"
