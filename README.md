\# Flask Backend



This project is a Flask backend application deployed on Amazon EC2.



\## Technology



\- Python

\- Flask

\- Gunicorn



\## Port



The application runs on:



http://EC2\_PUBLIC\_IP:5000



\## API Endpoints



\### Home



GET /



\### Health Check



GET /api/health



\## Deployment



The application is deployed using Jenkins CI/CD.



Jenkins automatically:



1\. Pulls the latest source code.

2\. Installs Python dependencies.

3\. Runs tests.

4\. Restarts the Flask application.

