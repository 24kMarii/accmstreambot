try:
    import discord
    from discord.ext import commands
    from colorama import Fore
    import time
    import tracemalloc
    import os
    import ctypes
    import threading
    import pystray
    from PIL import Image
except:
    os.system("python -m pip install pillow")
    os.system("python -m pip install pystray")
    os.system("python -m pip install discord.py-self")
    os.system("python -m pip install colorama")
    os.system("python -m pip install discord")
tracemalloc.start()

ctypes.windll.kernel32.SetConsoleTitleW("ACCM.CC | Streaming Bot")

logo = f"""
                                        {Fore.BLUE}    _   ___ ___ __  __   ___ ___ 
                                        {Fore.BLUE}   /_\ / __/ __|  \/  | / __/ __|
                                        {Fore.LIGHTBLUE_EX}  / _ \ (_| (__| |\/| || (_| (__ 
                                        {Fore.LIGHTBLUE_EX} /_/ \_\___\___|_|  |_(_)___\___|
                                        {Fore.LIGHTMAGENTA_EX}           Streaming Bot
"""

print(logo + "\n")
prefix = input(f"                       {Fore.MAGENTA}Prefix:".")
token = input(f"                       {Fore.YELLOW}Token: "ODIxOTY5NzAyMjkyMDI5NDkw.GaR-gs.J8i4KNxHC8NfIasDQSWGuDeQFNf5dWFLSc8Rvc"
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print(f"                                                     {Fore.GREEN}Logged in!")
    await bot.change_presence(status=discord.Status.do_not_disturb)
    time.sleep(1.5)
    os.system('cls')
    print(logo + f"                      Username: {bot.user.name}#{bot.user.discriminator} | Id: {bot.user.id} | Servers: {len(bot.guilds)} | Friends: {len(bot.friends)}\n")
    print(f"{Fore.MAGENTA}                                                     Commands -")
    print(f"{Fore.BLUE}                                                     {prefix}purge\n                                                     {prefix}stream")


@bot.command()
async def stream(ctx, stream_game: str):
    await ctx.message.delete()
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Streaming(name=stream_game, url="https://www.twitch.tv/#"))

@bot.command()
async def purge(ctx):
    async for msg in ctx.message.channel.history(limit=100):
        try:
            await msg.delete()
        except:
            print("Couldnt delete message, skipping message.")





def minimize_to_tray(icon, item):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def restore_from_tray(icon, item):
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
    ctypes.windll.user32.SetForegroundWindow(ctypes.windll.kernel32.GetConsoleWindow())

def create_tray_icon():
    image = Image.open("retardassemoji.ico")
    menu = (
        pystray.MenuItem("Minimize to Tray", minimize_to_tray),
        pystray.MenuItem("Restore", restore_from_tray)
    )
    icon = pystray.Icon("ACCM.CC | Streaming Bot", image, "ACCM.CC | Streaming Bot", menu)
    icon.run()

def login(tokenselected):
    bot.run(tokenselected, log_handler=None)

# Create a separate thread for running the tray icon
tray_thread = threading.Thread(target=create_tray_icon)

# Start the tray thread
tray_thread.start()

# Call the login function
login(token)
