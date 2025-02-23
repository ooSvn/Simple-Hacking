# 🔓 Hacking Project  

This was one of my early hacking experiments in college, where I explored web security vulnerabilities and image processing techniques. The project consists of:  

🚀 **Brute-forcing a login page** using a **binary search algorithm** to exploit status responses and uncover the correct password.  
🖼️ **Bypassing a CAPTCHA system** composed of smaller images representing numbers (0-9) by processing them with **Python's PIL (Pillow) library**.  
🌐 **Interacting with a website** by sending **GET and POST requests** to automate the attack.  

⚠️ **Disclaimer:** This project was purely for educational purposes to understand security flaws and ethical hacking techniques. Always follow ethical guidelines and legal boundaries when working on cybersecurity-related projects.  

## 🛠️ Technologies Used  
- **Python** 🐍 – Core programming language.  
- **Requests** – For handling HTTP requests (GET, POST) to interact with the login page and CAPTCHA system.  
- **PIL (Pillow)** – For image processing and converting CAPTCHA images to grayscale.  
- **io.BytesIO** – For handling image byte streams efficiently.  
- **JSON** – For parsing server responses during password cracking.  
- **Binary Search Algorithm** – For efficiently determining the correct password based on server response statuses.  

## 📸 CAPTCHA Breakdown  
The CAPTCHA system was composed of smaller images, each representing a number from **zero to nine**. The goal was to programmatically **analyze and reconstruct the CAPTCHA** to bypass it.  

## 🚀 How It Works  
1. **Login Page Exploit:**  
   - The website responds differently based on password correctness.  
   - Using **binary search**, we systematically narrow down the correct password by analyzing response statuses.  

2. **CAPTCHA Bypass:**  
   - The CAPTCHA image is formed by stitching together **smaller digit images**.  
   - By segmenting the image and identifying each number, we can reconstruct the CAPTCHA solution.  
