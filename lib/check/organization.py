from typing import Any
from libprobe.asset import Asset
from ..query import query


async def check_organization(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict[str, list[dict[str, Any]]]:

    org_id = config.get('id')
    if not org_id:
        raise Exception(
            'Missing organization ID in asset collector configuration')

    req = f'/organizations/{org_id}'
    resp = await query(asset, asset_config, asset_config, req)

    licensing_model = resp.get('licensing', {}).get('model')
    cloud_region = resp.get('cloud', {}).get('region', {}).get('name')
    management_details = resp.get('management', {}).get('details', [])

    try:
        api_enabled = resp['api']['enabled']
    except KeyError:
        raise Exception('Api Enabled missing in organization data')

    management_customer_number = None
    for detail in management_details:
        if detail.get('name') == 'customer number':
            try:
                management_customer_number = int(detail.get('value'))
            except Exception:
                pass

    item = {
        "name": resp["id"],  # str
        "id": resp["id"],  # str  (same as name)
        "url": resp["url"],  # str
        "apiEnabled": api_enabled,  # bool
        "organizationName": resp["name"],  # str
        "licensingModel": licensing_model,  # str?
        "cloudRegion": cloud_region,  # str?
        "managementCustomerNumber": management_customer_number,  # int?
    }

    return {"organization": [item]}
