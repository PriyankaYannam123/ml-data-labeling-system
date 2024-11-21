pipeline {
    agent any
    environment {
        AWS_ACCESS_KEY_ID = 'your-access-key'
        AWS_SECRET_ACCESS_KEY = 'your-secret-key'
        BUCKET_NAME = 'your-bucket-name'
        FILE_NAME = 'data.csv'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/ml-data-labeling.git'
            }
        }
        stage('Run Python Script') {
            steps {
                script {
                    sh 'python3 data_labeling.py'
                }
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Cleaning up'
                // Add any cleanup steps if required
            }
        }
    }
}
