pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git branch: 'main', url: 'https://github.com/silvaman47/task-api.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t task-api .'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }
    stage('Run') {
      steps {
        sh 'docker run -d -p 5000:5000 task-api'
      }
    }
  }
}
