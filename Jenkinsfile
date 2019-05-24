pipeline{
    agent any

    stages{
        stage("部署master分支"){
            when{
                branch 'master'
            }
            steps{
                echo "master 部署成功"
            }
    }

        stage("部署dev分支"){
            when{
                branch 'dev'
            }
            steps{
                echo "dev 部署成功"
            }
    }

        stage("部署feature分支"){
            when{
                branch 'feature'
            }
            steps{
                echo "feature 部署成功"
            }
        }
    }

}