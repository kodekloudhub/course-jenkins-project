pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sanjeevkt720/jenkins-flask-app'
        IMAGE_TAG_COMMIT = "${IMAGE_NAME}:${env.GIT_COMMIT}"
        IMAGE_TAG_RELEASE = "${IMAGE_NAME}:${GIT_TAG}"
        
    }

    
    stages {
        stage('Setup') {
            steps {
                script {
                    echo "${IMAGE_TAG_COMMIT}"
                    echo "${IMAGE_TAG_RELEASE}"
                    env.GIT_TAG = '1.1.1'
                    echo "${IMAGE_TAG_COMMIT}"
                    echo "${IMAGE_TAG_RELEASE}"
                }

            }
        }
   
    }
}