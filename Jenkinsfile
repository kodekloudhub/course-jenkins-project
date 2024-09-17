pipeline {
    agent any
    parameters {
        string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'Specify the environment for deployment')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: "Run Tests in pipeline")
    
    }


    stages {


        stage('test') {
            when {
                expression {
                    params.RUN_TESTS == true
                }
            }
            steps {
                echo "testing application"
            }
        }
        stage('Deploy') {
            steps {
                echo "deploying to ${params.Environment} environment"
                
            }
        }    

        
            
    }
}