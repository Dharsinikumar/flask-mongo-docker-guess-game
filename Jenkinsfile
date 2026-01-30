pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-guess-game .'
            }
        }

        stage('Run Containers') {
            steps {
                sh '''
                docker rm -f flask-guess-game || true
                docker rm -f mongodb || true

                docker run -d --name mongodb -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=admin123 mongo:6.0

                docker run -d --name flask-guess-game --link mongodb:mongodb -p 5000:5000 -e MONGO_URI=mongodb://admin:admin123@mongodb:27017 flask-guess-game
                '''
            }
        }
    }
}
