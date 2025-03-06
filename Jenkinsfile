pipeline{
    agent any
    stages{
        stage('Build Image'){
            steps{
                sh 'docker build -t diegopgm23/kubedash .'
            }
        }
        stage('Push Image'){
            steps{
                sh 'docker push diegopgm23/kubedash'
            }
        }
    }
}