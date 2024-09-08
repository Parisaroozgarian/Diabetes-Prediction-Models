from flask import Flask, render_template, jsonify, request
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
import pandas as pd

app = Flask(__name__)

# Load the dataset
def load_data():
    data = pd.read_csv('/Users/macbook12/Desktop/diabetes/diabetes.csv')
    x = data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
    y = data['Outcome']
    return train_test_split(x, y, test_size=0.2, random_state=0)

# Evaluate model
def evaluate_model(clf, x_train, x_test, y_train, y_test):
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return {
        'f1_score': f1_score(y_test, y_pred, average='weighted'),
        'accuracy': accuracy_score(y_test, y_pred)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-model', methods=['POST'])
def run_model():
    x_train, x_test, y_train, y_test = load_data()
    data = request.get_json()
    
    model_type = data.get('model_type')
    params = data.get('params', {})

    if model_type == 'decision_tree':
        max_depth = params.get('max_depth', None)
        dt = DecisionTreeClassifier(max_depth=int(max_depth) if max_depth else None)
        result = evaluate_model(dt, x_train, x_test, y_train, y_test)

    elif model_type == 'knn':
        n_neighbors = params.get('n_neighbors', 5)
        knn = KNeighborsClassifier(n_neighbors=int(n_neighbors))
        result = evaluate_model(knn, x_train, x_test, y_train, y_test)

    elif model_type == 'logistic_regression':
        lr = LogisticRegression(max_iter=1000)
        result = evaluate_model(lr, x_train, x_test, y_train, y_test)

    elif model_type == 'svm':
        svm_model = svm.SVC(kernel='linear')
        result = evaluate_model(svm_model, x_train, x_test, y_train, y_test)

    else:
        return jsonify({'error': 'Invalid model type'}), 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
