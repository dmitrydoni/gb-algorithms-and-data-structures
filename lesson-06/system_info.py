import sys
import os
import platform


print(f'Python: {sys.version}\nPlatform: {sys.platform} | {platform.mac_ver()[0]}\nOperating System: {os.uname()[3]}')

# Python: 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43)
# [Clang 6.0 (clang-600.0.57)]
# Platform: darwin | 10.15.3
# Operating System: Darwin Kernel Version 19.3.0: Thu Jan  9 20:58:23 PST 2020; root:xnu-6153.81.5~1/RELEASE_X86_64
