
1. Clone this repository:
   git clone https://github.com/subreto-roy/repliq.git
   cd asset_tracking_project
  



2. Install project dependencies:
   pip install -r requirements.txt




3. Apply database migrations:
   python manage.py migrate


4. Create a superuser account:


   python manage.py createsuperuser


## Usage

1. Start the development server:


   python manage.py runserver
 

2. Access the admin interface at `http://127.0.0.1:8000` and log in with your superuser account to manage companies, employees, devices, and logs.



