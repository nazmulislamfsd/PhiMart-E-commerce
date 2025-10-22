# 🛒 Phimart — E-commerce REST API

Phimart is a fully functional **E-commerce REST API** built with **Django Rest Framework (DRF)**.  
It provides all core features of a modern e-commerce backend including **Products**, **Categories**, **Carts**, **Orders**, and **User Authentication** (via JWT).  
The project also includes interactive API documentation using **Swagger UI** and **ReDoc**.

---

## 🚀 Features

✅ **User Authentication**
- Register, login, logout using **JWT Authentication**  
- Implemented with **Djoser** for simplicity and security  

✅ **Product Management**
- CRUD operations for products  
- Filter products by category, price, etc.  

✅ **Category Management**
- Manage product categories  
- Supports nested category structure  

✅ **Cart System**
- Add/remove items from cart  
- Update item quantity  
- Automatically calculates total price  

✅ **Order Management**
- Create orders from cart items  
- View user order history  

✅ **API Documentation**
- Auto-generated API docs using **drf_yasg**
- Accessible through Swagger UI and ReDoc  

---

## 🏗️ Tech Stack

| Technology | Purpose |
|-------------|----------|
| **Python** | Programming language |
| **Django** | Web framework |
| **Django REST Framework** | API framework |
| **Djoser** | JWT authentication endpoints |
| **drf-yasg** | API documentation |
| **PostgreSQL** | Database |
| **Simple JWT** | Token-based authentication |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/phimart.git
cd phimart
```
### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # for Windows
source venv/bin/activate     # for Mac/Linux
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Apply migrations
```bash
python manage.py migrate
```
### 5️⃣ Create a superuser
```bash
python manage.py createsuperuser
```
### 6️⃣ Run the development server
```bash
python manage.py runserver
```
Then open your browser and go to 👉
http://127.0.0.1:8000/

## 📚 API Documentation

You can explore and test all API endpoints from the interactive docs:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

## 🧠 Future Improvements:

* Payment gateway integratio(Stripe/SSLCommerz)

## 🧑‍💻 Author:

__Md. Nazmul Islam__

🎓 Computer Science & Technology, Rangpur Polytechnic Institute

📧 Email: [nazmulislamfsd@gmail.com
]

🌐 GitHub: nazmulislamfsd

## 🌱 Environment Variables

Create a ```.env``` file in the root of your project directory and add the following variables:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=your_database_url
EMAIL_HOST=your_email_host
```