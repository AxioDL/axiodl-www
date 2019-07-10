class Configuration:
    site_name = 'AxioDL'
    site_slogan = 'We reverse things others won\'t!'
    locked = False


configuration = Configuration


def lock_site(locked=False):
    configuration.locked = locked


def is_site_locked():
    return configuration.locked
