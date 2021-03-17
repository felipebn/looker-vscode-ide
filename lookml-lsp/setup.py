from setuptools import setup  # type: ignore


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='lookml-language-server',
    version='0.01',
    author='Felipe Nascimento',
    author_email='felipe.nascimento1@gmail.com',
    description='LookML Language Server Implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/felipebn/looker-vscode-ide/tree/main/lookml-lsp',
    packages=['lookml_lsp'],
    python_requires='>=3.6',
    install_requires=[
        'pygls~=0.9',
        'pyflakes~=2.2',
        'pycodestyle~=2.5',
        'yapf~=0.30'
    ],
    entry_points={
        'console_scripts': [
            'lookml_lsp=lookml_lsp.__main__:main'
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)"
    ]
)
