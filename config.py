import os
BASE_DIRS=os.path.dirname(__file__)
options={
    "port":9001,
}

settings={
    # "autoreload":True,
    "static_path":os.path.join(BASE_DIRS,'static'),
    "template_path":os.path.join(BASE_DIRS,'template')
}