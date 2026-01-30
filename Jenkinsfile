pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build & Start Containers') {
            steps {
                sh '''
                # Stop and remove old containers if they exist
                docker-compose down

                # Build images and start containers in detached mode
                docker-compose up -d --build
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'  # Optional: see running containers
            }
        }
    }
}
