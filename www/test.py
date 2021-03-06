import orm
import asyncio, logging
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop,user='root', password='password', database='awesome')

    u = User(name='Test3', email='test3@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()