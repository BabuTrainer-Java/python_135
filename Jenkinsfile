pipeline {
    agent {
        label 'windows' // Replace 'windows' with your actual node label
    }
    environment {
        PYTHON_ENV ='C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python312\\' 
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository
                git 'https://github.com/your-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                bat "${env.PYTHON_ENV}\\Scripts\\pip install -r requirements.txt"
            }
        }
        stage('Run Python Script') {
            steps {
                // Run your Python script
                bat "${env.PYTHON_ENV}\\Scripts\\python demo.py"
            }
        }
    
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }

}
}
