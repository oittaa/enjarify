import os
from setuptools import setup, find_packages

NAME = "enjarify"
PACKAGES = find_packages()

DESCRIPTION = "Translates Dalvik bytecode (.dex or .apk) to Java bytecode (.jar)"
URL = "https://github.com/Storyyeller/enjarify"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

AUTHOR = ""
AUTHOR_EMAIL = ""
GITHUB_REF = os.environ.get("GITHUB_REF")
PREFIX = "refs/tags/"

if GITHUB_REF and GITHUB_REF.startswith(PREFIX):
    prefix_len = len(PREFIX)
    VERSION = GITHUB_REF[prefix_len:]
else:
    VERSION = "0.0.0.dev0"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    zip_safe=False,
    keywords=[
        "Android",
        "Java",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    scripts=["bin/enjarify", "bin/enjarify.bat"],
    setup_requires=[
        "wheel",
    ],
    python_requires=">=3.6",
)
