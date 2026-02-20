import asyncio
from pyscript import document, window
from js import Audio

# Symulacja dźwięku
def play_sound():
    sound = document.getElementById("alarm-sound")
    sound.play()

def stop_sound():
    sound = document.getElementById("alarm-sound")
    sound.pause()
    sound.currentTime = 0  # Przewija dźwięk do początku

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
    stop_sound()  # Zatrzymujemy dźwięk przy wejściu w relaks
    document.getElementById("alert-window").classList.add("hidden")
    document.getElementById("fullscreen-relax").classList.remove("hidden")

def delay_relax(event):
    stop_sound()  # Zatrzymujemy dźwięk przy odłożeniu przerwy
    document.getElementById("alert-window").classList.add("hidden")
    seconds = int(document.getElementById("delay-select").value)
    asyncio.create_task(countdown(seconds))

def finish_relax(event):
    document.getElementById("fullscreen-relax").classList.add("hidden")
    document.getElementById("main-menu").classList.remove("hidden")
