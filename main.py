import asyncio
from pyscript import document, window
from js import Audio

# Symulacja dźwięku
def play_sound():
    sound = document.getElementById("alarm-sound")
    sound.play()

async def countdown(seconds):
    await asyncio.sleep(seconds)
    show_alert()

def start_activity(event):
    seconds = int(document.getElementById("interval-select").value)
    document.getElementById("main-menu").classList.add("hidden")
    # Uruchamiamy odliczanie w tle
    asyncio.create_task(countdown(seconds))

def show_alert():
    play_sound()
    document.getElementById("alert-window").classList.remove("hidden")

def relax_now(event):
    document.getElementById("alert-window").classList.add("hidden")
    document.getElementById("fullscreen-relax").classList.remove("hidden")

def finish_relax(event):
    document.getElementById("fullscreen-relax").classList.add("hidden")
    document.getElementById("main-menu").classList.remove("hidden")

def delay_relax(event):
    seconds = int(document.getElementById("delay-select").value)
    document.getElementById("alert-window").classList.add("hidden")
    asyncio.create_task(countdown(seconds))