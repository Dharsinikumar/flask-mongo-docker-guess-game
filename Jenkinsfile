pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Dharsinikumar/flask-mongo-docker-guess-game.git'
            }
        }

        stage('Build & Up Docker') {
            steps {
                script {
                    sh 'docker-compose -f $DOCKER_COMPOSE_FILE up --build -d'
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    sh '''
                        echo "Waiting 20s for Mongo & Flask to start..."
                        sleep 20
                        docker ps
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
