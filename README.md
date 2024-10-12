
# Gas Utility Management System

A Django-based web application designed to streamline gas utility services by allowing customers to submit service requests, track their status, and manage their account information. This application also provides customer support representatives with the necessary tools to manage and respond to customer inquiries effectively.

## Table of Contents
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Key Features
- **Service Requests:** Customers can submit service requests online, specifying the type of service needed, providing additional details, and attaching files.
- **Request Tracking:** Users can track the status of their service requests, including submission and resolution dates.
- **User Account Management:** Customers can view and manage their account details.
- **Admin Dashboard:** Customer support representatives can manage service requests through a dedicated admin interface.

## Technologies Used
- Python
- Django
- HTML/CSS
- Bootstrap

## Installation Instructions
To set up and run the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/gas_utility.git
   cd gas_utility
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage
- Customers can navigate to `/create-request/` to submit service requests.
- Use `/track-request/` to view the status of submitted requests.
- Visit `/account-details/` to manage account information.
- Access the Django admin interface at `/admin/` to manage service requests (login with superuser credentials).

## Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

