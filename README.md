# 📋 TaskMaster - A Simple Task Management Microservice

TaskMaster is a lightweight **Flask-based task management system** that allows users to **create, assign, and manage tasks efficiently**. This microservice ensures data persistence using **SQLite** and follows software inclusivity and quality heuristics.

## 🎯 Features
✅ **Create Tasks** – Users can add new tasks via a simple web interface.  
✅ **Assign Tasks** – Tasks can be assigned to team members.  
✅ **Set Deadlines** – Users can specify deadlines for each task.  
✅ **Delete Tasks** – Tasks can be removed when completed.  
✅ **Database Storage** – Tasks are stored in an SQLite database (`tasks.db`) for persistence.  
✅ **Easy-to-Use UI** – Clean, simple, and accessible interface.  

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/brookcs3/taskmaster.git
cd taskmaster
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
```

### **3️⃣ Activate the Virtual Environment**
#### 🔹 **Windows (PowerShell)**
```bash
venv\Scripts\activate
```
#### 🔹 **Mac/Linux**
```bash
source venv/bin/activate
```

### **4️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application
1️⃣ **Ensure the virtual environment is activated.**  
2️⃣ **Start the Flask application:**
```bash
python app.py
```
3️⃣ **Open your browser and go to:**
```
http://127.0.0.1:5000/
```

---

## 🛠 Database Setup & Management

TaskMaster uses **SQLite** to store task data. The database is automatically created when the application runs.

### **🗄️ Viewing the Database**
To manually inspect or modify `tasks.db`, use SQLite:

```bash
sqlite3 instance/tasks.db
```

### **🔍 List All Tables**
```sql
.tables
```

### **📌 View All Tasks**
```sql
SELECT * FROM task;
```

### **🗑️ Delete a Task**
```sql
DELETE FROM task WHERE id=1;
```

### **💾 Exit SQLite**
```sql
.exit
```

---

## ✅ Running Tests
TaskMaster includes tests to ensure correct functionality.

### **Run All Tests**
```bash
pytest test_app.py
```

### **Expected Output**
```
test_app.py .... [100%]
4 passed in 0.65s
```

---

## 📦 Creating a GitHub Release
1️⃣ Commit and push your latest changes:
```bash
git add .
git commit -m "Finalized TaskMaster"
git push origin main
```
2️⃣ Go to your GitHub repository.  
3️⃣ Click on **"Releases" → "Create a new release"**.  
4️⃣ Use **Tag version: `v1.0`** and **Title: "Final Submission - Assignment 5"**.  
5️⃣ Click **"Publish Release"**.  

📌 **Take a screenshot of this page for submission.**

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👨‍💻 Contributing
Pull requests are welcome! If you’d like to contribute:
1️⃣ Fork the repository  
2️⃣ Create a feature branch (`git checkout -b new-feature`)  
3️⃣ Commit your changes (`git commit -m "Added feature"`)  
4️⃣ Push to the branch (`git push origin new-feature`)  
5️⃣ Open a Pull Request  

---

## 🛠 Built With
- **Flask** – Web framework
- **SQLite** – Database
- **HTML, CSS** – Frontend
- **Python** – Backend scripting
- **Git & GitHub** – Version control

---

## 📩 Contact
For any questions, feel free to reach out via GitHub issues.

---

🚀 **Now you're ready to run TaskMaster!**  
