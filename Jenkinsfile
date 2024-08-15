pipeline {
    agent any

    options {
        timeout(time: 1, unit: 'MINUTES')
    }
    

    stages {

        stage('lint and format') {
            steps {
                sh "sleep 70"
            }
        }


        stage('Setup') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'server-creds', usernameVariable: "myuser", passwordVariable: "mypassword")]) {

                    sh '''
                    echo ${myuser}
                    echo ${mypassword}
                    '''
                }

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