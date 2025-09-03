# Rock Paper Scissors - Django Game 🎮

A beautiful, full-featured Rock-Paper-Scissors game built with Django 4.x and modern frontend technologies.

## Features ✨

### Backend (Django)
- **Django 4.x** project with clean app structure
- **Session-based storage** (no database models needed)
- **AJAX API endpoints** for game moves and reset functionality
- **Comprehensive game logic** with proper win/lose/draw detection
- **Error handling** and validation
- **Unit tests** for game logic and views

### Frontend (Modern Web Technologies)
- **Beautiful responsive UI** with CSS Grid/Flexbox
- **Smooth animations** and transitions
- **Mobile-first responsive design**
- **Real-time score tracking**
- **Game history** (last 10 games)
- **AJAX interactions** without page reloads
- **Loading states** and user feedback
- **Toast notifications** for user actions

### Game Features
- Choose between Rock (🗿), Paper (📄), or Scissors (✂️)
- Animated battle sequences
- Real-time score tracking (Player vs Computer vs Draws)
- Session-based game history
- Reset game functionality
- Responsive design for all devices

## Installation & Setup 🚀

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Quick Start

1. **Clone or download the project**
   ```bash
   # If using git
   git clone <repository-url>
   cd rock-paper-scissors-django

   # Or extract the ZIP file and navigate to the directory
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations** (creates SQLite database)
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

🎉 **You're ready to play!**

