pipeline {
    agent any


    

    stages {
        stage('build and lint'){
            stages {
                stage('build') {
                    echo "running build nested stage"
                }

                stage('lint') {
                    echo "running lint nested stage"
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