pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Dharsinikumar/flask-mongo-docker-guess-game.git'
            }
        }

        stage('Build & Start Containers') {
            steps {
                // Stop any old containers
                sh 'docker compose down || true'

                // Build and start both MongoDB + Flask
                sh 'docker compose up --build -d'
            }
        }
    }
}
