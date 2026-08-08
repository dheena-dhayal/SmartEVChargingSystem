from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import Vehicle, Booking, Station
from database import db
from services.optimizer import find_best_slot

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html')

@user_bp.route('/vehicles', methods=['GET', 'POST'])
@login_required
def vehicles():
    if request.method == 'POST':
        model = request.form.get('model')
        capacity = float(request.form.get('capacity'))
        vehicle = Vehicle(user_id=current_user.id, model=model, battery_capacity=capacity)
        db.session.add(vehicle)
        db.session.commit()
        flash('Vehicle added!')
    return render_template('user/vehicles.html')

@user_bp.route('/book', methods=['GET', 'POST'])
@login_required
def book_slot():
    if request.method == 'POST':
        # Logic for booking will go here
        pass
    stations = Station.query.all()
    return render_template('user/book_slot.html', stations=stations)

@user_bp.route('/api/stats')
@login_required
def get_stats():
    import random
    from services.optimizer import get_grid_load, find_best_slot
    
    # Real data
    location_query = request.args.get('location', '')
    if location_query:
        stations = Station.query.filter(Station.location.ilike(f'%{location_query}%')).all()
    else:
        stations = Station.query.all()
        
    total_stations = len(stations)
    available_stations = sum(1 for s in stations if s.status == 'Available')
    
    # Grid & Optimization
    grid_load = get_grid_load()
    best_slot = find_best_slot()
    
    # Station Grid Data
    station_data = [{
        'id': s.id,
        'name': s.name,
        'status': s.status,
        'power': s.max_power_kw,
        'location': s.location
    } for s in stations]
    
    # Simulated User Session Data
    battery_level = random.randint(20, 95)
    charging_status = 'Charging' if battery_level < 90 else 'Completed'
    time_remaining = (100 - battery_level) * 1.5 
    energy_consumed = round(random.uniform(10.5, 50.0), 2)
    
    # Dynamic Cost Calculation
    # Assuming 1 hour of charge simulated
    from services.optimizer import calculate_cost
    cost = calculate_cost(1.0) 
    
    return {
        'total_stations': total_stations,
        'available_stations': available_stations,
        'occupied_stations': total_stations - available_stations,
        'battery_level': battery_level,
        'ideal_battery_level': 80,
        'charging_status': charging_status,
        'time_remaining': time_remaining,
        'energy_consumed': energy_consumed,
        'cost': cost,
        'grid_load': grid_load,
        'best_slot': best_slot,
        'stations': station_data
    }
