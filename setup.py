import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opydoviz-kurlari",
    version="1.1",
    author="Muhammed Çamsarı",
    license='MIT',
    author_email="Muhammedcamsari@icloud.com",
    description="Python ile guncel doviz kurlarini goruntuleyin.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muhammedcamsari/opydoviz-kurlari",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Turkish",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    scripts=["opydoviz.py"],
    install_requires = ['opy-logger>=2.0', 'lxml>=4.8.0'],

    py_modules=['opydoviz'],
    entry_points='''
        [console_scripts]
        opydoviz=opydoviz:opydoviz
    ''',
)
