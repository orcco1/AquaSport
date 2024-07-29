# AquaSport

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AquaSport.git
   cd AquaSport

2. **Create a virtual enviroment:**
    python -m venv env

3. **Activate your virtual enviroment:**
    windows: .\env\Scripts\activate
    linux/macOS: source env/bin/activate

4. **Install dependencies**
    pip install -r requirements.txt

5. **Run the app**
    python index.py

6. **Database credentials**
    if needed, create an issue specifiying why you need them.
    - put the email to send the file
    - choose me as a reviewer
    - once you have the file, download it and copy it to "your/carpets/AquaSport"
    - add to .gitignore

## Contribution guidelines

1. **Create your own fork of the repository**

2. **Create an issue for the contribution**
    - describe the changes
    - approach
    - motivation

3. **Create a branch rebased on master for every issue**

4. **Open a pull request for your commits**

5. **Only reviewers can merge**

6. **Never push any sensitive data**

## Tkinter usage
 Tkinter is included by default with Python installations on Windows. If you have Python installed, you already have Tkinter available. No separate installation is needed.
 If you're using linux, you'll have to install it
 - Arch based distros:  sudo pacman -S tk
 - Ubuntu based distros: sudo apt-get install python3-tk
