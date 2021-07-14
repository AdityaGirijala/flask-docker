pipeline
{
    agent any
    stages
    {
        stage("Code Checkout")
        {
            steps
            {
                git url:'https://github.com/devops-example-projects/flask-docker.git',branch: 'main'
            }
        }
        stage("Code Build")
        {
            steps
            {
                script
                {
                    sh "docker build -t flask-docker ."
                }
            }
        }
        stage("Push to DockerHub")
        {
            steps
            {
                script
                {
                    def buildNumber = BUILD_NUMBER
                    sh "docker tag flask-docker adityadevops/flask-docker:${buildNumber}"
                    sh "docker tag flask-docker adityadevops/flask-docker:latest"
                    withCredentials([string(credentialsId: 'DockerHubPass', variable: 'DockerHubPassword')])
                    {
                        sh "docker login -u adityadevops -p ${DockerHubPassword}"
                    }
                    sh "docker push adityadevops/flask-docker:${buildNumber}"
                    sh "docker push adityadevops/flask-docker:latest"
                }
            }
        }
        stage("Deploy on Kubernetes Cluster")
        {
            steps
            {
                sshagent(['k8s'])
                {
                    sh "scp -o StrictHostKeyChecking=no kubernetes.yaml ec2-user@172.31.29.187:/home/ec2-user"
                    script
                    {
                        try
                        {
                             sh "ssh ec2-user@172.31.29.187 kubectl apply -f kubernetes.yaml"
                        }
                        catch(error)
                        {
                            sh "ssh ec2-user@172.31.29.187 kubectl create -f kubernetes.yaml"
                        }
                    }
                }
            }
        }
    }
}