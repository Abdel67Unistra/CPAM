// JavaScript principal pour CPAM Analytics
class CPAMAnalytics {
    constructor() {
        this.apiBase = 'api/';
        this.initializeRealTimeData();
        this.initializeMiniCharts();
    }

    // Initialise les données en temps réel
    async initializeRealTimeData() {
        try {
            await this.updateRealTimeStats();
            // Mise à jour toutes les 30 secondes
            setInterval(() => this.updateRealTimeStats(), 30000);
        } catch (error) {
            console.log('Mode démo - données simulées');
            this.simulateRealTimeData();
        }
    }

    // Simule les données en temps réel
    simulateRealTimeData() {
        setInterval(() => {
            const budget = 41500 + Math.random() * 100 - 50;
            const actes = 13200000 + Math.floor(Math.random() * 10000);
            const fraudes = 2350 + Math.floor(Math.random() * 50);
            const delai = 9.5 + Math.random() * 2 - 1;

            this.updateStatDisplay('stat-budget', budget.toFixed(0));
            this.updateStatDisplay('stat-actes', actes.toLocaleString());
            this.updateStatDisplay('stat-fraudes', fraudes);
            this.updateStatDisplay('stat-delai', delai.toFixed(1));
        }, 3000);
    }

    // Met à jour l'affichage des statistiques
    updateStatDisplay(elementId, value) {
        const element = document.getElementById(elementId);
        if (element) {
            element.textContent = value;
            element.style.animation = 'pulse 0.5s ease-in-out';
            setTimeout(() => {
                element.style.animation = '';
            }, 500);
        }
    }

    // Met à jour les statistiques en temps réel
    async updateRealTimeStats() {
        try {
            const response = await fetch(this.apiBase + 'stats');
            const data = await response.json();
            
            this.updateStatDisplay('stat-budget', data.budget);
            this.updateStatDisplay('stat-actes', data.actes);
            this.updateStatDisplay('stat-fraudes', data.fraudes);
            this.updateStatDisplay('stat-delai', data.delai);
        } catch (error) {
            // Fallback vers données simulées
            this.simulateRealTimeData();
        }
    }

    // Initialise les mini-graphiques
    initializeMiniCharts() {
        if (document.getElementById('mini-chart-depenses')) {
            this.createMiniChart('mini-chart-depenses', 'doughnut', [12000, 9500, 15000, 3000, 2000]);
        }
        if (document.getElementById('mini-chart-actes')) {
            this.createMiniChart('mini-chart-actes', 'pie', [8500, 1200, 900, 1500, 1100]);
        }
        if (document.getElementById('mini-chart-prevision')) {
            this.createMiniChart('mini-chart-prevision', 'line', [42000, 43000, 44500, 46000, 47500]);
        }
        if (document.getElementById('mini-chart-fraudes')) {
            this.createMiniChart('mini-chart-fraudes', 'bar', [1200, 800, 350]);
        }
    }

    // Crée un mini-graphique
    createMiniChart(elementId, type, data) {
        const ctx = document.getElementById(elementId);
        if (!ctx) return;

        new Chart(ctx, {
            type: type,
            data: {
                labels: type === 'line' ? ['2021', '2022', '2023', '2024', '2025'] : [],
                datasets: [{
                    data: data,
                    backgroundColor: [
                        '#0055a4', '#0077c2', '#0099e5', '#00bbf1', '#00ddff'
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: type === 'line' ? {
                    x: { display: false },
                    y: { display: false }
                } : {}
            }
        });
    }

    // Exécute un script Python
    async runPythonScript(scriptName, params = {}) {
        try {
            const response = await fetch(this.apiBase + 'python/' + scriptName, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(params)
            });
            
            const result = await response.json();
            return result;
        } catch (error) {
            console.error('Erreur script Python:', error);
            return { error: 'Erreur lors de l\'exécution du script' };
        }
    }

    // Exécute un script R
    async runRScript(scriptName, params = {}) {
        try {
            const response = await fetch(this.apiBase + 'r/' + scriptName, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(params)
            });
            
            const result = await response.json();
            return result;
        } catch (error) {
            console.error('Erreur script R:', error);
            return { error: 'Erreur lors de l\'exécution du script R' };
        }
    }

    // Charge des données CSV
    async loadCSVData(filename) {
        try {
            const response = await fetch('data/' + filename);
            const text = await response.text();
            return this.parseCSV(text);
        } catch (error) {
            console.error('Erreur chargement CSV:', error);
            return null;
        }
    }

    // Parse les données CSV
    parseCSV(text) {
        const lines = text.trim().split('\n');
        const headers = lines[0].split(',');
        const data = [];
        
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',');
            const row = {};
            headers.forEach((header, index) => {
                row[header] = values[index];
            });
            data.push(row);
        }
        
        return { headers, data };
    }

    // Met à jour un graphique
    updateChart(chart, newData) {
        chart.data.datasets[0].data = newData;
        chart.update();
    }

    // Crée un graphique Plotly
    createPlotlyChart(elementId, data, layout) {
        Plotly.newPlot(elementId, data, layout, {
            responsive: true,
            displayModeBar: true
        });
    }
}

// Utilitaires pour les animations
function addPulseAnimation() {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
    `;
    document.head.appendChild(style);
}

// Initialisation
document.addEventListener('DOMContentLoaded', function() {
    addPulseAnimation();
    window.cpamAnalytics = new CPAMAnalytics();
    
    // Active les tooltips et autres interactions
    initializeTooltips();
});

function initializeTooltips() {
    // Ajoute des tooltips aux éléments avec data-tooltip
    document.querySelectorAll('[data-tooltip]').forEach(element => {
        element.addEventListener('mouseenter', function() {
            showTooltip(this, this.getAttribute('data-tooltip'));
        });
        
        element.addEventListener('mouseleave', function() {
            hideTooltip();
        });
    });
}

function showTooltip(element, text) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = text;
    tooltip.style.cssText = `
        position: absolute;
        background: #333;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 12px;
        z-index: 1000;
        pointer-events: none;
    `;
    
    document.body.appendChild(tooltip);
    
    const rect = element.getBoundingClientRect();
    tooltip.style.left = rect.left + 'px';
    tooltip.style.top = (rect.top - tooltip.offsetHeight - 5) + 'px';
}

function hideTooltip() {
    const tooltip = document.querySelector('.tooltip');
    if (tooltip) {
        tooltip.remove();
    }
}
