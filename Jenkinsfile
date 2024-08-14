pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sanjeevkt720/jenkins-flask-app'
        IMAGE_TAG = "${IMAGE_NAME}:${env.GIT_COMMIT}"
        RELEASE_TAG = "0.1.4"
        KUBECONFIG = credentials('kubeconfig-credentials-id')
   
        
    }
  
    stages {
        stage('Only Run if Pull Request') {

            when {
                    expression {
                        return env.action == 'opened'
                    }
                }
            steps {
                
                script {
                    echo "${env.action}"
                    sh "printenv"
                    echo "PR Has been opened: ${env.pullRequestNumber}"
                }
            }
        }

        


        stage('Test') {
            steps {
                sh "poetry run pytest"
            }
        }


        stage('tag') {
            steps {
                echo "My tags: ${GIT_TAG}"

                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    sh """
                        git config user.name 'jenkins'
                        git config user.email 'jenkins@example.com'
                        git tag -a ${RELEASE_TAG} -m 'Taggign commit ${env.GIT_COMMIT}'
                        git push https://${GITHUB_TOKEN}@github.com/kodekloudhub/course-jenkins-project ${RELEASE_TAG}
                    """
                }

            }
        }
        

        stage('Login to docker hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh 'echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin'}
                echo 'Login successfully'
            }
        }

        stage('Push Docker Image')
        {
            steps
            {
                sh 'docker push --all-tags ${IMAGE_NAME}'
                echo "Docker image push successfully"
            }
        }


    
        
    }
}