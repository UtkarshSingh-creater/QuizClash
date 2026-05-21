# 🚀 QuizClash

QuizClash is a real-time multiplayer quiz platform backend built using **Django**, **Django REST Framework**, **PostgreSQL**, **Redis**, and **Django Channels**.

The project is designed to support live quiz sessions where hosts can create rooms, participants can join using room codes, and gameplay updates happen instantly using WebSockets and Redis-powered real-time communication.

---

# ✨ Features

## 🔐 Authentication System
- JWT-based authentication
- User registration and login
- Secure API access
- Role-based user handling

---

## 🏠 Quiz Room Management
- Create quiz rooms
- Unique room code generation
- Host-controlled sessions
- Multiplayer room handling

---

## ❓ Question Management
- Create quiz questions
- Multiple-choice options
- Question activation and ending
- Multiple question type support

---

## 👥 Participant System
- Join rooms using room codes
- Guest participant support
- Session-based player management
- Score tracking system

---

## ⚡ Real-Time Functionality
- Live quiz communication
- Instant score updates
- Real-time question synchronization
- Room-based event broadcasting
- Multiplayer synchronization using WebSockets

---

## 🏆 Leaderboard System
- Redis-based leaderboard handling
- Real-time rankings
- Fast score retrieval
- Live leaderboard updates

---

# 🛠️ Tech Stack

## 🔹 Backend
- Python
- Django
- Django REST Framework

---

## 🔹 Database
- PostgreSQL

Used for:
- user management
- rooms
- questions
- participants
- answers
- persistent application data

---

## 🔹 Real-Time Infrastructure
- Redis
- Django Channels
- WebSockets

Used for:
- real-time communication
- multiplayer synchronization
- event broadcasting
- leaderboard updates

---

## 🔹 Authentication
- JWT Authentication (`SimpleJWT`)

---

# 🧠 System Architecture

The backend follows a modular architecture where different Django apps handle separate responsibilities such as authentication, quiz rooms, questions, answers, participants, leaderboards, and WebSocket communication.

The project combines:
- REST APIs for standard operations
- WebSockets for real-time multiplayer communication

This architecture keeps business logic and live event handling separate and scalable.

---

# ⚡ Real-Time Features

QuizClash uses **Django Channels** and **Redis** to implement real-time multiplayer communication.

### Implemented Features
- Live quiz updates
- Real-time question activation
- Instant leaderboard updates
- Multiplayer event broadcasting
- Room-based communication
- Real-time synchronization

---

# 🗄️ Database Design

## PostgreSQL
Used as the primary relational database for storing:
- users
- quiz rooms
- questions
- participants
- answers

---

## Redis
Used as an in-memory data store for:
- WebSocket channel layers
- leaderboard caching
- fast ranking operations
- real-time event processing

---

# 📈 Scalability Focus

The backend is designed with scalability in mind through:
- modular Django applications
- asynchronous WebSocket communication
- Redis-based real-time processing
- PostgreSQL relational data handling

The architecture can later be extended for:
- Docker deployment
- cloud hosting
- distributed systems
- horizontal scaling

---

# 🚀 Future Improvements

Planned future features:
- Timer synchronization
- Tournament mode
- Analytics dashboard
- AI-generated quiz questions
- Matchmaking system
- Docker support
- Cloud deployment
- Notifications system
- Advanced leaderboard analytics

---

# 📚 Learning Outcomes

This project demonstrates concepts including:
- backend system design
- REST API development
- real-time communication
- WebSocket integration
- Redis integration
- PostgreSQL integration
- JWT authentication
- multiplayer backend architecture