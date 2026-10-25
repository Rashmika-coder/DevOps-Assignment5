```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out application source code'
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                echo 'Checking Python application syntax'
                bat 'python --version'
                bat 'python -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                bat 'docker build -t supermarket-app:1.0 .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                echo 'Verifying Docker image'
                bat 'docker image inspect supermarket-app:1.0'
                bat 'docker images supermarket-app'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully'
        }
        failure {
            echo 'CI pipeline failed. Check the console output.'
        }
    }
}
```
