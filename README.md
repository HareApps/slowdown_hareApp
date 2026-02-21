SlowDown HareApp
Rest your eyes, refresh your mind.
SlowDown HareApp is a lightweight, Python-powered Progressive Web App (PWA) designed to help users combat eye strain and mental fatigue. By setting customizable activity intervals, the app reminds you to take a step back, breathe, and enjoy a moment of relaxation.
It was entirely vibe coded in AI Studio and with a help of Gemini AI by a non-technical person as I am
Features
Python in the Browser: Leverages PyScript to run Python logic directly in the client-side environment.
Customizable Intervals: Choose between 30 minutes, 1 hour, 2 hours,
Delayed Relax: Not ready to stop yet? Use the "DelayRelax" feature to snooze the alert for a few more minutes.
Immersive Experience: A full-screen relaxation mode featuring calming visuals.
PWA Ready: Includes a web manifest and service worker, allowing it to be "installed" on mobile or desktop and work offline.
Audio Alerts: Features a gentle piano notification to grab your attention.
Tech Stack
Component
Technology
Logic
Python 3.x (via PyScript)
Frontend
HTML5, CSS3
Offline Support
Service Workers & Web Manifest (PWA)
Interactivity
Asyncio for non-blocking timers
Project Structure
index.html: The main UI structure and styling.
main.py: The core Python logic handling timers, sounds, and UI state.
manifest.json: Configuration for PWA installation (icons, theme colors).
sw.js: Service Worker for caching assets and offline functionality.
pyscrip.json: Configuration file defining required assets for the PyScript runtime.
How to Run Locally
Since this app uses PyScript and Service Workers, it is best served via a local web server to avoid CORS issues.
Clone the repository:
Bash
git clone https://github.com/HareApps/SlowDown_HareApp.git
cd SlowDown_HareApp
Start a local server:
If you have Python installed, run:
Bash
python -m http.server 8000
Open the app:
Navigate to http://localhost:8000 in your web browser.
Internet browser
Open the address https://hareapps.github.io/slowdown_hareApp/. It works on desktop and a mobile
Usage
Set the Timer: Select your desired work interval from the dropdown.
Work: Click Start Activity. The app will run in the background.
Relax: When the "Hare" alerts you, click RelaxNow to enter full-screen mode, or DelayRelax if you need a few more minutes.
Return: Click anywhere or press a key in the full-screen view to return to the main menu.
Credentials to
KevinSchmid for his kevinschmid-aurora-borealis-4965488_1920.jpg picture made available in Pixabay.com. For the purpose of the App it was renamed to zorza.jpg
SoundReality - Pixabay, for the piano sound soundreality-notification-piano-443094.mp3
AI Studio and Gemini AI who helped a non-technical person as I am to vibe code the App.
Thank you for your contributions.
License
This project is open-source with Apache License 2.0. Feel free to fork it and add your own relaxation features!
