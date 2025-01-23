# Jenkins Installation Guide

Follow the steps below to install and configure Jenkins on your system.

## Step 1: Download and Add Jenkins Key
```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
```

## Step 2: Update Packages and Install Dependencies
```bash
sudo apt-get update
sudo apt-get install fontconfig openjdk-11-jre
```

## Step 3: Install Jenkins
```bash
sudo apt install jenkins
```

## Step 4: Start Jenkins Service
```bash
sudo systemctl start jenkins.service
sudo systemctl status jenkins
```

## Step 5: Configure the Firewall
```bash
sudo ufw allow 8080
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
```

## Step 6: Retrieve Initial Jenkins Password
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

## Notes
- Ensure you have administrative privileges to execute the commands above.
- After retrieving the initial admin password, open a web browser and navigate to `http://<your-server-ip>:8080` to complete the Jenkins setup.
- For additional configuration, refer to the [official Jenkins documentation](https://www.jenkins.io/doc/).
