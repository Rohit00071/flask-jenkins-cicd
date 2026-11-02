pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                echo 'Installing Flask dependencies...'

                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Flask application...'

                sh '''
                    . .venv/bin/activate
                    python -m py_compile app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application...'

                sh '''
                    pkill -f "python.*app.py" || true

                    nohup .venv/bin/python app.py > flask.log 2>&1 &

                    sleep 3

                    curl -f http://127.0.0.1:5000/api/health
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