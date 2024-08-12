pipeline {
    agent any

    
    stages {

        stage('Setup') {
            steps {
                sh "pip install -r lambda-app/tests/requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "pytest"
            }
        }

        stage('Build') {
            steps {
                sh "sam build"

            }
        }
        stage('Deploy') {

            environment {
                AWS_ACCESS_KEY_ID = credentials('aws-access-key')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
            }
            
            steps {
                sh "sam deploy --no-confirm-changeset --no-fail-on-empty-changeset"

            }
        }
      
    }
}