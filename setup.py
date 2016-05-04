import setuptools

try:
    import shoop_setup_utils
except ImportError:
    shoop_setup_utils = None


if __name__ == '__main__':
    setuptools.setup(
        name="shoop-mailchimp",
        version="0.3.4",
        description="Shoop Mailchimp Integration",
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shoop.addon": "shoop_mailchimp=shoop_mailchimp"},
        cmdclass=(shoop_setup_utils.COMMANDS if shoop_setup_utils else {}),
        install_requires=[
            'mailchimp3',
            'shoop>=3.0,<5',
        ],
    )
