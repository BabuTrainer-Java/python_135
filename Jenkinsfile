pipeline {
    agent any
    environment {
        // Define any environment variables here
        MY_VAR = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code
                git url: 'https://github.com/BabuTrainer-Java/python_135.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                // Build steps
                sh 'make build'
            }
        }
        stage('Test') {
            steps {
                // Test steps
                sh 'make test'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy steps
                sh 'make deploy'
            }
        }
    }
    post {
        always {
            // Cleanup actions
            cleanWs()
        }
        success {
            // Actions to perform on success
            echo 'Build succeeded!'
        }
        failure {
            // Actions to perform on failure
            echo 'Build failed!'
        }
    }
}
