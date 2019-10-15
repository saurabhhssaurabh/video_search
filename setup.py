from io import open

from setuptools import find_packages, setup

with open('video_search/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = [
    'gensim',
    'pandas',
    'scikit-learn',
    'nmslib==1.7.3.2',
    'joblib',
    'h5py',
    'spacy==2.0.11',
    'nltk==3.4.5',
    # 'wikipedia==1.4.0',
    'Flask==1.0.2',
    'Flask-Cors==3.0.6',
    'Flask-RESTful==0.3.6',
    'gunicorn',
    'Pillow==5.0.0',
    'moviepy',
    'opencv-python',
    'face-recognition==1.2.2',
    'face-recognition-models==0.3.0'
]

setup(
    name='video_search',
    version=version,
    description='',
    long_description=readme,
    author='Malar Invention',
    author_email='malarkannan.invention@gmail.com',
    maintainer='Malar Invention',
    maintainer_email='malarkannan.invention@gmail.com',
    url='https://github.com/malarinv/video_search',
    license='MIT/Apache-2.0',
    keywords=['search', 'video'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'searchui = video_search.server:main',
        ],
    })
