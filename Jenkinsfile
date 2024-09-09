pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sanjeevkt720/jenkins-flask-app'
        IMAGE_TAG_COMMIT = "${IMAGE_NAME}:${env.GIT_COMMIT}"
        
        
    }

    
    stages {
        stage('Setup') {
            steps {
                script {
                    echo "${IMAGE_TAG_COMMIT}"
                    env.GIT_TAG = '1.1.1'
                    env.IMAGE_TAG_RELEASE = "${IMAGE_NAME}:${env.GIT_TAG}"
                    echo "${IMAGE_TAG_COMMIT}"
                    echo "${IMAGE_TAG_RELEASE}"
                }

            }
        }

        stage('stage2') {
            steps {
                script {
                    echo "${IMAGE_TAG_COMMIT}"
                    echo "${IMAGE_TAG_RELEASE}"
                }

            }
        }
   
    }
}