pipeline
{
    agent none
    stages
    {
        stage("Code Checkout")
        {
            agent
            {
                label 'Docker'
            }
            steps
            {
                git branch: 'main', url: 'https://github.com/devops-example-projects/flask-docker.git'
            }
        }
        stage("Code Build")
        {
            agent
            {
                label 'Docker'
            }
            steps
            {
                sh "docker build -t flask-docker-app ."
                sh "docker tag flask-docker-app adityadevops/flask-docker-app:${env.BUILD_ID}"
                //sh "docker tag flask-app adityadevops/flask-docker-app:${env.BUILD_TAG}"
                sh "docker tag flask-docker-app adityadevops/flask-docker-app:latest"
            }
        }
        stage("Push To Docker Hub")
        {
            agent
            {
                label 'Docker'
            }
            steps
            {
                withCredentials([string(credentialsId: 'DockerHubPassword', variable: 'Docker_Hub_Password')]) 
                {
                    sh 'docker login -u adityadevops -p ${Docker_Hub_Password}'
                }
                sh "docker push adityadevops/flask-docker-app:${env.BUILD_ID}"
                sh "docker push adityadevops/flask-docker-app:latest"
                sh "docker rmi flask-docker-app"
                sh "docker rmi adityadevops/flask-docker-app:${env.BUILD_ID}"
                sh "docker rmi adityadevops/flask-docker-app:latest"
            }
        }
        stage("Trigger Ansible Playbook")
        {
            agent
            {
                label 'Docker'
            }
            steps
            {
                sh "ansible-playbook -i hosts playbook.yaml"
            }
        }
    }
}
