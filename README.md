📌 FastAPI Project Explanation
This FastAPI project provides APIs to store, retrieve, and greet users using a JSON file for persistent storage.

1️⃣ Features
✅ Save User Data (/save_data) - Adds a new user with an auto-incrementing ID.
✅ Greet User (/greet/{user_id}) - Greets a user by fetching their details using user_id.
✅ View All Users (/get_saved_data) - Returns all stored users.

2️⃣ How It Works
🔹 Persistent Storage: Data is saved in data.json.
🔹 Auto-Incrementing ID: Ensures unique IDs for each user.
🔹 Validation: Uses Pydantic for request validation.
🔹 Error Handling: Returns 404 if user ID is not found.

3️⃣ Tech Used
🚀 FastAPI, Pydantic, JSON File Handling

Perfect for learning REST APIs, data persistence, and validation in FastAPI! 🎯

