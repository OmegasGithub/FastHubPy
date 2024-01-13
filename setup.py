from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'FastHubPy',         
  packages = ['FastHubPy'],   
  version = '0.1',      
  license='MIT',        
  description = 'Utilizes the TTS service from Fasthub.net',  
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Me',                  
  author_email = '',      
  url = '',  
  download_url = 'https://github.com/OmegasGithub/FastHub/archive/refs/tags/v_0.2.tar.gz',  
  keywords = ['tts', 'fasthub', 'text to speech'],   
  install_requires=[           
          'requests',
          'pydub',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.11',
  ],
)