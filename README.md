# 🌐 Dark Comm Terminal Chat

A beautiful, feature-rich terminal-based chat application with streaming text, color coding, and modern UI/UX.

## ✨ Features

- **Beautiful Terminal UI**: Rich, colorful interface that looks great in any terminal
- **Streaming Text**: Messages appear character by character (like AI text generation)
- **Adaptive Streaming Speed**: All messages complete within exactly 2 seconds regardless of length
- **User Color Coding**: Each user gets a unique color for easy identification
- **Modern Prompts**: Beautiful input prompts with user identification
- **Real-time Chat**: Multiple users can chat simultaneously
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup Environment

```bash
python setup.py
```

This creates a `.env` file with default settings:
- Server IP: localhost
- Port: 12345

### 3. Start the Server

```bash
python start_server.py
```

### 4. Start Clients

In separate terminal windows:

```bash
python start_client.py
```

### Alternative: Direct Module Execution

You can also run the modules directly:

```bash
# Server
python server/server.py

# Client
python client/client.py
```

## 🎨 Features in Detail

### Streaming Text Animation
- Messages stream character by character
- Speed automatically adjusts to complete in exactly 2 seconds
- Creates a smooth, AI-like typing effect

### Color System
- Each user gets a unique color
- Colors are assigned automatically when users join
- 13 different colors available for user identification

### Beautiful UI Elements
- Welcome screen with ASCII art
- Colored usernames and messages
- Clean, modern terminal interface
- Real-time connection status

## 🔧 Configuration

Edit the `.env` file to change server settings:

```env
SERVER_IP=localhost
PORT=12345
```

## 📱 Usage

1. **Start the server** in one terminal
2. **Start clients** in other terminals
3. **Enter your username** when prompted
4. **Type messages** and press Enter
5. **Type 'exit'** to leave the chat

## 🛠️ Technical Details

- **Modular Architecture**: Separate socket handling modules for client and server
- **Client-Server Architecture**: Central server handles message broadcasting
- **Threading**: Non-blocking message handling
- **JSON Protocol**: Structured message format
- **Rich Library**: Beautiful terminal UI components
- **Colorama**: Cross-platform color support

## 📁 Project Structure

```
Dark-Comm/
├── server/
│   ├── __init__.py
│   ├── server.py          # Main server application
│   └── socket_handler.py  # Server socket handling module
├── client/
│   ├── __init__.py
│   ├── client.py          # Main client application
│   └── socket_handler.py  # Client socket handling module
├── start_server.py        # Server launcher
├── start_client.py        # Client launcher
├── requirements.txt       # Dependencies
├── setup.py              # Setup script
└── README.md             # This file
```

## 📦 Dependencies

- `colorama`: Cross-platform colored terminal text
- `rich`: Rich text and beautiful formatting in the terminal
- `python-dotenv`: Environment variable management

## 🎯 Requirements Met

✅ **Nice UI/UX in terminal** - Rich, colorful interface with modern design  
✅ **Streaming text display** - Character-by-character animation like AI text generation  
✅ **Adaptive streaming speed** - All messages complete in exactly 2 seconds  
✅ **Color coding** - Each user gets unique colors for identification  
✅ **Beautiful prompts** - Modern input prompts with user identification  

## 🚀 Future Enhancements

- Multiple chat rooms
- File sharing
- Message history persistence
- User authentication
- Emoji support
- Custom themes

---

**Enjoy your beautiful terminal chat experience!** 🎉
