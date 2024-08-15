pipeline {
    agent any


    

    stages {

        stage('lint and format') {
            parallel {
                stages {
                    stage('linting'){
                        steps {
                            sh "sleep 30"
                        }
                    }

                    stage('formatting'){
                        steps {
                            sh "sleep 30"
                        }
                    }
                }
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