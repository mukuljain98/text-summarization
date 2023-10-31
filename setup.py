import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_desription = f.read()

__version__ = "0.0.0"

REPO_NAME = "text-summarization"
AUTHOR_USER_NAME = "mukuljain98"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "mukuljain8991@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A small NLP project",
    long_description=long_desription,
    long_desription_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)