pipeline {
    agent any

    stages {
        stage('Install Testing Tools') {
            steps {
                echo 'Installing tidy validator inside the Jenkins environment...'
                // If Jenkins runs as root or standard user, this handles both cleanly
                sh 'apt-get update && apt-get install -y tidy || sudo apt-get update && sudo apt-get install -y tidy'
            }
        }

        stage('Test HTML Syntax') {
            steps {
                echo 'Scanning index.html for structural layout errors...'
                // -errors tells tidy to ONLY output crucial errors, ignoring minor alerts
                // -quiet hides the default welcome banners from messy logs
                sh 'tidy -errors -quiet index.html'
            }
        }

        stage('Deploy Jungle App') {
            steps {
                echo 'Test passed flawlessly! Initializing Nginx deployment...'
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