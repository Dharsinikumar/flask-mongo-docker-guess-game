pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dharsinikumar/flask-mongo-docker-guess-game.git'
            }
        }

        stage('Build & Start Containers') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up --build -d'
            }
        }
    }

    post {
        always {
            emailext(
                to: 'dharsinikumar23@gmail.com',
                subject: "Jenkins Build: ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: """
                    <h2>Build Status: ${currentBuild.currentResult}</h2>
                    <p>Job: ${env.JOB_NAME}</p>
                    <p>Build Number: ${env.BUILD_NUMBER}</p>
                    <p>Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                mimeType: 'text/html'
            )
        }
    }
}
