class Configuration:
    site_name = 'AxioDL'
    site_slogan = 'We reverse things others won\'t!'
    locked = False


configuration = Configuration


def lock_site(locked=False):
    configuration.locked = locked


def is_site_locked():
    return configuration.locked


GOOGLE_RECAPTCHA_SECRET_KEY='6LcBPK4UAAAAAF3-YpH5E1W8j48U3OCPgLuRaXME'
GOOGLE_RECAPTCHA_SITE_KEY='6LcBPK4UAAAAAKs13opqkNGd0x11HAxDdIZmyK5P'
