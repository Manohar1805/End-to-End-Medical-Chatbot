import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templetes/chat.html"
]


for f_path in files:
    filepath=Path(f_path)
    print("f_path   >>>>>", f_path)
    dir, file_name=os.path.split(filepath)

    if dir != "":
        os.makedirs(dir,exist_ok=True)
        logging.info(f"creating the direactory {dir} for the file {file_name}")

    if (not os.path.exists(f_path) or (os.path.getsize(f_path)==0)):
        with open(f_path,'w') as f:
            pass
        logging.info(f"created the filepath {filepath}")

    else:
        logging.info(f"{file_name} already present")
    
    
