class MyError(Exception):
    ...
class OtherError(Exception):
    ...  
 
def launch():
    exception_ = MyError('a', 'b', 'c')
    raise exception_

try:
    launch()
except (MyError, ZeroDivisionError) as e:
    print(e.args)
    print()
    exception_ = OtherError('Something went wrong again')
    exception_.add_note('This is a note test')
    raise exception_ from e