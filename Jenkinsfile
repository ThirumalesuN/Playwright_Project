
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"C:\\Users\\THIRU\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pip install -r Tests\\requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }
    }
}
