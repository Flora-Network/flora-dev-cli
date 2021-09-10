from setuptools import setup

if __name__ == '__main__':
    setup(
        name='fd_cli',
        version='0.0.1',
        packages=[
            'fd_cli'
        ],
        url='https://github.com/zqrx/fd-cli',
        license='GNU General Public License v2.0',
        author='zqrx',
        author_email='',
        description='',
        install_requires=[
            'click~=7.1.2',
            'chia-blockchain~=1.2.3',
            'setuptools~=57.0.0',
            'requests~=2.26.0'
        ],
        entry_points={
            'console_scripts': [
                'fd-cli = fd_cli.fd_cli:main',
                'flora-dev-cli = fd_cli.fd_cli:main'
            ]
        }
    )
