# Surgery Management API

A reference implementation of the REST API described by the [swagger.yaml](swagger.yaml) file provided is not yet available.
In a nutshell, this API will support the creation of a surgery management web app where receptionists, doctors and admins may do
the tasks outlined below:

### User Stories:
* As a receptionist
    * I should be able to add patients to the system
    * I should be able to create an appointment for a patient with an available doctor
    * I should be able to see  a list of available doctors for a given time period
    * I should be able to see a list of all patients
    * I should be able to select a patient and see their appointments or surgeries
* As a doctor
    * I should be able see a list of all my surgeries
    * I should be able to create a surgery for a patient
    * I should be able to see a list of available rooms for surgery for a given time period
    * I should be able see all available doctors for a surgery for a particular time period
* As an admin 
    * I should be able to check the schedule of any doctor or room as well as perform all the functions of a doctor or receptionist in the system

Your implementation may be in [Python](https://www.python.org), [Java](https://www.java.com/en/) or JavaScript (using [nodejs](https://nodejs.org/en/)), and you may use a web framework of your choosing.

In addition to satisfying the API specification, your implementation should adhere to the following conditions:
* You should make use of a relational database management system (PostgreSQL, MySQL or MariaDB).
* Make your implementation scalable - i.e., multiple users should be able to use it without suffering performance penalties
* All endpoints should be protected by bearer auth using a JSON web token except the following:
    * POST /login
* You should include instructions on how to set up your implementation for testing in a file called INSTRUCTIONS.md, including provisions for one admin user with the following credentials:
    * email: admin@speurgroup.com
    * password: admin

You may need to make some other assumptions (e.g. how to respond to error conditions) in order to complete the implementation. As long as they do not conflict with one of the requirements that have been clearly stated, feel free to make and state your assumptions in your submission.


```bash
{
    code: number,
    message: string,
    data: object | array
}
```
## Instructions

Fork this repository and write code to satisfy the implementation. When you are satisfied that your code works 
(or when the time is up), submit a merge request back to this repository. You are allowed to make use of any programming
resource (online or otherwise) but ensure that the code you submit is yours.

Make small commits with clear commit messages describing each change made to the code.

Be sure to submit a merge request by the due date even if you are not finished.

## Technologies

In order to implement this REST API effectively, you will need to be familiar with the following:
* [Git](https://git-scm.com/docs)
* [JSON Web Token](https://jwt.io/)
* [OpenAPI 3.0](https://swagger.io/specification/)
* [Markdown](https://spec.commonmark.org/0.29/)

## Bonus points

The following are for bonus points only and are not required:

* Include a working `Dockerfile` and/or `docker-compose.yaml` for your project (see [Docker](https://www.docker.com/))
* Include a working `.gitlab-ci.yaml` file for your project (see [GitLab CI/CD](https://docs.gitlab.com/ce/ci/))
* Include a `Bonus.md` file explaining how you would implement a "forgot password" feature, allowing a user to change
 their password
 * Actually implement the forgot password feature


## Final Remarks

Don't waste too much time reading documentation. Read just enough to get started and then attempt what you were reading.
You might find it useful to spend more time on forums like [stackoverflow](https://stackoverflow.com/) and 
[reddit](https://www.reddit.com/) and include the sites in your search queries.

If you find any issues with the assessment while attempting your implementation, be sure to bring them to my attention 
so that I may address them.

Good skill!