----------------------------------------  
Keylogger with Active Window Tracking  
----------------------------------------  

**Author**: Eclipsemanic  

----------------------------------------  
### DESCRIPTION  
A Python script that logs keystrokes and tracks active window changes. Data is saved to `key_log.txt`, including timestamps for application/window switches. Special keys are formatted for readability.  

----------------------------------------  
### FEATURES  
- Logs keystrokes to a text file.  
- Tracks active window titles (e.g., "Chrome" or "Notepad").  
- Maps special keys (e.g., [ENTER], [SHIFT], [CTRL]).  
- Runs in the background until stopped with Ctrl+C.  

----------------------------------------  
### INSTALLATION  
1. **Install Dependencies**:  
   Run these commands in your terminal:  
   pip install pynput pygetwindow  

2. **Download Script**:  
   Save the script as `keylogger.py`.  

----------------------------------------  
### USAGE  
1. **Start the Keylogger**:  
   Run the script:  
   python keylogger.py  

2. **Stop the Keylogger**:  
   Press Ctrl+C in the terminal.  

3. **View Logs**:  
   Open `key_log.txt` to see keystrokes and window changes.  

----------------------------------------  
### EXAMPLE LOG  
-------- Switched to: Document1 - Notepad --------  
H e l l o [SPACE][ENTER]  
-------- Switched to: Chrome --------  
h t t p s : / / g i t h u b . c o m [ENTER]  

----------------------------------------  
### DISCLAIMER  
- **Educational use only**.  
- Use only with **explicit permission** on systems you own.  
- The author is not responsible for misuse.  

----------------------------------------  
### LICENSE  
Free and open-source. Modify and redistribute freely.  

----------------------------------------  
**Author**: eclipsemanic  
**GitHub**: https://github.com/EclipseManic
