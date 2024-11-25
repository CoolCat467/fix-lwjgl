# fix-lwjgl
Fix which LWJGL (Light Weight Java Game Library) version is used in Minecraft for ARM devices

<!-- BADGIE TIME -->

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/CoolCat467/fix-lwjgl/main.svg)](https://results.pre-commit.ci/latest/github/CoolCat467/fix-lwjgl/main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![code style: black](https://img.shields.io/badge/code_style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

<!-- END BADGIE TIME -->

## Description
This script is a wrapper for launching Minecraft on devices that aren't properly
supported by Mojang, such as computers with ARM processors like the Raspberry Pi 3 and 4,
as well as Apple's new M series chips.
On these devices, the wrong version of LWJGL is downloaded, preventing minecraft
from launching properly. This program takes the arguments that would have been
used to run Minecraft and rewrites a few details about LWJGL, pointing minecraft
to use a user-specified folder as the LWJGL library library path for the
shared object files and in the case of LWJGL 3, changing the
java class path information to use the correct files for your machine.

Basically, it means minecraft works now!

## Testing
This program has been tested successfully with [ATLauncher](https://github.com/ATLauncher/ATLauncher)
on a Raspberry Pi 4 running 64 bit Raspberry Pi OS bullseye. It should work
for 32 bit Raspberry Pi OS bullseye, but I have not tested that yet.

## Success testimonials
The following ARM64 platforms have run Minecraft successfully with this script:
- M3 Mac with macOS - [Eagle3820](https://github.com/Eagle3820)
- [Orange Pi 5](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html) with Ubuntu - [Lolmc0587](https://github.com/Lolmc0587)
- M2 Max Mac with [Asahi Fedora Remix](https://asahilinux.org/fedora/) - [agouin](https://github.com/agouin)


This script might also work other platforms with arm processors, but may require minor changes.

If possible, if this script works on anything not listed as tested, please
tell me using [the discussions page](https://github.com/CoolCat467/fix-lwjgl/discussions/1)!

## Installation
Ensure Python 3 is installed on your computer, and use pip to
install this project with the command listed below:

```
pip install git+https://github.com/CoolCat467/fix-lwjgl.git
```

#### Installation on MacOS
If you are using MacOS, you will probably have to install [homebrew](https://brew.sh/) to install [pipx](https://pipx.pypa.io/latest/installation/)
(use the links given, not copying their install instructions here because they will get out of date).

After pipx is installed, you can use the following command to install:

```
pipx install git+https://github.com/CoolCat467/fix-lwjgl.git
```

## About Installation
On default, all LWJGL files are expected to be in
`$HOME/.local/share/fix_lwjgl/lwjgl_{lwjgl_version}{system_arch}`, so
if the script was run on Raspberry Pi OS 32 bit, it would be `lwjgl_3arm32`. If this
folder does not exist or files are missing (only checks in LWJGL 3 mode), the folder
is created and all required files are downloaded from https://build.lwjgl.org/
(browse at https://www.lwjgl.org/browse) (see also `can_download` in configuration)

If this script needs the LWJGL 2 folder, it will download the folders in this repository.
If this script needs any LWJGL 3 modules, it will download them from LWJGL's build repository
available to browse at https://www.lwjgl.org/browse

## Configuration
All configuration files should be located in `~/.config/fix_lwjgl/fix_lwjgl_config.ini`. The current options
as of writing include:
- `lwjgl_base_path` - Controls where the lwjgl folders are expected to live at (defaults to `$HOME/.local/share/fix_lwjgl`)
- `can_download` - If the wrapper is allowed to download files from the internet (defaults to True)
- `download_timeout` - Timeout in seconds for downloading files from the internet (defaults to 15 seconds)

## Usage
Go to your Minecraft launcher, and somewhere in settings is likely the ability to
set a "wrapper command". Set it to `fix_lwjgl_wrapper` after you install the script
and everything *should* be good.

On Raspberry Pi OS bullseye and some other platforms, it might be useful to have this
"pre-launch" command if you are experiencing crashes:

```bash
export MESA_GL_VERSION_OVERRIDE=4.2COMPAT
```

This tells mesa gl to pretend it's OpenGL 4.2, which stops Minecraft from trying to do
some things that might cause crashes.

You might also want to try changing it from `4.2COMPAT` to `4.3` or `4.5`, this is known to fix the
["Could not initialize class com.mojang.blaze3d.systems.RenderSystem" issue](https://github.com/CoolCat467/fix-lwjgl/issues/30)

## Problems
If you encounter any issues regarding this program, please check and see if anyone else is
having the same issue before making a new issue.
When posting your issue, be sure to include any relevant logs and what operating system
you're using and what architecture your computer's processor uses.

Additionally, re-running Minecraft with the additional arguments
```
-Dorg.lwjgl.util.DebugLoader=true -Dorg.lwjgl.util.Debug=true
```
might help diagnose your issue. Just be sure to remove them after everything is
fixed, because OpenGL errors cause crashes in debug mode instead of just being silently
ignored.


### Links
* Source Code - https://github.com/CoolCat467/fix-lwjgl.git
* Issues      - https://github.com/CoolCat467/fix-lwjgl/issues

### License
-------
Code and documentation are available according to the MIT License (see [LICENSE](https://github.com/CoolCat467/fix-lwjgl/blob/HEAD/LICENSE)).
