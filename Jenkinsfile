pipeline {
    agent any

    
    stages {
        stage('Install SAM CLI') {
            steps {
                sh "wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip"
                sh "unzip aws-sam-cli-linux-x86_64.zip -d sam-installation"
                sh "sudo ./sam-installation/install"
                sh "sam --version"
            }
        }
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