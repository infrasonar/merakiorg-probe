from libprobe.probe import Probe
from lib.check.organization import check_organization
from lib.check.wireless import check_wireless
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'organization': check_organization,
        'wireless': check_wireless,
    }

    probe = Probe("merakiorg", version, checks)

    probe.start()
