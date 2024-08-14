pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sanjeevkt720/jenkins-flask-app'
        IMAGE_TAG = "${IMAGE_NAME}:${env.GIT_COMMIT}"
        RELEASE_TAG = "0.1.4"
        KUBECONFIG = credentials('kubeconfig-credentials-id')
        GIT_TAG = ''
        
    }

    
    stages {

        stage("Check for Git Tag") {
            steps {
                script {
                    def tag = sh(returnStdout: true, script: "git tag --contains").trim()
                    if (tag != null && tag =~ /^v[0-9]+\\.[0-9]+\\.[0-9]+$/) {

                        env.GIT_TAG = tag
                     
                    }
                    echo "${GIT_TAG}"
                }
            }
        }   

        stage("blah") {
            when {
                expression {
                    return GIT_TAG != "" // Only run if GIT_TAG is not empty
                }
            }

            steps {
                echo "yeah we detected a tag: ${GIT_TAG}"

            }
        }


        stage('Setup') {
            steps {
                echo "My tags: ${GIT_TAG}"

                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    sh """
                        git config user.name 'jenkins'
                        git config user.email 'jenkins@example.com'
                    """
                }

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


    
        
    }
}