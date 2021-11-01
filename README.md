# CointTrackerTakeHome

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- src folder - Code for the application's Lambda function.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

APIs Supported are:
1. create_user_address: Given a User Id, associates an address with the user. Sample invoke : `curl -d '{"userId": "2afc86cab8b31f55b3747d6aedb5e12c", "address": "bc1qsjf2j7fxhq5338z4zee3p0sr9uu8jf6anmkj4w"}' -H 'Content-Type: application/json' -X POST https://bgrasykzp8.execute-api.us-west-2.amazonaws.com/Prod/create_user_address `. Please use this same userId as my DB only has this in it.
2. get_user_details: Displays user details like name, email, physical address, etc. Sample invoke: `curl https://bgrasykzp8.execute-api.us-west-2.amazonaws.com/Prod/get_user_details?userId=2afc86cab8b31f55b3747d6aedb5e12c`
3. get_user_addresses: Given a user Id displays associated bitcoin addresses. Sample invoke: `curl https://bgrasykzp8.execute-api.us-west-2.amazonaws.com/Prod/get_user_addresses?userId=2afc86cab8b31f55b3747d6aedb5e12c`
4. get_address_details: Given an address displays balance, spent and received in USD. Sample invoke: `curl https://bgrasykzp8.execute-api.us-west-2.amazonaws.com/Prod/get_address_details?address=bc1qsjf2j7fxhq5338z4zee3p0sr9uu8jf6anmkj4w`
5. sync_addresses: Given an address, syncs the address balance, spent and received using blockchairs api. Invoke this after a new address is added. If you see "Internal Server error", please retry as sometime lambda times out waiting for blockchair. Sample invoke: `curl -d '{"address": "bc1qsjf2j7fxhq5338z4zee3p0sr9uu8jf6anmkj4w"}' -H 'Content-Type: application/json' -X POST https://bgrasykzp8.execute-api.us-west-2.amazonaws.com/Prod/sync_addresses`

This project does not follow the technologies suggested in the SYSTEM DESIGN, for a MVP I chose to to use AWS Serverless Infrastructure which stores and retrieves data from MYSQL DB.

To Create the DB, please check the DB folder which contains the SQL Scripts: https://github.com/Souratendu/project-name/blob/master/src/db/SQLQueries.sql.


Please follow the below instructions if it is need to setup this code base in another AWS account. Folloe the instructions to set up SAM CLI first.
The mysqlutility.py file does not have the MySQL configurations, for this code to work in another environment, those values need to be setup.

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
CointTrackerTakeHome$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
CointTrackerTakeHome$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
CointTrackerTakeHome$ sam local start-api
CointTrackerTakeHome$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
CointTrackerTakeHome$ sam logs -n HelloWorldFunction --stack-name CointTrackerTakeHome --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name CointTrackerTakeHome
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
