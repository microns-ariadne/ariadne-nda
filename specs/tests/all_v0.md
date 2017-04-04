## Sparse

### S1: is_synapse

**Request**

- id = 14

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=is_synapse&id=14&experiment=a&sample=b&dataset=c&channel=d
```

**Response:**

```
true
```

### S3: synapse_keypoint

**Request**

- id = 14

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=synapse_keypoint&id=14&experiment=a&sample=b&dataset=c&channel=d
```

**Response:**

```
{
    "y": 118, 
    "x": 351, 
    "z": 57
}
```

### S4: synapse_parent

**Request**

- id = 14

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=synapse_parent&id=14&experiment=a&sample=b&dataset=c&channel=d&x=0&y=0&z=0&width=512&height=512&depth=100
```

**Response:**

```
{
    "synapse_parent_pre": 18, 
    "synapse_id": 14, 
    "synapse_parent_post": 5445
}
```

*****


### S5: is_neuron

**Request**

- id = 18

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=is_neuron&id=18&experiment=a&sample=b&dataset=c&channel=d
```

**Response:**

```
true
```

### S7: neuron_keypoint

**Request**

- id = 18

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=neuron_keypoint&id=18&experiment=a&sample=b&dataset=c&channel=d
```

**Response:**

```
{
    "y": 118, 
    "x": 351, 
    "z": 57
}
```

### S8: neuron_children

**Request**

- id = 18

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=neuron_children&id=18&experiment=a&sample=b&dataset=c&channel=d
```

**Response:**

```
{
    "14": 2
}
```

## Dense

### S2: synapse_ids

**Request**

- x,y,z = 0,0,0
- width,height,depth = 512,512,100

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=synapse_ids&experiment=a&sample=b&dataset=c&channel=d&x=0&y=0&z=0&width=512&height=512&depth=100
```

**Response:**

```
[
    14, 
    17
]
```

### S6: neuron_ids

**Request**

- x,y,z = 0,0,0
- width,height,depth = 512,512,100

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=neuron_ids&experiment=a&sample=b&dataset=c&channel=d&x=0&y=0&z=0&width=512&height=512&depth=100
```

**Response:**

```
[
    18, 
    6487, 
    5445
]
```

### S9: voxel_list

**Request**

- id = 0
- x,y,z = 0,0,0
- width,height,depth = 512,512,100

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=voxel_list&id=0&experiment=a&sample=b&dataset=c&channel=d&x=0&y=0&z=0&width=512&height=512&depth=100
```

**Response:**

```
[
    "Voxel List not Supported yet"
]
```
