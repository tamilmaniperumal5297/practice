pipeline {
    agent any

    environment {
        APP_NAME = 'jungle-k8s-app'
        TAG      = 'latest'
    }

    stages {
        stage('1. Static Code Check') {
            steps {
                echo 'Checking Python application files...'
                sh 'echo "Skipping local python check, proceeding to Docker build..."'
            }
        }

        stage('2. Build Container Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${APP_NAME}:${TAG} ."
            }
        }

        stage('3. Deploy to Kubernetes Cluster') {
            steps {
                echo 'Applying Kubernetes manifests...'
                // Updated to match k8s_deployment.yaml with underscore
                sh 'kubectl apply -f k8s_deployment.yaml'
                sh "kubectl rollout restart deployment/${APP_NAME}"
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