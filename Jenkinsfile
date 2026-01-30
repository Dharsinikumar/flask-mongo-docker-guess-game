pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-guess-game .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-guess-game || true
                docker run -d -p 5000:5000 --name flask-guess-game flask-guess-game
                '''
            }
        }
    }
}
