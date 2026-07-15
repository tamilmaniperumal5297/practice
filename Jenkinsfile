pipeline {
    agent any

    stages {
        stage('Install Testing Tools') {
            steps {
                echo 'Installing tidy validator...'
                // Just use apt-get directly. No need for sudo.
                sh 'apt-get update && apt-get install -y tidy'
            }
        }

        stage('Test HTML Syntax') {
            steps {
                echo 'Testing index.html...'
                sh 'tidy -errors -quiet index.html'
            }
        }

        stage('Deploy Jungle App') {
            steps {
                sh '''
                    docker stop my-jungle-web-app || true
                    docker rm my-jungle-web-app || true
                    docker run -d --name my-jungle-web-app -p 8083:80 nginx:alpine
                    sleep 2
                    docker cp index.html my-jungle-web-app:/usr/share/nginx/html/index.html
                '''
            }
        }
    }
}