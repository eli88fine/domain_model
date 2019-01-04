from setuptools import setup
from setuptools import find_packages

setup(name='domain_model',
      version='0.3',
      description='Abstract classes and base implementations for isolating domain models and business logic from implementation details relating to persistence, while also allowing business logic to determine when to persist.',
      url='https://git-codecommit.us-east-1.amazonaws.com/v1/repos/domain_model',
      author='Coyne Scientific',
      author_email='efine@coynesci.com',
      #license='AGPL3'
      # The easiest way to make sure there are no legal issues related to distributing any of our
      # software is distributing under the AGPL3 license
      package_dir={"": "src"},
      packages=find_packages(where="src"),#['src/domain_model'],
      install_requires=open('requirements.txt').readlines(),
      setup_requires=open('setup-requirements.txt').readlines(),
      tests_require=open('test-requirements.txt').readlines(),
      )
