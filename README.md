# 🛡️ CloudSentinel: Automated Security & Uptime Monitoring

CloudSentinel is a production-grade serverless solution designed to host a secure web asset, protect it from global threats, and provide 24/7 automated health monitoring. This project demonstrates mastery of the **AWS Well-Architected Framework** pillars, specifically Security and Operational Excellence.



---

## 🏗️ Architecture Overview

* **Storage**: Private Amazon S3 Bucket (Hidden Origin).
* **Delivery**: Amazon CloudFront with Origin Access Control (OAC).
* **Security**: AWS WAF (Web Application Firewall) protecting against SQLi and XSS.
* **Monitoring**: AWS Lambda (Python 3.13) Heartbeat script.
* **Alerting**: Amazon SNS (Simple Notification Service) for real-time failure alerts.

---

## 📂 Repository Structure

```text
AWS-CloudSentinel/
├── frontend/
│   └── index.html         # The pulse-animation status page
├── backend/
│   └── lambda_function.py # The Python uptime monitor logic
└── README.md              # Documentation & Step-by-Step Guide
```
---- 
## 🚀 Step-by-Step Implementation Guide

Phase 1: Secure Origin Storage (S3)

1/ Create Bucket: Create a private S3 bucket (e.g., cloudsentinel-storage-01).
2/ Settings: Keep "Block all public access" turned ON.
3/ Upload Content: Upload the index.html file from the /frontend folder of this repo.
4/ Purpose: This ensures the data is not accessible via the public internet, only through our secure CDN.

Phase 2: Secure Global Delivery (CloudFront & OAC)
1/ Create Distribution: Set the Origin Domain to your S3 bucket.
2/ Origin Access: Select Origin access control settings (OAC). Create a new control setting and assign it.
3/ Default Root Object: Type index.html.
4/ Security Handshake: After the distribution is created, copy the generated S3 Bucket Policy.
5/ Apply Policy: Navigate to your S3 Bucket -> Permissions -> Bucket Policy, and paste it there. This "whitelists" CloudFront to talk to your private S3.

Phase 3: Edge Security Shield (AWS WAF)
1/ Create Web ACL: Navigate to AWS WAF and create a new Web ACL.
2/ Resource Association: Select "CloudFront distributions" and choose your Sentinel distribution.
3/ Add Managed Rules: Add the following rules to filter malicious traffic:
   * Core Rule Set (CRS): Protects against OWASP Top 10 (SQLi, XSS).
   * Amazon IP Reputation List: Blocks requests from known malicious bots/IPs.

Phase 4: Automated Heartbeat (Lambda & SNS)
1/ Create Alert Topic: Create an SNS Topic (Standard) named Sentinel-Alerts.
2/ Subscribe: Add your email as a subscriber to the topic and confirm the subscription in your inbox.
3/ Create Monitor: Create a Lambda Function (Python 3.13).
4/ Code: Paste the code from /backend/lambda_function.py.
5/ IAM Permissions: Add sns:Publish permissions to the Lambda's Execution Role.
6/ Environment Variables: Add SITE_URL (Your CloudFront URL) and SNS_TOPIC_ARN to the Lambda configuration.
7/ Schedule: Add an EventBridge (CloudWatch Events) trigger with a schedule of rate(1 minute).

---
## 🛠️ Technology Stack

* Compute: AWS Lambda (Serverless Python)
* Security: AWS WAF, IAM, CloudFront OAC
* Storage: Amazon S3
* Content Delivery: Amazon CloudFront
* Notifications: Amazon SNS
* Automation: Amazon EventBridge
---
## 🧹 Cleanup (Cost Control)

To ensure the project remains free, delete resources in this order:
1/ WAF: Delete the Web ACL.
2/ CloudFront: Disable, then Delete.
3/ S3: Empty the bucket, then Delete.
4/ Lambda/SNS: Delete the function and the SNS topic.
---
## 👨‍💻 Author
Omer Taha Ahmed 
