### Day-22: Getting Started with Jenkins

#### ✅ Task 1: What is Jenkins?

Jenkins is an open-source automation tool used in the DevOps lifecycle to build, test, and deploy code continuously. It helps automate repetitive tasks, reducing manual errors and speeding up the delivery process. Jenkins integrates with tools like Git, Docker, and Maven using plugins, enabling seamless Continuous Integration and Continuous Deployment (CI/CD).

#### ✅ Task 2: Jenkins Freestyle Job

- Printed “Hello World”
- Printed current date & time
- Cloned my GitHub repo: [https://github.com/Karthi2124/Jenkins](https://github.com/Karthi2124/Jenkins)
- Listed the contents
- Scheduled to run every hour

🔧 Jenkins Shell Script:

```bash
echo "Hello World"
echo "Current Date and Time:"
date

echo "Cloning Repository..."
git clone https://github.com/Karthi2124/Jenkins.git

echo "Listing Repo Contents:"
cd Jenkins
ls -la



---

#### 🔧 **2. Try These Next Tasks (Advanced Jenkins Ideas)**

| Task | Description |
|------|-------------|
| **Create a Jenkinsfile (Declarative Pipeline)** | Move your shell commands into a `Jenkinsfile` and create a **Pipeline project** instead of freestyle. |
| **Email Notification** | Add email notification when a build fails or succeeds using the Email plugin. |
| **Integrate Docker Build** | Write a Jenkins job that builds a Docker image from your repo’s Dockerfile. |
| **Trigger Build on Git Push** | Use **GitHub Webhook** so Jenkins auto-builds when you push code to GitHub. |
| **Use Parameters** | Add parameters to the job (e.g., choose which repo to clone). |

---

### Want Help with Any of These?

I can help you:
- Convert this to a **Jenkinsfile**
- Add **email notifications**
- Create a **Docker build pipeline**
- Set up **GitHub webhooks**

Just tell me what you'd like to do next 💡
