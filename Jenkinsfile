pipeline {
    agent any

    environment {
        APP_NAME = 'jungle-k8s-app'
        TAG      = 'latest'
    }

    stages {
        stage('1. Static Code Check') {
            steps {
                dir('ok') {
                    echo 'Checking Python application files...'
                    sh 'python3 -m py_compile app.py || python -m py_compile app.py'
                }
            }
        }

        stage('2. Build Container Image') {
            steps {
                dir('ok') {
                    echo 'Building Docker image...'
                    sh "docker build -t ${APP_NAME}:${TAG} ."
                }
            }
        }

        stage('3. Deploy to Kubernetes Cluster') {
            steps {
                dir('ok') {
                    echo 'Applying Kubernetes manifests...'
                    sh 'kubectl apply -f k8s-deployment.yaml'
                    sh "kubectl rollout restart deployment/${APP_NAME}"
                }
            }
        }

        stage('4. Verify Rollout Status') {
            steps {
                echo 'Waiting for pods to reach Running status...'
                sh "kubectl rollout status deployment/${APP_NAME} --timeout=60s"
            }
        }
    }
}