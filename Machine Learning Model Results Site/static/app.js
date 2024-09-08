document.getElementById('run-models').addEventListener('click', () => {
    console.log('Run Models button clicked');

    const modelType = document.querySelector('input[name="model"]:checked').value;
    const params = {};

    if (modelType === 'knn') {
        const knnNeighbors = document.getElementById('knn-n-neighbors').value;
        if (knnNeighbors) params.n_neighbors = knnNeighbors;
    }

    if (modelType === 'decision_tree') {
        const treeMaxDepth = document.getElementById('tree-max-depth').value;
        if (treeMaxDepth) params.max_depth = treeMaxDepth;
    }

    fetch('/run-model', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ model_type: modelType, params: params })
    })
    .then(response => response.json())
    .then(data => {
        const formatNumber = num => num ? num.toFixed(2) : 'N/A';

        if (modelType === 'decision_tree') {
            document.getElementById('decision-tree-results').textContent = 
                `F1 Score: ${formatNumber(data.f1_score)}, Accuracy: ${formatNumber(data.accuracy)}`;
            document.getElementById('decision-tree-card').classList.remove('hidden');
        }

        if (modelType === 'knn') {
            document.getElementById('knn-results').textContent = 
                `F1 Score: ${formatNumber(data.f1_score)}, Accuracy: ${formatNumber(data.accuracy)}`;
            document.getElementById('knn-card').classList.remove('hidden');
        }

        if (modelType === 'logistic_regression') {
            document.getElementById('logistic-regression-results').textContent = 
                `F1 Score: ${formatNumber(data.f1_score)}, Accuracy: ${formatNumber(data.accuracy)}`;
            document.getElementById('logistic-regression-card').classList.remove('hidden');
        }

        if (modelType === 'svm') {
            document.getElementById('svm-results').textContent = 
                `F1 Score: ${formatNumber(data.f1_score)}, Accuracy: ${formatNumber(data.accuracy)}`;
            document.getElementById('svm-card').classList.remove('hidden');
        }
    })
    .catch(error => console.error('Error fetching data:', error));
});
