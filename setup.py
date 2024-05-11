from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# exec(open('cnvpytor/version.py').read())

setup(
    name='autocnv',
    version='1',
    author='Fan, Chunna and Wang, Zhonghua and Sun, Yan and Sun, Jun and Liu, Xi and Kang, Licheng and Xu, Yingshuo and Yang, Manqiu and Dai, Wentao and Song, Lijie and Wei, Xiaoming and Xiang, Jiale and Huang, Hui and Zhou, Meizhen and Zeng, Fanwei and Huang, Lin and Xu, Zhengfeng and Peng, Zhiyu',
    packages=['autocnv'],
    package_dir={'autocnv': 'autocnv'},
    description='autocnv',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zhonghua-wang/autocnv',
    install_requires=[
        'pysam>=0.16',
        'pandas>=1.2.5',
        'pyfaidx',
        'gtfparse>=1.2.1',
    ],
    entry_points={
        'console_scripts': [
            'autocnv = autocnv.__main__:main'
        ]
    })