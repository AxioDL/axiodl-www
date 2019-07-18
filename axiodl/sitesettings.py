class Configuration:
    site_name = 'AxioDL'
    site_slogan = 'We reverse things others won\'t!'
    locked = False


configuration = Configuration


def lock_site(locked=False):
    configuration.locked = locked


def is_site_locked():
    return configuration.locked


GOOGLE_RECAPTCHA_SITE_KEY='6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI' # Google Test key - Replace immediately with your key
GOOGLE_RECAPTCHA_SECRET_KEY='6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe' # Google Test key - Replace immediately with your key
