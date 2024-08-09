pipeline {
    agent any

    environment {
        SERVER_IP = credentials('prod-server-ip')
    }
    stages {
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

        stage('Package code') {
            steps {
                sh "zip -r myapp.zip ./* -x '*.git*' -x"
            }
        }

        stage('Deploy to Prod') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh-key', keyFileVariable: 'MY_SSH_KEY', usernameVariable: 'username')]) {
                    sh '''
                    scp -i $MY_SSH_KEY -o StrictHostKeyChecking=no myapp.zip  ${username}@${env.SERVER_IP}:/home/ec2-user/app/
                    ssh -i $MY_SSH_KEY -o StrictHostKeyChecking=no ${username}@${env.SERVER_IP} << EOF
                    unzip /home/ec2-user/app/myapp.zip
                    systemctl restart flaskapp.service
                    '''
                }
            }
        }
       
        
       
        
    }
}