import aiohttp
from libprobe.asset import Asset
from .connector import get_connector


async def query(
        asset: Asset,
        asset_config: dict,
        check_config: dict,
        req: str):
    api_key = asset_config.get('secret')
    assert api_key, (
        'API key is missing, '
        'please provide the API key as `secret` in the appliance config')

    headers = {
        'X-Cisco-Meraki-API-Key': api_key,
    }
    uri = f'https://api.meraki.com/api/v1{req}'

    async with aiohttp.ClientSession(connector=get_connector()) as session:
        async with session.get(uri, headers=headers, ssl=True) as resp:
            assert resp.status // 100 == 2, \
                f'response status code: {resp.status}; reason: {resp.reason}'

            data = await resp.json()
            return data
