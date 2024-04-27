from setuptools import find_packages, setup

setup(
    name="tsut",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "anyio",
        "certifi",
        "charset-normalizer",
        "exceptiongroup",
        "h11",
        "httpcore",
        "httpx",
        "idna",
        "mutagen",
        "python-dotenv",
        "python-telegram-bot",
        "requests",
        "sniffio",
        "twspace-dl",
        "typing_extensions",
        "urllib3",
    ],
    entry_points={
        'console_scripts': [
            'tsut = tsut:run',
        ]
    },
    
    long_description="Twitter space downloader.",
    long_description_content_type="text/plain"
)