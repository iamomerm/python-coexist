## <ins> Parallel Context Manager </ins>

Run multiple code statements concurrently using a simple and Pythonic context manager <br>

### <ins> Features </ins>
- Execute multiple tasks in parallel with threads <br>
- Simple with statement interface for easy use <br>
- Collect tasks via lambdas or callable functions <br>
- Configurable number of worker threads <br>
- Waits for all tasks to complete before exiting the context <br>

### <ins> Installation </ins>
You can install this package via PIP: pip install python-parallel

### <ins> Usage </ins>

```python
from parallel import parallel

with parallel(max_workers=5) as pl:
    pl(lambda: print('Hello'))
    pl(lambda: print('World'))
```
