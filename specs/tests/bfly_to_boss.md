Here's some pseudocode that shows how I would convert the part of the butterfly API to part of the BOSS API. Feel free to post here once a decison has been made for transforming the expermient, sample, dataset, and channel parameters.

* This will let you map from the [NDA SSD api/anatomy/data method](http://rc.hoff.in/SSD/System-Specification.pdf#page=8) to the BOSS API.

*From Butterfly (NDA SSD) API*
```
&x=0&y=0&z=0&width=512&height=512&resolution=1
```

*Make these changes*
```python
# Constant
BOSS.orientation = 'xy'

# The same resolution and z
BOSS.resolution = BFLY.resolution
BOSS.z_arg = BFLY.z

# Other arguments need scaling by resolution
BOSS.y_arg = '{}:{}'.format(BFLY.y, BFLY.y + BFLY.height*(2**BFLY.resolution))
BOSS.x_arg = '{}:{}'.format(BFLY.x, BFLY.x + BFLY.width*(2**BFLY.resolution))
```


*To Boss API*
```
orientation=xy&z_arg=0&x_arg=0:1024&y_arg=0:1024&resolution=1
```
