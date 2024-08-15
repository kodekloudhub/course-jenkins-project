pipeline {
    agent any


    

    stages {

        stage('lint and format') {
            stages {
                stage('linting'){
                    steps {
                        echo "linting code in nested stage"
                    }
                }

                stage('formatting'){
                    steps {
                       echo "formatting code in nested stage" 
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