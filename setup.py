from setuptools import setup, find_packages

setup(
    name='my-mkdocs-plugin',
    version='0.0.1',
    description='Some Desc',
    author='xudshen',
    author_email='some@some.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'setuptools>=18.5',
        'mkdocs>=1.0.4',
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'mymkdocsplugin = my_mkdocs_plugin.plugin:MyMkDocsPlugin'
        ]
    },
    zip_safe=False
)
