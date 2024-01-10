# yeticontroller for Cyberdyne

This repo holds the code and pipelines for an Example Flask App that is deployed using AWS SAM.

Location of Dev URL that is deployed: [Dev Link](https://p6dambi6yb.execute-api.us-east-2.amazonaws.com/Prod/)
Location of Production Link: [Prod Link]( https://dakb85f168.execute-api.us-east-2.amazonaws.com/Prod/)

**Note**:  You can find the shortened commit SHA for DEV and the Production release tag in use on these pages.


**Design Considerations.**

 - **Why Flask?** - Flask is a great and easy WSGI server for python.
 - **Why AWS SAM?** - It deploys serve-less models easily using a defined template.  Its rather easy and does not rely on outside frameworks like serverless.io. Serverless.io is great, but I wanted to keep things simple for the demo.
 - **Why Serverless?** - Its basically free for the demo and can demo the piplines.  Again for time sake, Serverless was used rather than terraform creating / destroying resources.

## How to use the Repository
The pipelines are configured to run every time there is a commit to the development branch.  We can switch this up and have versioned development releases and production releases.  But for the sake of this project, we have are deploying every time there is a commit to the development branch.

### Deploying
----
**Development**:  All you have to do is merge your feature branch into the development branch, this will start a development pipeline that will check code coverage, run tests, then finally deploy with AWS SAM.

 **Production**: To kick off a production release, you have two options.
 

 - **Manual For a specific tag**  This is helpful when you want to revert or deploy a spefic commit on master.
 -  **Automation On vX.X.X releases**:  When you create a release, the pipeline runs when it detects a v release.



### AWS SAM
----
AWS SAM is a framework provided by AWS to deploy serverless functions. It allows you to test locally and define some IAC for the function.

The two main files are.

**template.yaml**
This is where the cloudformation resides for the function.  You can customize this to suit your needs.

**samconfig.toml**
This is where the AWS SAM configuration lives.  This is what tells SAM what to do.  You can define different enviornments.  We have DEV and PROD defined.

**Helpful documentation.**
Deploying a Server-less Flask app using AWS SAM.
[Link to AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)