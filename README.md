# Significant Performance Decline During the Download and Storage of Small Images in Python 3.12

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

> No Significant Difference

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
