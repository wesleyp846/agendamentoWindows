python -m venv env  
.\env\Scripts\Activate.ps1

create .gitignore >> env/

git init | git add . | git commit -m "initial" 
git remote add <name> https://github.com/wesleyp846