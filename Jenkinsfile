pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Dharsinikumar/flask-mongo-docker-guess-game.git'
            }
        }
        stage('Build & Start Containers') {
            steps {
                sh 'docker compose down'
                sh 'docker compose up --build -d'
            }
        }
    }
}
