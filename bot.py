from discord.ext import commands
import settings
import os

from run import run_django

client = commands.Bot(command_prefix=settings.Prefix)
client.remove_command('help')

cogs = []
skip_files = {"__init__.py", "models.py"}

for root, dirs, files in os.walk('core'):
    for f in files:
        # skip the subdirs models and migrations

        if root.endswith("migrations"):
            continue
        # skip any non .py file
        if not f.endswith(".py"):
            continue
        # also skip __init__.py files
        if f in skip_files:
            continue
        # remove .py from filename
        f = f[:-3]

        # add filename including full root and subst \ to .
        cogs.append(os.path.join(root, f).replace("\\", "."))

if __name__ == "__main__":
    run_django()
    for i in cogs:
        client.load_extension(i)
        print("Loaded ", i)

    client.run(settings.TOKEN)
