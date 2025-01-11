provider "aws" {
  region = "us-east-1" # Choose your AWS region
}

resource "aws_instance" "flask_app" {
  ami           = "ami-0e2c8caa4b6378d8c" # Replace with your Ubuntu AMI ID
  instance_type = "t2.micro"
  key_name      = "terraform-admin" # Replace with your EC2 key pair
  security_groups = [aws_security_group.flask_sg.name]

  user_data = <<-EOF
    #!/bin/bash
    sudo apt update -y
    sudo apt install -y python3
    sudo apt install -y python3-pip
    sudo apt install -y python3-venv
    sudo apt install -y git
    sudo apt install -y sqlite3

    # Clone your repository
    git clone https://github.com/kaaartik/Admin-Dashboard.git /home/ubuntu/app
    # Set up the virtual environment
    cd /home/ubuntu/app
    python3 -m venv venv
    source venv/bin/activate
    pip install flask gunicorn

    # Start the Flask app
    nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app &
  EOF

  tags = {
    Name = "FlaskAppInstance"
  }
}

resource "aws_security_group" "flask_sg" {
  name_prefix = "flask_app_sg"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  # Ingress rule for SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 # Ingress rule for HTTP
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "public_ip" {
  value = aws_instance.flask_app.public_ip
}
