from setuptools import setup

setup(
    name='lektor-embed-x',
    version='0.1',
    author=u'Khaled Monsoor',
    author_email='k@kmonsoor.com',
    license='MIT',
    py_modules=['lektor_embed_x'],
    install_requires=['lektor', 'embedx']
    entry_points={
        'lektor.plugins': [
            'embed-x = lektor_embed_x:EmbedXPlugin',
        ]
    }
)
