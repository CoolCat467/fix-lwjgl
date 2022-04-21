# fix-lwjgl
Fix LWJGL (Light Weight Java Game Library) java classpath data for ARM devices

## Description
This script is a wrapper for launching Minecraft on devices that aren't properly
supported by Mojang, such as computers running Raspberry Pi OS. On these devices,
the wrong version of LWJGL is downloaded, preventing minecraft from working
properly. This program takes the arguments that would have been used to run
Minecraft and rewrites a few details about LWJGL, pointing minecraft to use a
user-specified folder as the LWJGL library library path for the shared object
files and in the case of LWJGL 3, completely re-writing the java class path
information to use the correct files.

## Testing
This program has been tested successfully with [ATLauncher](https://github.com/ATLauncher/ATLauncher)
on a Raspberry Pi 4 running 64 bit Raspberry Pi OS bullseye. It should work
for 32 bit Raspberry Pi OS bullseye, but I have not tested that yet.

This *might* work on the new Apple M1 chips, as they are arm64 processors,
but this is unlikely. I have not tested this either.

If possible, if this script works on anything not listed as tested, please
tell me using discussions.

## Installation
Download `fix_lwjgl.py` onto your computer, ensure Python 3 is installed, and use pip to
install everything in `requirements.txt`

```bash
wget https://raw.githubusercontent.com/CoolCat467/fix-lwjgl/HEAD/fix_lwjgl.py && pip install aiohttp async-timeout && chmod +x fix_lwjgl.py
```
The first time you run Minecraft using this wrapper, if the user defined lwjgl directory
does not exist in the case of LWJGL 2 or any of the modules are not found in LWJGL 3,
the wrapper will automatically download all the files required.

If it needs the lwjgl 2 folder, it will download the folders in this repository.
If it needs any lwjgl 3 modules, it will download them from lwjgl's build repository
available to browse at https://www.lwjgl.org/browse

## Usage
Go to your Minecraft launcher, and somewhere in settings is likely the ability to
set a "wrapper command". Set it to `fix_lwjgl.py` and everything *should* be good.

On Raspberry Pi OS bullseye in particular, it might be useful to have this "pre-launch"
command if you are experiencing crashes:
```bash
export MESA_GL_VERSION_OVERRIDE=4.2COMPAT
```
This tells mesa gl to pretend it's OpenGL 4.2, which stops Minecraft from trying to do
some things that might cause crashes.

## Problems
If you encounter any issues regarding this program, please check and see if anyone else is
having the same issue before making a new issue.
When posting your issue, be sure to include any relevant logs and what operating system
you're using and what architecture your computer's processor uses.

Additionally, re-running Minecraft with the additional arguments
```bash
-Dorg.lwjgl.util.DebugLoader=true -Dorg.lwjgl.util.Debug=true
```
might help diagnose your issue. Just be sure to remove them after everything is
fixed, because OpenGL errors cause crashes in debug mode instead of just being silently
ignored.
