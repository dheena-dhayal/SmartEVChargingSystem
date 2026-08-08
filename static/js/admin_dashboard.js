document.addEventListener('DOMContentLoaded', function () {
    fetch('/admin/api/analytics')
        .then(res => res.json())
        .then(data => {
            // Update Text Stats
            document.getElementById('total-energy').textContent = data.energy_usage.reduce((a, b) => a + b, 0) + ' kWh';
            document.getElementById('active-users').textContent = data.active_users;
            document.getElementById('total-sessions').textContent = data.total_sessions;

            // Energy Chart
            const ctxEnergy = document.getElementById('energyChart').getContext('2d');
            new Chart(ctxEnergy, {
                type: 'line',
                data: {
                    labels: data.days,
                    datasets: [{
                        label: 'Energy Consumed (kWh)',
                        data: data.energy_usage,
                        borderColor: '#2ecc71',
                        backgroundColor: 'rgba(46, 204, 113, 0.2)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { labels: { color: 'var(--text-color)' } }
                    },
                    scales: {
                        y: { ticks: { color: 'var(--text-color)' } },
                        x: { ticks: { color: 'var(--text-color)' } }
                    }
                }
            });

            // Peak Hours Chart
            const ctxPeak = document.getElementById('peakChart').getContext('2d');
            new Chart(ctxPeak, {
                type: 'bar',
                data: {
                    labels: ['6AM', '9AM', '12PM', '3PM', '6PM', '9PM', '12AM', '3AM'],
                    datasets: [{
                        label: 'Avg Active Sessions',
                        data: data.peak_hours,
                        backgroundColor: '#3498db'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { labels: { color: 'var(--text-color)' } }
                    },
                    scales: {
                        y: { ticks: { color: 'var(--text-color)' } },
                        x: { ticks: { color: 'var(--text-color)' } }
                    }
                }
            });
        })
        .catch(err => console.error('Error loading analytics:', err));
});
