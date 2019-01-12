# https://stackoverflow.com/a/51704613
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

DEFAULT_LOGGER = 'rlbot'


def upgrade():
    package = 'rlbot'

    import importlib

    try:
        # https://stackoverflow.com/a/24773951
        importlib.import_module(package)

        from rlbot.utils import public_utils, logging_utils

        logger = logging_utils.get_logger(DEFAULT_LOGGER)
        if not public_utils.have_internet():
            logger.log(logging_utils.logging_level,
                       'Skipping upgrade check for now since it looks like you have no internet')
        elif public_utils.is_safe_to_upgrade():
            import os
            requirements = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pkgs', 'rlbot_gui', 'requirements.txt')
            pipmain(['install', '-r', requirements, '--upgrade', '--upgrade-strategy=eager'])

    except (ImportError, ModuleNotFoundError):
        pipmain(['install', package])


if __name__ == '__main__':
    upgrade()
