pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'calculator_using_python'
        GITHUB_REPO_URL = 'https://github.com/kalyaniverma/SPE.git'
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the GitHub repository
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        
        stage('Run Main Application') {
            steps {
                script {
                    sh "echo '${choice}\n${number}\n${exp}'|python3 calculator_main.py"
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh 'python3 calculator_test.py'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }
        
        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        sh 'docker tag calculator_using_python kalyaniv2001/calculator_using_python:latest'
                        sh 'docker push kalyaniv2001/calculator_using_python'
                    }
                }
            }
        }
        
        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                    )
                }
            }
        }
    }
}

