# Password Generator

A secure and user-friendly desktop application for generating random passwords with real-time strength analysis.

## ✨ Features

- **Secure Password Generation**: Generate cryptographically secure passwords using advanced algorithms
- **Real-time Strength Analysis**: Visual password strength indicator with progress bar
- **Customizable Options**: Choose from lowercase, uppercase, digits, and symbols
- **One-Click Copy**: Instantly copy generated passwords to clipboard
- **Dark/Light Theme**: Toggle between themes for comfortable viewing
- **Standalone Executable**: No installation required - just download and run!

## 🚀 How to Use

### For End Users (Easy)
1. Download the `password_generator.exe` file
2. Double-click to launch the application
3. No installation or dependencies required

### For Developers
```bash
pip install pyperclip
python password_generator.py

🎮 How It Works
Main Interface
Enter your desired password length (1-128 characters)

Select character types using checkboxes

Click "Generate Password" to create a secure password

Use "Copy to Clipboard" to instantly copy the password

Password Strength System
Weak (Red): Basic password with limited character variety

Medium (Orange): Good password with multiple character types

Strong (Green): Excellent password with full character diversity

Theme System
Toggle between light and dark themes using the theme button

Theme preference is maintained during session

📊 Character Options
Lowercase Letters: a-z (26 characters)

Uppercase Letters: A-Z (26 characters)

Digits: 0-9 (10 characters)

Symbols: @!%$#&*-? (9 special characters)

📁 Project Structure
password_generator.exe - Standalone executable for Windows

password_generator.py - Main application source code

icon.png - Application icon

🔒 Security Features
Uses Python's secrets module for cryptographically secure random generation

Ensures at least one character from each selected character set

Implements proper shuffling to avoid predictable patterns

No data collection or internet connection required

💡 Tips for Best Experience
Use Longer Passwords: 12+ characters for optimal security

Enable All Character Types: Maximize password strength

Regular Updates: Generate new passwords for different services

Theme Preference: Switch to dark mode for reduced eye strain

🔧 Technical Details
Built with Python and Tkinter for cross-platform compatibility

Uses system clipboard integration for easy copying

Implements efficient password strength calculation

Supports high-DPI displays and responsive layout

Includes comprehensive error handling

🎯 Ideal For
Creating secure account passwords

Generating API keys and tokens

Password reset scenarios

Security-conscious users who need strong passwords

Developers testing password validation systems