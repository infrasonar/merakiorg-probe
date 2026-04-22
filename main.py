from libprobe.probe import Probe
from lib.check.organization import CheckOrganization
from lib.check.wireless import CheckWireless
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckOrganization,
        CheckWireless,
    )

    probe = Probe("merakiorg", version, checks)

    probe.start()
