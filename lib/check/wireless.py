from typing import Any
from libprobe.asset import Asset
from ..query import query


async def check_wireless(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict[str, list[dict[str, Any]]]:

    org_id = config.get('id')
    if not org_id:
        raise Exception(
            'Missing organization ID in asset collector configuration')

    req = f'/organizations/{org_id}/devices?productTypes[]=wireless'
    resp = await query(asset, asset_config, asset_config, req)

    items: list[dict[str, Any]] = []
    for device in resp:
        # try:
        #     datestr = device['configurationUpdatedAt']
        #     configuration_updated_at = \
        #         int(datetime.datetime.fromisoformat(datestr).timestamp())
        # except Exception:
        #     configuration_updated_at = None

        # details = device.get('details', [])
        # running_software_version = None
        # for detail in details:
        #     if detail.get('name') == 'Running software version':
        #         try:
        #             running_software_version = detail.get('value')
        #         except Exception:
        #             pass

        items.append({
            "name": device['serial'],  # str
            "serial": device['serial'],  # str
            "deviceName": device['name'],  # str
            "mac": device['mac'],  # str
            "networkId": device['networkId'],  # str
            "organizationId": org_id,
            # "productType": device['productType'],  # str
            # "model": device['model'],  # str
            # "address": device.get('address') or None,  # str?
            # "lat": device['lat'],  # float
            # "lng": device['lng'],  # float
            # "notes": device.get('notes') or None,  # str?
            # "lanIp": device['lanIp'],  # str
            # "configurationUpdatedAt": configuration_updated_at,  # int?
            # "firmware": device['firmware'],  # str
            # "running_software_version": running_software_version,  # str?
        })

    return {"devices": items}
