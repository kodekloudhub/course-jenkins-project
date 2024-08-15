pipeline {
    agent any

    environment {
        SERVER_IP = credentials('prod-server-ip')
    }
    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/kodekloudhub/jenkins-project.git', branch: 'main'
                sh "ls -ltr"
            }
        }

        
        stage('Setup') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                sh "pytest"
            }
        }    
            
    }
}