from setuptools import setup

setup(
    name='cryptocurrency_portfolio',
    packages=['cryptocurrency_portfolio'],
    include_package_data=True,
    install_requires=[
        # 'tkinter',
		'sqlalchemy',
		'requests',
		# 'json'
    ],
)