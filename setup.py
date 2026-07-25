from setuptools import setup, find_packages


setup(

    name="passguard",

    version="1.0.0",

    description="Privacy-first password security analyzer",

    author="Viranske",

    packages=find_packages(),

    entry_points={

        "console_scripts": [

            "passguard=app.main:main"

        ]

    },

)
