# Car Rental Hub

**Car Rental Hub** is a functional web application developed as an individual project for the **Django Basics** course at SoftUni. The project demonstrates the implementation of fundamental Django concepts, including database modeling, form handling, class-based and function-based views, and dynamic template inheritance.

---

## Key Features

* **Car Catalog:** A comprehensive list of available vehicles with detailed information.
* **Rental Management:** A system for booking cars for specific dates.
* **Review System:** Users can leave ratings and feedback for each car.
* **Full CRUD Functionality:** Implemented for both Cars and Rentals (Create, Read, Update, Delete).
* **Dynamic Design:** Fully responsive interface built with Bootstrap 5.

---

## Tech Stack

* **Framework:** Django (Latest Stable Version)
* **Database:** PostgreSQL
* **Frontend:** Django Template Language, HTML5, CSS3, Bootstrap 5
* **Backend:** Python 3.14
* **Version Control:** Git & GitHub

---

## Project Architecture

The application consists of three (3) main Django apps, each with a clear responsibility:

1.  **`cars`**: Manages the car fleet, specifications, and availability.
2.  **`rentals`**: Handles the rental process, dates, and booking logic.
3.  **`common`**: Manages the home page, custom filters, and the review system.

### Database Models & Relationships
* **Car Model:** Contains core data (brand, model, year, price, image).
* **Rental Model:** Includes a **Many-to-One** relationship with `Car`.
* **Features Model:** Linked to `Car` via a **Many-to-Many** relationship for extras (e.g., GPS, AC).
* **Review Model:** Connected to `Car` to store user ratings and comments.

---

## Installation and Local Setup

Follow these steps to set up the project locally:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/MonsterGuti/Car-Rental-Hub.git](https://github.com/MonsterGuti/Car-Rental-Hub.git)
    cd Car-Rental-Hub
    ```

2.  **Set up a Virtual Environment:**
    ```bash
    python -m venv venv
    # For Windows:
    venv\Scripts\activate
    # For macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure PostgreSQL:**
    Ensure PostgreSQL is running and create a database named `car_rental_hub_db`. 

5.  **Environment Variables & Credentials:**
    The application is configured to look for the following settings in `settings.py` or an `.env` file:
    * DB_NAME=car_rental_hub_db
    * DB_USER=postgres
    * DB_PASSWORD=marti123
    * DB_HOST=localhost
    * DB_PORT=5432
    * SECRET_KEY=cars-are-awesome`

6.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Start the Application:**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000/` in your browser.

---

## Important Notes for Evaluators

* **Data Validation:** Custom validators are implemented in forms and models to handle date logic (e.g., rental start date cannot be in the past) and numerical constraints.
* **Forms Customization:** Forms include custom error messages, labels, and placeholders. Read-only fields are used in specific views to prevent modification of key data during confirmation.
* **Templates & UI:**
    * Uses a mandatory **Base Template** with inheritance.
    * Includes **Partial Templates** for reusable components (navbars, footers, cards).
    * Features a **Custom 404 Error Page**.
    * Implements **Custom Template Filters** (e.g., `currency`).
* **Navigation:** All pages are accessible through navigation links (no orphan pages). A consistent footer and header are present on all pages.
* **Clean Code:** Follows OOP principles, high cohesion, and loose coupling.

---

## Web Pages (Templates)
The project includes more than 10 web pages:
1.  **Home Page** (Landing page)
2.  **Car Catalog** (List all objects)
3.  **Car Details Page** (Single object view)
4.  **Add Car** (Create functionality)
5.  **Edit Car** (Update functionality)
6.  **Delete Car Confirmation** (Delete functionality)
7.  **Rental Form** (Create rental)
8.  **My Rentals** (Filtered objects view)
9.  **Add Review Page** (Form handling)
10. **404 Custom Page** (Error handling) 
**and more...**

---

### License
This project is developed for the **Django Basics Regular Exam** at SoftUni.
