pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/kaaartik/Admin-Dashboard.git'
            }
        }
        stage('Install Python venv Package') {
            steps {
                sh 'sudo apt-get update && sudo apt-get install -y python3-venv'
            }
        }
        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv          # Create virtual environment
                    source venv/bin/activate           # Activate virtual environment
                    pip install Flask             # Install Flask inside the virtual environment
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'No tests defined'
            }
        }
        stage('Deploy') {
            steps {
                sh 'sudo systemctl restart app'  // Replace 'my-flask-app' with your Flask app service name if needed
            }
        }
    }
}
