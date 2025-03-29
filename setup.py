from setuptools import setup, find_packages

with open("src/docs/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="terminal_snake_game",
    version="1.0.3",
    author="Sweta Tanwar",
    author_email="shweta_tanwar@ymail.com",
    description="A classic Snake game implementation in Python using curses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SwetaTanwar/snake-game",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        'terminal_snake_game': ['assets/*'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment :: Arcade",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "terminal_snake_game=terminal_snake_game:main",
        ],
    },
) 