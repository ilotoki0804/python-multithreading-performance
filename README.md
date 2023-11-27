# python-multithreading-performance

Refer to [`performance-check-result.md`](performance-check-result.md) for comprehensive performance measurements.

## Summary

### Control Group

```
Python 3.12:
    elapsed time: 5.305475600005593
    cpu_percents mean: 0.57

Python 3.11:
    elapsed time: 5.2019462999887764
    cpu_percents mean: 1.7448979591836733
```

> Python 3.11 uses more CPU.

### Threadpool

```
Python 3.12:
    elapsed time: 63.789028299972415
    cpu_percents mean: 390.2005928853755

Python 3.11:
    elapsed time: 36.32241010002326
    cpu_percents mean: 11.792128279883382
```

> Python 3.12 is **1.76** times *slower* and uses **33.09** times more CPU.

### threading.Thread

```
Python 3.12:
    elapsed time: 85.85906719998457
    cpu_percents mean: 364.18723849372384

Python 3.11:
    elapsed time: 57.02882329997374
    cpu_percents mean: 13.909514925373134
```

> Python 3.12 is **1.51** times *slower* and uses **26.18** times more CPU.

### Threadpool (on Windows Sandbox)

```
Python 3.12:
    elapsed time: 77.19274369999994
    cpu_percents mean: 441.97548746518106

Python 3.11:
    elapsed time: 72.3070917
    cpu_percents mean: 3.6785511363636365
```

> Python 3.12 is **1.07** times *slower* and uses **120.15** times more CPU.
