from setuptools import find_packages, setup 

setup(
    name = "smartgrid",
    version = "0.1.0",
    author="Syed Adnan Zafar",
    author_email='sa.zafar7101@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[]
)