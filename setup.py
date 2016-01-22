from setuptools import setup

setup(
    name='lektor-embed-x',
    version='0.1',
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
    }
)
