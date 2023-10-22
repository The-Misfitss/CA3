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
    parameter{
        string(name:'VERSION',defaultValue:'1.0', description:'...')
        choice(name:'Blah', choices = ['1', '2', '3'],description='...')
        booleanParam(name:'Deploy', defaultValue=true, description='...')
    }
    environment{
        VERSION = '1.3'
        SERVER_CREDENTIALS = credentials('jenkins-tut')
        //Here we called the credentials function which takes the Reference ID as a parameter to get the credentials and store them in SERVER_CREDENTIALS.
    }
    stages{
        stage("build"){
            when{
                expression{
                    BRANCH_NAME == 'master'  //Run only if the current branch is master and any changes have been made in the code
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
                    BRANCH_NAME == 'master' //Only if the current branch is master let's say
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
                //We can use the following function named as withCredentials that takes as a parameter an object [] <-- (This is an object syntax in groovy). This object will be usernamePassword() -> Now this is a function that lets me get the username and the password individually
                withCredentials([
                    usernamePassword(credentialsId:'server-credentials',usernameVariable:'USER',passwordVariable:'PASSWORD') //Using the usernamePassword function because the type of credentials we created on jenkins was of this type.. 
                    //After that we are simply storing the username ins the variable USER and the password in the varibale PASSWORD
                ]){
                    //Now here in this block I can use USER and PASSWORD

                    //echo "Server Credentials -> ${SERVER_CREDENTIALS}"
                    echo "${USER} ${PASSWORD}"
                }

            }
        }

    }
    //After all the stages are done we can define the post stages. Which will be executed after all of the stages have been executed.
    post{
        always{
            echo "This will be executed alway, like sending emails etc"
            //This will be executed alway, like sending emails etc
        }
        success{
            echo "Will execute in case of success"

            //Will execute in case of success
        }
        failure{
            echo "Will execute in case of failure"

            //Will execute in case of failure
        }
        unstable{
            echo "Will execute in case the build was unstable"

            //Will execute in case the build was unstable
        }
    }
}


/*
Accessing the local variable
    localhost:8080/env-vars.html
We can define our own variables as shown in the above code
*/

/*
Using credentials in Jenkinsfile
To use the credentials inside the jenkins we use the 'Credentials Binding'plugin
    1. Setup the credentials in the jenkins
    2. Access them using the credentials function(As a parameter it takes the ID reference of the credentials) and assign them to some env variable in the environment block
*/
