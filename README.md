# 🔓 Hacking Project  

This was one of my early hacking experiments in college, where I explored web security vulnerabilities and image processing techniques. The project consists of:  

🚀 **Brute-forcing a login page** using a **binary search algorithm** to exploit status responses and uncover the correct password.  
🖼️ **Bypassing a CAPTCHA system** composed of smaller images representing numbers (0-9) by processing them with **Python's PIL (Pillow) library**.  
🌐 **Interacting with a website** by sending **GET and POST requests** to automate the attack.  

⚠️ **Disclaimer:** This project was purely for educational purposes to understand security flaws and ethical hacking techniques. Always follow ethical guidelines and legal boundaries when working on cybersecurity-related projects.  

## 🛠️ Technologies Used  
- **Python** 🐍  
- **PIL (Pillow)** for image processing  
- **Requests** library for handling HTTP requests  
- **Binary Search Algorithm** for efficient password cracking  

## 📸 CAPTCHA Breakdown  
The CAPTCHA system was composed of smaller images, each representing a number from **zero to nine**. The goal was to programmatically **analyze and reconstruct the CAPTCHA** to bypass it.  

## 🚀 How It Works  
1. **Login Page Exploit:**  
   - The website responds differently based on password correctness.  
   - Using **binary search**, we systematically narrow down the correct password by analyzing response statuses.  

2. **CAPTCHA Bypass:**  
   - The CAPTCHA image is formed by stitching together **smaller digit images**.  
   - By segmenting the image and identifying each number, we can reconstruct the CAPTCHA solution.  

## 🎯 Lessons Learned  
- How **web authentication** can be exploited through status-based password guessing.  
- Techniques for **image processing** and pattern recognition.  
- The importance of **CAPTCHA security** and how weak implementations can be cracked.  
