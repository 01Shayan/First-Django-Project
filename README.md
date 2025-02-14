# First Django Project
My first django project.

## How to run
1. Install `python3`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/01Shayan/First-Django-Project.git`.
3. Make environment ready using commands below:
  ```bash
  git clone https://github.com/01Shayan/First-Django-Project.git && cd First-Django-Project
  python3 -m venv venv  # Create virtualenv named build
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py migrate  # Create database tables
  ```

4. Run `First-Django-Project` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your Django-Todo-List version.
6. If you need a Tailwind installation guide, you can visit this site -> [django-tailwind-installation](https://django-tailwind.readthedocs.io/en/latest/installation.html).

## Run On Windows
If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python3`, `pip`, `virtualenv` 
2. Clone the project using:  `git clone https://github.com/01Shayan/First-Django-Project.git`.
3. Make Environment Ready Like This:
  ```bash
  cd First-Django-Project
  virtualenv -p "PATH\TO\Python.exe" build # Give Full Path To python.exe
  build\Scripts\activate # Activate The Virutal Environment
  pip install -r requirements.txt
  python manage.py migrate # Create Database Tables
  ```
4. Run `First-Django-Project` using `python manage.py runserver`
<<<<<<< HEAD
5. Go to [http://localhost:8000](http://localhost:8000) to see your Django-Todo-List version.
=======
5. Go to [http://localhost:8000](http://localhost:8000) to see your Django-Todo-List version.