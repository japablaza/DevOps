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

### Installing Jenkins
- Debian distribution
    Install Java (OpenJDK)
      `sudo apt-get install openjdk-7-jre -y`
      `sudo apt-get install openjdk-7-jdk -y`
      `java -version`
    Add the Security Key from Jenkins repository
      `wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -`
      `sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'`
    Add Jenkins apt-get repository
    Install Jenkins
