This converts the S2 of the NDA to the butterfly API.

### Requests

**From NDA (ICD) API**
```
https://<domain>/synapse_ids/<collection>/<experiment>/<channel>/
    ...<resolution>/<xstart>,<xstop>/<ystart>,<ystop>/<zstart>,<zstop>/
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/synapse_ids/a/b/c/
    ...1/512,1024/0,512/0,1/
```

**Make these changes**
```python

# The same <resolution> and <z> origin
BFLY.resolution = NDA.resolution
BFLY.z = NDA.zstart
# take <depth> from the difference
BFLY.depth = NDA.zstop - NDA.zstart

# Scale all by the resolution
scale = 2**BFLY.resolution

# Integer division for <x> and <y> origin
BFLY.y = NDA.ystart // scale
BFLY.x = NDA.xstart // scale
# Integer division of differences for <width> and <height>
BFLY.height = ( NDA.ystop - NDA.ystart ) // scale
BFLY.width = ( NDA.xstop - NDA.xstart ) // scale

# Just map the naming conventions
BFLY.experiment = NDA.collection
BFLY.sample = NDA.collection
BFLY.dataset = NDA.experiment
BFLY.channel = NDA.channel
```

**To Butterfly API**
```
https://<butterfly_domain>/synapse_ids?experiment=<collection>&sample=<collection>&dataset=<experiment>&channel=<channel>
    ...&resolution=<resolution>&x=<x>&y=<y>&z=<z>&width=<w>&height=<h>&depth=<d>
https://butterfly.rc.fas.harvard.edu/api/synapse_ids?experiment=a&sample=a&dataset=b&channel=c
    ...&resolution=1&x=256&y=0&z=0&width=256&height=256&depth=1
```

### Responses

**From Butterfly Response**
```
[
    14, 
    17
]
```

**To NDA (ICD Response**
```
{
    "ids": [14, 17]
}
```
