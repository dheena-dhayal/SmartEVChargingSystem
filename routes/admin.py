from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.before_request
@login_required
def require_admin():
    if current_user.role != 'admin':
        return "Unauthorized", 403

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/api/analytics')
@login_required
def analytics():
    if current_user.role != 'admin':
        return {"error": "Unauthorized"}, 403
        
    import random
    
    # Mock Data for Analytics
    # In a real app, this would query the Booking database
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    energy_data = [random.randint(50, 200) for _ in days]
    
    peak_hours = [random.randint(5, 20) for _ in range(8)]
    
    return {
        'days': days,
        'energy_usage': energy_data,
        'peak_hours': peak_hours,
        'active_users': random.randint(10, 50),
        'total_sessions': random.randint(100, 500)
    }
