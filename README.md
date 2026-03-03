# BlogHub 🚀

A modern, feature-rich REST API for a social blogging platform built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. BlogHub enables users to create, share, and engage with blog posts through a robust voting system with JWT-based authentication.

## 🌟 Features

### Core Functionality
- ✅ **User Authentication** - Secure JWT-based authentication with OAuth2
- ✅ **User Management** - User registration, profile retrieval, and email validation
- ✅ **Blog Posts** - Create, read, update, and delete blog posts with full CRUD operations
- ✅ **Voting System** - Users can upvote/downvote posts and see aggregated vote counts
- ✅ **Search & Pagination** - Search posts by title with limit and offset pagination
- ✅ **Authorization** - Users can only modify or delete their own posts
- ✅ **CORS Support** - Cross-origin requests enabled for frontend integration

### Security Features
- 🔒 **Password Hashing** - Argon2 algorithm for secure password storage
- 🔐 **JWT Tokens** - Configurable token expiration with secure key management
- 🛡️ **OAuth2 Implementation** - Industry-standard authentication protocol
- ✔️ **Email Validation** - EmailStr validation for user registration

### Database Features
- 📦 **Database Migrations** - Alembic for version-controlled database schema management
- 📊 **Relationship Mapping** - SQLAlchemy ORM with proper foreign key relationships
- ⏰ **Timestamps** - Automatic created_at timestamps with timezone support
- 🔄 **Cascade Deletes** - Automatic cleanup of related data when users/posts are deleted

## 🏗️ Architecture

### Project Structure
```
BlogHub/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Settings management from environment variables
│   ├── database.py          # SQLAlchemy database configuration
│   ├── models.py            # SQLAlchemy ORM models
│   ├── schemas.py           # Pydantic request/response schemas
│   ├── oauth2.py            # JWT token generation and verification
│   ├── utils.py             # Utility functions (password hashing)
│   └── routers/
│       ├── auth.py          # Authentication endpoints
│       ├── post.py          # Post CRUD endpoints
│       ├── user.py          # User management endpoints
│       └── vote.py          # Voting system endpoints
├── alembic/                 # Database migrations
├── requirements.txt         # Python dependencies
├── alembic.ini             # Alembic configuration
└── README.md               # This file
```

### Database Schema
```
Users Table
├── id (Primary Key)
├── email (Unique)
├── password (Hashed)
└── created_at

Posts Table
├── id (Primary Key)
├── title
├── content
├── published (Boolean)
├── created_at
└── owner_id (Foreign Key → Users)

Votes Table
├── user_id (Foreign Key → Users, Primary Key)
├── post_id (Foreign Key → Posts, Primary Key)
```

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Login with email and password, returns JWT token |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/` | Register a new user |
| GET | `/users/{id}` | Get user profile by ID |

### Posts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/posts/` | Get all posts (with vote counts, paginated, searchable) |
| POST | `/posts/` | Create a new post |
| GET | `/posts/{id}` | Get a specific post with vote count |
| PUT | `/posts/{id}` | Update a post (owner only) |
| DELETE | `/posts/{id}` | Delete a post (owner only) |

**Query Parameters for GET /posts/:**
- `limit` (default: 5) - Number of posts to return
- `skip` (default: 0) - Number of posts to skip
- `search` (default: "") - Search term for post titles

### Votes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/votes/` | Add or remove a vote on a post |

**Vote Request Body:**
```json
{
  "post_id": 1,
  "dir": 1  // 1 to upvote, 0 to unvote
}
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sangbit1123/BlogHub.git
   cd BlogHub
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_NAME=fastapi
   DATABASE_USERNAME=postgres
   DATABASE_PASSWORD=your_password
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   ```

5. **Set up the database**
   ```bash
   alembic upgrade head
   ```

6. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

### API Documentation
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📝 Example Usage

### 1. Register a User
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
```

### 2. Login
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"
```

### 3. Create a Post
```bash
curl -X POST "http://localhost:8000/posts/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my first blog post",
    "published": true
  }'
```

### 4. Get All Posts
```bash
curl -X GET "http://localhost:8000/posts/?limit=10&skip=0&search=FastAPI" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### 5. Vote on a Post
```bash
curl -X POST "http://localhost:8000/votes/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"post_id": 1, "dir": 1}'
```

## 🔧 Technology Stack

### Backend Framework
- **FastAPI** (0.128.0) - Modern Python web framework
- **Uvicorn** - ASGI server for running FastAPI

### Database
- **PostgreSQL** - Relational database
- **SQLAlchemy** (2.0+) - Python ORM
- **Alembic** (1.18.4) - Database migration tool
- **psycopg2** - PostgreSQL adapter for Python

### Authentication & Security
- **python-jose** (3.5.0) - JWT token handling
- **passlib** (1.7.4) - Password hashing
- **Argon2** - Modern password hashing algorithm
- **cryptography** - Cryptographic recipes and primitives

### Data Validation
- **Pydantic** (2.12.5) - Data validation using Python type annotations
- **email-validator** - Email validation

### Additional Libraries
- **python-dotenv** - Environment variable management
- **python-multipart** - Form data handling
- **CORS Middleware** - Cross-origin resource sharing

## 🗄️ Database Migrations

The project uses Alembic for database migrations. To manage migrations:

### Create a new migration
```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations
```bash
alembic upgrade head
```

### Rollback migrations
```bash
alembic downgrade -1
```

### View migration history
```bash
alembic history
```

## 🔐 Authentication Flow

1. **User Registration** - User creates account with email and password
2. **Password Hashing** - Password is hashed using Argon2
3. **Login** - User provides credentials, validates password
4. **Token Generation** - JWT token created with user ID and expiration
5. **Protected Routes** - Token required in Authorization header for protected endpoints
6. **Token Validation** - FastAPI dependency verifies token and extracts user info

## 🛡️ Authorization Rules

- **Posts**: Users can only update/delete posts they own
- **Profile**: Only authenticated users can view profiles
- **Voting**: Only authenticated users can vote
- **CORS**: All origins allowed for cross-platform support

## 📊 Response Format

### Successful Response Example
```json
{
  "Post": {
    "id": 1,
    "title": "Welcome to BlogHub",
    "content": "This is an example post",
    "published": true,
    "created_at": "2026-02-11T10:30:00.123456",
    "owner_id": 1,
    "owner": {
      "id": 1,
      "email": "user@example.com",
      "created_at": "2026-02-11T10:00:00.123456"
    }
  },
  "votes": 5
}
```

### Error Response Example
```json
{
  "detail": "Post with id 999 was not found"
}
```

## 🚨 Error Handling

- **400 Bad Request** - Invalid request data or duplicate email
- **401 Unauthorized** - Missing or invalid authentication token
- **403 Forbidden** - User lacks permission for the action
- **404 Not Found** - Requested resource doesn't exist

## 🔄 Future Enhancements

- [ ] Comments system
- [ ] Post categories/tags
- [ ] Follow system
- [ ] Notifications
- [ ] Rich text editor support
- [ ] Image uploads
- [ ] Rate limiting
- [ ] Advanced analytics
- [ ] Email notifications
- [ ] Admin dashboard

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Sangbit Pramanick** - Backend developer passionate about building scalable web applications

## 🤝 Contributing

Contributions are welcome! Feel free to open issues and submit pull requests.

## 📞 Support

For issues, questions, or features requests, please open an issue on GitHub.

---

**Made using FastAPI and PostgreSQL**
