# Basics of Python for DevOps Engineers  

Python is a powerful scripting language used for **automation, cloud computing, and DevOps workflows**. This guide will help you set up Python and learn its basic data types.  

---  

## Step 1: Install Python  
 

### Linux (Ubuntu/Debian-based)  
1. Open the terminal and install Python:  
   ```sh  
   sudo apt update && sudo apt install python3 -y  
   ```  
2. Verify installation:  
   ```sh  
   python3 --version  
   ```  
   

---  

## Step 2: Learn Python Data Types  

Python has several built-in **data types** that are useful for DevOps automation.  

| Data Type  | Example |  
|------------|---------|  
| **String (`str`)**  | `"Hello, DevOps!"` |  
| **Integer (`int`)** | `100` |  
| **Float (`float`)** | `3.14` |  
| **Boolean (`bool`)** | `True` or `False` |  
| **List (`list`)** | `["AWS", "Docker"]` |  
| **Tuple (`tuple`)** | `("CI/CD", "Terraform")` |  
| **Dictionary (`dict`)** | `{ "Cloud": "AWS" }` |  

### Example Code: Checking Data Types  
Create a script `datatypes.py`:  
```python  
# Define different data types  
name = "DevOps Engineer"  # String  
experience = 2  # Integer  
rating = 4.5  # Float  
is_certified = True  # Boolean  
tools = ["Docker", "Kubernetes", "Ansible"]  # List  
config = ("Linux", "AWS", "Terraform")  # Tuple  
info = {"Name": "Karthikeyan", "Role": "DevOps"}  # Dictionary  

# Print types  
print(type(name), type(experience), type(rating))  
print(type(is_certified), type(tools), type(config), type(info))  
```  
Run the script:  
```sh  
python3 datatypes.py  
```  

---  

## Step 3: Writing a Simple Python Script  

Create `hello.py`:  
```python  
print("Hello, DevOps Engineers!")  
```  
Run the script:  
```sh  
python3 hello.py  
```  

---  

## Step 4: Get System Information  
Python can fetch system details, useful for DevOps tasks.  

Create `sys_info.py`:  
```python  
import platform  

print("OS:", platform.system())  
print("Version:", platform.version())  
print("Processor:", platform.processor())  
```  
Run:  
```sh  
python3 sys_info.py  
```  

--- 
