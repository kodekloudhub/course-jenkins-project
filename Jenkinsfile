pipeline {
    agent any

    

    stages {

        stage('Setup') {

        environment {
            DB_HOST = '192.168.12.1'
            USERNAME = 'user1'
            PASSWORD = 'password123'
        }
            steps {
                sh "pip install -r requirements.txt"
                echo "The Database IP is: ${DB_HOST}"
            }
        }
        stage('Test') {
            steps {
                sh "pytest"
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }    
            
    }
}