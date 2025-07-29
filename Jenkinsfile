pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/silvaman47/task-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-api .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm --entrypoint "" task-api pytest'
            }
        }

        stage('Run') {
            steps {
                // Optional cleanup
                sh 'docker rm -f task-api-app || true'
                sh 'docker run -d -p 5000:5000 --name task-api-app task-api'
            }
        }
    }
}
