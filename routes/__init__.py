
from sqlalchemy.orm import Session
from flask import Blueprint, jsonify, request, make_response
from utils.db import get_db

import logging
logs = logging.getLogger(__name__)
db = next(get_db())