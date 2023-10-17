pipeline{
    agent any //Here we can specify the agent name, as we know jenkins is a master slave architecture, so we can specify the agent name here, if we do not specify any agent name then it will run on master node.
        stages{
            stage('codeget'){
                steps{
                    echo"codeget stage"
                }
            }
            stage('build'){
                steps{
                    echo"build stage"
                }
            }
            stage('deploy'){
                steps{
                    echo"deploy stage"
                }
            }
        }
}
