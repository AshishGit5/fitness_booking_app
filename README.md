# fitness_booking_app


```markdown
# Fitness Studio Booking API

A Django REST API that allows clients to view and book fitness classes such as Yoga and Zumba. It supports timezone-aware scheduling and simple validations.

---

## Features

- View all upcoming fitness classes (`/classes`)
- Book a class if slots are available (`/book`)
- Fetch all bookings by email (`/bookings?email=...`)
- Timezone-aware scheduling (IST → UTC handling)
- Logs and validations included

---

## Setup Instructions

### 1. Clone the repository and navigate to the project
```bash
git clone <your-repo-url>
cd fitness_booking_api
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply migrations
```bash
python manage.py migrate
```

### 4. Load seed data
```bash
python manage.py loaddata seed_data.json
```

### 5. Run the server
```bash
python manage.py runserver
```

---

## API Endpoints & Sample cURL

### GET /classes
List all upcoming classes

```bash
curl -X GET http://127.0.0.1:8000/classes/
```

---

### POST /book
Book a class by ID (ensure available slots exist)

```bash
curl -X POST http://127.0.0.1:8000/book/ \
  -H "Content-Type: application/json" \
  -d '{"class_id": 1, "client_name": "Ashish", "client_email": "ashish@example.com"}'
```

---

### GET /bookings
View bookings by client email

```bash
curl -X GET "http://127.0.0.1:8000/bookings/?email=ashish@example.com"
```

---

## Timezone Behavior

- All class times are stored in **UTC**
- Converted to **IST (Asia/Kolkata)** using Django’s `localtime()` during API response
- Ensures consistent behavior regardless of server timezone

---

## How to Run Tests

You can add test cases using Django's `TestCase` class. Example:

```bash
python manage.py test
```

(Add tests in `bookings/tests.py`)

---

## Seed Data Format

Example: `seed_data.json`

```json
[
  {
    "model": "bookings.fitnessclass",
    "fields": {
      "name": "Yoga",
      "date_time": "2025-06-06T07:00:00Z",
      "instructor": "Amit",
      "total_slots": 10,
      "available_slots": 10
    }
  }
]
```

---

## Optional Admin Access

If needed:
```bash
python manage.py createsuperuser
```

---

## Loom Video

> Refer to the Loom link provided with this README for a walkthrough of the project functionality and design.

---

## Author

Ashish R.  
Python Developer
```
