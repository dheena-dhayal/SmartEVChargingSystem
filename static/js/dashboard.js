document.addEventListener('DOMContentLoaded', function () {

    function updateDashboard() {
        const searchInput = document.getElementById('location-search');
        let url = '/user/api/stats';
        if (searchInput && searchInput.value.trim() !== '') {
            url += `?location=${encodeURIComponent(searchInput.value.trim())}`;
        }
        
        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Battery Animation
                const batteryFill = document.getElementById('battery-fill');
                const batteryPercent = document.getElementById('battery-percent');

                batteryPercent.textContent = data.battery_level;
                batteryFill.style.width = data.battery_level + '%';
                batteryFill.textContent = data.battery_level + '%';

                // Status
                document.getElementById('charging-status').textContent = data.charging_status;
                document.getElementById('time-remaining').textContent = Math.round(data.time_remaining) + ' min';

                // Energy & Cost
                document.getElementById('energy-consumed').textContent = data.energy_consumed;
                document.getElementById('session-cost').textContent = data.cost;

                // Smart Optimization
                const gridLoadEl = document.getElementById('grid-load');
                gridLoadEl.textContent = data.grid_load;
                gridLoadEl.className = 'badge ' + (
                    data.grid_load === 'High' ? 'bg-danger' :
                        data.grid_load === 'Medium' ? 'bg-warning text-dark' : 'bg-success'
                );

                document.getElementById('best-slot').textContent = data.best_slot;

                // Render Charger Grid
                const grid = document.getElementById('charger-grid');
                grid.innerHTML = '';

                if (data.stations) {
                    data.stations.forEach(station => {
                        const box = document.createElement('div');
                        const statusClass = station.status.toLowerCase(); // available, occupied, maintenance
                        const statusIcon = statusClass === 'available' ? 'bi-check-circle-fill' :
                            statusClass === 'occupied' ? 'bi-ev-station-fill' : 'bi-cone-striped';

                        box.className = `charger-box ${statusClass}`;
                        box.innerHTML = `
                            <h4>${station.name}</h4>
                            <div class="text-muted small mb-2"><i class="bi bi-geo-alt-fill text-danger"></i> ${station.location || 'Unknown'}</div>
                            <i class="bi ${statusIcon} fs-1 mb-2 d-block"></i>
                            <span class="badge rounded-pill bg-light text-dark shadow-sm">${station.status}</span>
                            <small class="d-block mt-2 text-muted">${station.power} kW</small>
                            ${statusClass === 'available' ? '<div class="mt-3 text-success small fw-bold"><i class="bi bi-hand-index-thumb"></i> Click to Book</div>' : ''}
                        `;

                        if (statusClass === 'available') {
                            box.onclick = () => {
                                window.location.href = `/user/book?station_id=${station.id}`;
                            };
                        }

                        grid.appendChild(box);
                    });
                }
            })
            .catch(error => console.error('Error fetching stats:', error));
    }

    // Initial call
    updateDashboard();

    // Handle Ideal Target Change dynamically
    const idealTargetSelect = document.getElementById('user-ideal-target');
    const idealMarker = document.getElementById('ideal-battery-marker');
    const idealLabel = document.getElementById('ideal-battery-label');

    idealTargetSelect.addEventListener('change', function () {
        const val = this.value;
        idealMarker.style.left = val + '%';
        idealMarker.title = `Target Charge Level (${val}%)`;
        idealLabel.style.left = val + '%';
        idealLabel.textContent = `${val}% Target`;
    });

    // Update every 3 seconds
    setInterval(updateDashboard, 3000);
    
    // Trigger update on search text change
    const searchInput = document.getElementById('location-search');
    if (searchInput) {
        searchInput.addEventListener('input', updateDashboard);
    }
});
