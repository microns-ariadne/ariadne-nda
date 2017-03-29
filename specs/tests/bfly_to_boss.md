Here's some pseudocode that shows how I would convert the part of the butterfly API to part of the BOSS API. Feel free to post here once a decison has been made for transforming the expermient, sample, dataset, and channel parameters.

* This will let you map from the [NDA SSD api/anatomy/data method](http://rc.hoff.in/SSD/System-Specification.pdf#page=8) to the BOSS API.

*From Butterfly (NDA SSD) API*
```
&x=0&y=0&z=0&width=512&height=512&resolution=1
```

*Make these changes*
```python
# Constant orientation
BOSS.orientation = 'xy'

# The same resolution and z origin
BOSS.resolution = BFLY.resolution
BOSS.z_arg = BFLY.z

# Scale by the resolution
scale = 2**BFLY.resolution

# Full resolution y_0, x_0, y_1, and x_1 bounds
y_0 = scale * BFLY.y
x_0 = scale * BFLY.x
y_1 = y_0 + scale * BFLY.height
x_1 = x_0 + scale * BFLY.width

# Format the full resolution bounds as boss arguments
BOSS.y_arg = '{}:{}'.format(y_0, y_1)
BOSS.x_arg = '{}:{}'.format(x_0, x_1)
```


*To Boss API*
```
orientation=xy&z_arg=0&x_arg=0:1024&y_arg=0:1024&resolution=1
```
