pipeline{
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('demo') {
            steps {
                sh 'python demo.py'
            }
        }
    }
}

