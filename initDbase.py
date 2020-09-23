import os
os.system(
"""
flask db init
flask db migrate
flask db upgrade
"""
)
