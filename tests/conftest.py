from app import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

# iter = Coord(self.coord.x, self.coord.y)
#             iter.iterate_up()
#             iter.iterate_up()
#             if iter.iterate_right():
#                 if iter == move:
#                     return True
#             iter.x, iter.y = (self.coord.x, self.coord.y)
#             iter.iterate_up()
#             iter.iterate_up()
#             if iter.iterate_left():
#                 if iter == move:
#                     return True
#             iter.x, iter.y = (self.coord.x, self.coord.y)
#             iter.iterate_down()
#             iter.iterate_down()
#             if iter.iterate_right():
#                 if iter == move:
#                     return True
#             iter.x, iter.y = (self.coord.x, self.coord.y)
#             iter.iterate_down()
#             iter.iterate_down()
#             if iter.iterate_left():
#                 if iter == move:
#                     return True
#             iter.x, iter.y = (self.coord.x, self.coord.y)
#             iter.iterate_right()
#             iter.iterate_right()
#             if iter.iterate_up():
#                 if iter == move:
#                     return True
#             iter.x, iter.y = (self.coord.x, self.coord.y)
#             iter.iterate_right()
#             iter.iterate_right()
#             if iter.iterate_down():
#                 if iter == move:
#                     return True
#             iter.x, iter.y = (self.coord.x, self.coord.y)
#             iter.iterate_left()
#             iter.iterate_left()
#             if iter.iterate_up():
#                 if iter == move:
#                     return True
#             iter.x, iter.y = (self.coord.x, self.coord.y)
#             iter.iterate_left()
#             iter.iterate_left()
#             if iter.iterate_down():
#                 if iter == move:
#                     return True
