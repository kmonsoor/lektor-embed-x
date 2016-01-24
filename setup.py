from codecs import open
from os import path

from setuptools import setup

# Load the README.md to `long_description`
here = path.abspath(path.dirname(__file__))
try:
    from pypandoc import convert
    long_description = convert('README.md', 'rst')
except(OSError, IOError, ImportError):
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='lektor-embed-x',
    version='0.1.2',
    author=u'Khaled Monsoor',
    author_email='k@kmonsoor.com',
    description='Enables embedding of web-contents from popular sites in MarkDown(*.md) on Lektor CMS',
    license='MIT',
    url='https://github.com/kmonsoor/lektor-embed-x',
    py_modules=['lektor_embed_x'],
    install_requires=['embedx'],
    entry_points={
        'lektor.plugins': [
            'embed-x = lektor_embed_x:EmbedXPlugin',
        ]
    },
    keywords=['lektor', 'embed', 'html', 'javascript', 'embeddable', 'code generation', 'from url'],
    platforms='any',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
