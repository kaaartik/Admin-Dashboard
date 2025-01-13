# 🚀 Admin Dashboard Deployment with Terraform

### 📝 **Project Description**  
This project demonstrates the deployment of an Admin Dashboard application built with **HTML**, **CSS**, **Python**, **Flask**, and **SQLite**, using **Terraform** for infrastructure-as-code. It automates the provisioning of an AWS EC2 instance, configures security groups, installs dependencies, and launches the application. The entire process achieves deployment in under 5 minutes, ensuring a scalable and reproducible setup.  

---

### 🛠 **Technologies Used**

- **Frontend**: HTML, CSS  
- **Backend**: Python, Flask, SQLite  
- **Infrastructure-as-Code**: Terraform  
- **Cloud**: AWS EC2  

---

### 📂 **Terraform Configuration**

The project includes a `main.tf` file with the following features:  
- **EC2 Instance**:  
  - Created in the `us-east-1` region using a specified Ubuntu AMI.  
  - Configured with a t2.micro instance type.  
- **Security Groups**:  
  - Allows inbound traffic on ports `5000` (Flask app), `22` (SSH), and `80` (HTTP).  
- **Automated Setup**:  
  - Installs Python, pip, Flask, Gunicorn, Git, and SQLite.  
  - Clones the Admin Dashboard repository.  
  - Sets up a Python virtual environment and installs dependencies.  
  - Launches the application using Gunicorn.  

---

### 📋 **Deployment Steps**

Follow these steps to deploy the project:

1. **Install Terraform**  
   Install Terraform on an existing EC2 instance or your local machine.  

2. **Create `main.tf`**  
   Copy the provided `main.tf` file to your working directory.  

3. **Initialize Terraform**  
   Run the following command to initialize the Terraform workspace:  
   ```bash
   terraform init
4. **Plan Terraform**  
   Run the following command to generate and review the execution:  
   ```bash
   terraform plan
5. **Apply Terraform**  
   Run the following command to deploy the infrastructure and run the setup:  
   ```bash
   terraform apply
6. **Verify Deployment**  
   Retrieve the public IP of the newly created EC2 instance from the Terraform output.
   SSH into the instance to confirm the application is running:
   ```bash
   ssh -i your-key.pem ubuntu@<public-ip>
7. **Access the Application**  
   Open a browser and navigate to **http://<public-ip>:5000** to view the Admin Dashboard.
