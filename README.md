# DevOps
All about DevOps


## Jenkins
Link from good tutorial
`https://www.youtube.com/watch?v=WWcijE7ifcA&list=PLzvRQMJ9HDiSaisKr7OnM4Fl7JXCDDcmt`


## Videos
### Introduction
- Continuous integration (CI)
    Test applications with every change
    Detect failures as soon as possible
- Continuous delivery (CD)
    Automate deployments
    Limit risk of human errors
    Push to production server
- Written in Java

- Rednode / DigitalOcean

### Installing Jenkins / Getting source code from Git
- Debian distribution
    Install Java (OpenJDK)
      `sudo apt-get install openjdk-7-jre -y`
      `sudo apt-get install openjdk-7-jdk -y`
      `java -version`
    Add the Security Key from Jenkins repository
      `wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -`
      `sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'`
      `sudo apt-get update`
      `sudo apt-get install jenkins -y`
      `localhost:8080`
    Add Jenkins apt-get repository
      Running on the Jenkins server
        `sudo apt-get install git -y`
      localhost:8080
        `Manage Jenkins`
          `Manage Plugins`
            `Available`
              Search for: `Git plugin`
                Download now and install after restart

    Configure Jenkins with Git
      Create new jobs
        Freestyle project
          Source Code Management
            Git -->  `<git_URL>/<user>/<repository>`
                --> Branch
                --> Other parameters leave by default and `Save`
      Build Now
        Check logs and see the progress

### Integrate with BitBucket: Build after each commit
- Jenkins in DigitalOcean (You need a public IP for Jenkins)
  Manage Plugins Search for `bitbucket plugin`
    Download now and install after restart
  Create new jobs
    Freestyle project
      Source Code Management
        Git
          In bitbucket --> `Clone` --> `Copy HTTPS URL`
          Branches to build: `*/master`
        Build Triggers
          Build when a change is pushed to BitBucket (You need a test repository in BitBucket)
          Build when a change is pushed to BitBucket     
          Save
- Bitbucket
    Settings
      webhooks
        URL: `<jenkins_URL>:PORT/bitbucket-hook/`

- Test integration
  Edit local file
    `SourceTree` --> commit
  In bitbucket account
    Commits and verify the push is there
  In Jenkins
    Check the build status

### Running PHPUnit test after each commit
- Show the code
    code
    test_code
- Install PHPUnit & JInit Plugins
  SSH to Jenkins server
    `sudo apt-get install phpunit -y`
  Open Jenkins UI
    Manage Jenkins
      Manage Plugins
        JUnite Plugin
    In jobs list --> Click on job name
      Configure
        Build
          Add build step
            Execute shell
              `phpunit --log-junit results/phpunit/phpunit.xml -c tests/phpunit.xml`
        Add post-build action
          Publish JUnit test result report
            Test report XMLs: `results/phpunit/phpunit.xml`
            Health report amplification factor: 1,0
      Save
  Build Now

### Integrate Jenkins with BitBucket build Status API
- Install BitBucket build Status Notifier Plugin
- Create OAuth keys on BitBucket
  BitBucket UI
    BitBucket settings
      Access Management
        OAuth
          Create new consumer
            URL: Jenkins IP or URL
            Permissions
              repository --> `rw`
          `Key` & `Secret`
- Configure Jenkins
    manage Jenkins
      Available
        bitbucket build status notifier plugin
        bitbucket OAuth Plugin
    Jobs
      Configure
        Add new post-build action
          bitbucket notify build status
            Notify build start
            Notify build finish
              Advance
                Credentials
                  Add --> `User/Passwd`//\\`Key/Secret`


- test & verify
