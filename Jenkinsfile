pipeline {
    agent any

    stages {
        stage('Deploy Jungle App') {
            steps {
                echo 'Pulling the latest code from GitHub and deploying...'
                
                sh '''
                    # 1. Stop and clear out the previous container if it exists
                    docker stop my-jungle-web-app || true
                    docker rm my-jungle-web-app || true
                    
                    # 2. Spin up a fresh Nginx container
                    docker run -d --name my-jungle-web-app -p 8083:80 nginx:alpine
                    
                    # 3. Wait 2 seconds and copy our HTML file straight from the GitHub download workspace
                    sleep 2
                    docker cp index.html my-jungle-web-app:/usr/share/nginx/html/index.html
                '''
            }
        }
    }
}