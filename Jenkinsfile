/*
In this File following Jenkinsfile concepts have been discussed.

1. Jenkinsfile structure
2. Post stages options
3. Conditions(When)
4. Environment Variables
5. Credentials
*/

pipeline{
    agent any
    environment{
        VERSION = '1.3'
        SERVER_CREDENTIALS = credentials('server-credentials')
        //Here we called the credentials function which takes the Reference ID as a parameter to get the credentials and store them in SERVER_CREDENTIALS.
    }
    stages{
        stage("build"){
            when{
                expression{
                    env.BRANCH_NAME == 'master' && env.CODE_CHANGE == true //Run only if the current branch is master and any changes have been made in the code
                }
            }
            steps{
                echo "building the application..."
                //Using the env variables
                echo "building the version: ${VERSION}"
            }
        }
        stage("test"){
            //We can define the conditions for our stage. e.g: Here if we want to run the test for only the master branch and exclude all other branches. So we used the 'When' keyword for this.
            when{
                expression{
                    // BRANCH_NAME is always provided in the environment variable provided by jenkins
                    env.BRANCH_NAME === 'master' //Only if the current branch is master let's say
                }
            }
            steps{
                echo "Testing the application..."
            }
        }

        stage("deploy"){
            steps{
                echo "Deploying the application..."
                echo "deploying with ${SERVER_CREDENTIALS}"
                sh "${SERVER_CREDENTIALS}"
            }
        }

    }
    //After all the stages are done we can define the post stages. Which will be executed after all of the stages have been executed.
    post{
        always{
            //This will be executed alway, like sending emails etc
        }
        success{
            //Will execute in case of success
        }
        failure{
            //Will execute in case of failure
        }
        unstable{
            //Will execute in case the build was unstable
        }
    }
}
