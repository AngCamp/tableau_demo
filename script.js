// script.js
document.addEventListener("DOMContentLoaded", function () {
    const goBtn = document.getElementById("goBtn");
    if (goBtn) {
        goBtn.addEventListener("click", function() {
            window.location.href = "./simulate_page.html";
        });
    }
});

async function runSimulation() {
    try {
        const response = await fetch('/simulate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({n_points: 100})
        });
        const data = await response.json();
        document.getElementById('result').innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error:', error);
    }
}

document.getElementById('runSimBtn')?.addEventListener('click', runSimulation);
