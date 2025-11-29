pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'Всё собралось'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker compose exec app python -m pytest -v'
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