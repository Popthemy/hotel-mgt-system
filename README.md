# 🏨 Hotel Management System 

A simple **Hotel Management System** built with **Django (MVT)** architecture. This project allows both authenticated and anonymous users to view available room categories and explore the rooms under each category.

## ✨ Features

✅ **Home Page**
Displays all available room categories (e.g. *Single*, *Double*, *Suite*) for easy browsing.

✅ **Rooms by Category**
Clicking on a category takes you to a list of rooms belonging to that category, each showing:

* 📜 Description
* 💰 Price
* 🏷 Amenities
* 📆 Availability

> 💡 **Note:** This is a practice implementation focusing on Django MVT structure and basic data retrieval.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Django Framework**
* **HTML & CSS (Django Templates)**
* **SQLite (default database)**

---

## ⚙️ Installation and Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/hotel-mgt-system.git
   cd hotel-mgt-system
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate     # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. Visit the site at:

   ```
   http://127.0.0.1:8000/
   ```


---

## 🎯 Future Plans

* User authentication & booking system
* Search and filter rooms
* Reservation management
* Payment integration

---

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have ideas for improving this project!

---

## 📜 License

This project is for educational and practice purposes. No license specified.
