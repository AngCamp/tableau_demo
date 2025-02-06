// simulation-page.js
let currentSimulation = null;

async function runSimulation() {
    const params = {
        mean: parseFloat(document.getElementById('meanInput').value) || 0,
        effect_size: parseFloat(document.getElementById('effectInput').value) || 0,
        n_points: parseInt(document.getElementById('nPointsInput').value) || 100
    };
    
    try {
        const response = await fetch('/simulate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(params)
        });
        currentSimulation = await response.json();
        document.getElementById('result').innerText = JSON.stringify(currentSimulation, null, 2);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function saveSimulation() {
    if (!currentSimulation) return;
    
    try {
        const response = await fetch(`/save/${currentSimulation.id}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(currentSimulation)
        });
        const result = await response.json();
        console.log('Save status:', result.status);
    } catch (error) {
        console.error('Error saving:', error);
    }
}

document.getElementById('runSimBtn').addEventListener('click', runSimulation);
document.getElementById('saveSimBtn').addEventListener('click', saveSimulation);
