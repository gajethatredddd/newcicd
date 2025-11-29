pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker compose run --rm fastapi_app python -m pytest -v'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker compose down'
                sh 'docker compose up -d'
            }
        }
    }
    
    post {
        always {
            echo 'Пайплайн завершен!'
        }
    }
}