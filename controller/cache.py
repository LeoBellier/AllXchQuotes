import asyncio

from aiocache import caches, Cache
from aiocache.serializers import StringSerializer, PickleSerializer

from ..apis.api_gate import get_list_cotizacion

caches.set_config({
    'default': {
        'cache': "aiocache,SimpleMemoryCache",
        'serializer': {
            'class' : "aiocache.serializers.StringSerializer"
        }
    },
    'redis_alt':{
        'cache': "aiocache.RedisCache",
        'endpoint': "127.0.0.1",
        'port': 6379,
        'timeout': 1,
        'serializer':{
            'class': "aiocache.serializers.PickeSerializer"
        }, 'plugins': [
            {'class':"aiocache.plugins.HitMissRatioPlugin"},
            {'class': "aiocache.plugins.TimingPlugin"}
        ]
    }
})

async def create_key():
    cache = caches.create(**caches.get_alias_config('redis_alt'))
    key:str
    value = []
    for i in get_list_cotizacion:
        value.append(i)
    cache = caches.get('default')
    await cache.set(key, value)

async def default_cache():
    cache = caches.get('default')
    await cache.set("key", "value")

async def alt_cache():
    cache = caches.create(**caches.get_alias_config('redis_alt'))

    await cache.set("key", "value")

    assert await cache.get('key') == "value"
    await cache.close() 

def test_alias():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(default_cache())
    loop.run_until_complete(alt_cache)

    cache = Cache(Cache.REDIS)
    loop.run_until_complete(default_cache())
    loop.run_until_complete(cache.close())

    loop.run_until_complete(caches.get('default').close())

if __name__ == "__main__":
    await create_key()

