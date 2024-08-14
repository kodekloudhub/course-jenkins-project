pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sanjeevkt720/jenkins-flask-app'
        IMAGE_TAG = "${IMAGE_NAME}:${env.GIT_COMMIT}"
        RELEASE_TAG = "0.1.0"
        KUBECONFIG = credentials('kubeconfig-credentials-id')
        
    }

    
    stages {


        stage('Setup') {
            steps {
                sh "git tag -a ${RELEASE_TAG} -m 'Taggign commit ${env.GIT_COMMIT}'"

            }
        }
        stage('Test') {
            steps {
                sh "poetry run pytest"
            }
        }

        stage('Login to docker hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh 'echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin'}
                echo 'Login successfully'
            }
        }

        stage('Build Docker Image')
        {
            steps
            {
                sh 'docker build -t ${IMAGE_TAG} -t ${RELEASE_TAG} .'
                echo "Docker image build successfully"
                sh 'docker image ls'
                
            }
        }
    
        
    }
}