# Car Rental Hub

Car Rental Hub is a full-stack Django web application developed as an individual project for the **Django Advanced
Course @ SoftUni**.  
The project demonstrates advanced Django concepts, User register, login/logout, REST API development, asynchronous
processing, and production deployment.

---

## Key Features

- User Authentication (Register, Login, Logout)
- Extended User Profile system
- User Groups & Permissions (Admin / Regular Users)
- Car Catalog with detailed specifications
- Rental Management System
- Review & Rating System
- Notifications System (async)
- Full CRUD for Cars, Rentals, and Reviews
- REST API (Django REST Framework)
- Asynchronous task processing
- Fully responsive UI (Bootstrap 5)

---

## Tech Stack

- **Backend:** Django 6.x, Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** Django Templates, HTML5, CSS3, Bootstrap 5
- **Async:** Background tasks (notifications)
- **Server:** Gunicorn + Nginx
- **Deployment:** AWS (EC2)
- **Version Control:** Git & GitHub

---

## Project Architecture

The application is modular and consists of **five (5) Django apps**:

- `cars` -> Car management (catalog, details, CRUD)
- `rentals` -> Booking system and rental logic
- `common` -> Home page, reviews, filters
- `accounts` -> Authentication, user profiles, permissions
- `notifications` -> Async notifications system

---

## Database Models & Relationships

The project includes multiple relational models:

- **User & Profile** (One-to-One)
- **Car**
- **Rental** -> Many-to-One with Car and User
- **Review** -> Many-to-One with Car and User
- **Feature** -> Many-to-Many with Car
- **Notification**

### Relationships:

- Two+ Many-to-One relationships
- Two+ Many-to-Many relationships
- Model inheritance and encapsulation

---

## Forms & Validation

- 7+ Django forms implemented
- Custom validation logic (dates, availability, constraints)
- User-friendly error messages
- Customized labels, placeholders, help texts
- Disabled/read-only fields in key forms
- Confirmation pages before delete actions

---

## Views & Business Logic

- ~90% Class-Based Views (CBVs)
- Proper GET/POST handling
- Redirects after successful actions
- Mixins and reusable logic

---

## REST API

The project includes RESTful endpoints built with **Django REST Framework**:

- API for Cars / Rentals / Reviews
- Serializers for data validation and transformation
- Permission-based access control

### Example endpoints:

```
/api/cars/
/api/rentals/
```

---

## Templates & Frontend

- 15+ templates
- 10+ dynamic pages
- Full CRUD UI
- Template inheritance (base.html)
- Reusable partials (navbar, footer, components)
- Custom template filters
- Custom error pages (404, 500)
- Responsive design (Bootstrap 5)

---

## Asynchronous Processing

- Background tasks implemented (notifications system)
- Async logic for improved performance and user experience

---

## Security

- CSRF protection enabled
- XSS protection via Django templates
- SQL Injection prevention (ORM)
- Environment variables for sensitive data
- Authentication & permissions system

---

## Testing

- 15+ tests implemented
- Coverage for:
- Models
- Views
- Authentication logic

---

## Deployment (AWS)

The application is deployed using:

- AWS EC2 (Ubuntu server)
- Gunicorn (WSGI server)
- Nginx (reverse proxy)
- PostgreSQL database

### Live URL:

```
http://16.16.140.89/
```

---

## Installation & Local Setup

### 1. Clone repository

```bash
git clone https://github.com/MonsterGuti/Car-Rental-Hub.git
cd Car-Rental-Hub
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / Mac
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Environment Variables

Create `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=car_rental_hub_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Apply migrations

```bash
python manage.py migrate
```

---

### 6. Run server

```bash
python manage.py runserver
```

---

## Important Notes

- Clean architecture (high cohesion, loose coupling)
- Follows OOP principles
- Modular and scalable structure
- No orphan pages (all accessible via navigation)

---

## Evaluation Coverage

This project satisfies all requirements for:

- Advanced Django functionality
- REST API implementation
- Async processing
- Deployment
- Testing
- Security
- Documentation

---

## License

This project is developed for educational purposes as part of the **Django Advanced Course @ SoftUni**.