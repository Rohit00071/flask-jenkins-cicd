pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning Flask backend repository...'

                git branch: 'main',
                    url: 'https://github.com/Rohit00071/flask-jenkins-cicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'

                sh '''
                    python3 -m pip install --user -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Flask application...'

                sh '''
                    python3 -m py_compile app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application with PM2...'

                sh '''
                    pm2 delete flask-app || true
                    pm2 start app.py --name flask-app --interpreter python3
                    pm2 save
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask deployment completed successfully!'
        }

        failure {
            echo 'Flask deployment failed!'
        }
    }
}