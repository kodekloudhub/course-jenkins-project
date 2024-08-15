pipeline {
    agent any

    environment {
        SERVER_HOST = '192.168.12.1'
        USERNAME = 'user1'
        PASSWORD = 'password123'
    }

    stages {

        stage('Setup') {
            steps {
                sh "pip install -r requirements.txt"
                echo 'The Server IP is ${SERVER_HOST}'
            }
        }
        stage('Test') {
            steps {
                sh "pytest"
                echo 'Server Username: ${USERNAME} Password: ${PASSWORD}'
            }
        }    
            
    }
}