from setuptools import setup, find_packages
setup(
    name="stackstats",
    python_requires=">=3.6.8",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas >=1.0.5, <2.0.0",
        "requests"
    ],
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "stats=stackstats.main:main",
        ],
    },
)
