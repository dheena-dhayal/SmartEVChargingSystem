from flask import Blueprint, render_template, request, jsonify
from services.rl_agent import RouteOptimizer

navigation_bp = Blueprint('navigation', __name__)
optimizer = RouteOptimizer()

@navigation_bp.route('/')
def index():
    return render_template('navigation.html')

@navigation_bp.route('/plan', methods=['POST'])
def plan_route():
    data = request.get_json()
    start_id = int(data.get('start_id', 0))
    end_id = int(data.get('end_id', 6))
    current_soc = float(data.get('current_soc', 50.0))
    
    result = optimizer.find_optimal_route(start_id, end_id, current_soc)
    return jsonify(result)
