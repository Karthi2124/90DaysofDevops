# 🚀 Day-22: Getting Started with Jenkins – CI/CD in Action!

This project is part of my **DevOps learning journey**, where I explore automation using Jenkins — one of the most popular CI/CD tools in the industry.

---

## Task 1: What is Jenkins?

Jenkins is an open-source automation server that helps developers **automate the building, testing, and deployment** of software. It's written in Java and plays a crucial role in the **DevOps lifecycle** by enabling Continuous Integration (CI) and Continuous Deployment (CD).

By integrating tools like Git, Docker, and Maven through plugins, Jenkins allows you to:
- Run tests every time code is pushed
- Automatically deploy builds to staging/production
- Monitor the health of your projects with logs and feedback

Jenkins empowers teams to deliver faster, more reliably, and with less manual effort.

---

## Task 2: Jenkins Freestyle Job

I created a **Freestyle Job** in Jenkins that performs the following steps:

- Prints “Hello World”
- Displays the current date and time
- Clones my GitHub repository
- Lists the contents of the cloned directory
- Scheduled to run **every hour** automatically using a cron trigger

🔗 **GitHub Repository Cloned in Job:**  
[https://github.com/Karthi2124/Jenkins](https://github.com/Karthi2124/Jenkins)

---

## 🔧 Jenkins Shell Script Used

Below is the shell script configured in the **"Execute Shell"** section of the Jenkins job:

```bash
echo "Hello World"
echo "Current Date and Time:"
date

echo "Cloning Repository..."
git clone https://github.com/Karthi2124/Jenkins.git

echo "Listing Repo Contents:"
cd Jenkins
ls -la
