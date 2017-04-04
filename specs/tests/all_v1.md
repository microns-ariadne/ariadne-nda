## Sparse

### S1: is_synapse

**Request**

- id = 14


```
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/is_synapse/integration_testing/2017_03_31/raw/14
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=is_synapse&id=14&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
```

**Response:**

```
true
```

### S3: synapse_keypoint

**Request**

- id = 14

```
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/synapse_keypoint/integration_testing/2017_03_31/raw/0/14
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=synapse_keypoint&id=14&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
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
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/synapse_parent/integration_testing/2017_03_31/raw/14
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=synapse_parent&id=14&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
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
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/is_neuron/integration_testing/2017_03_31/raw/18
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=is_neuron&id=18&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
```

**Response:**

```
true
```

### S7: neuron_keypoint

**Request**

- id = 18

```
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/neuron_keypoint/integration_testing/2017_03_31/raw/0/18
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=neuron_keypoint&id=18&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
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
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/neuron_children/integration_testing/2017_03_31/raw/18
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=neuron_children&id=18&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
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
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/synapse_ids/integration_testing/2017_03_31/raw/0/0,512/0,521/0,100/
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=synapse_ids&x=0&y=0&z=0&width=512&height=512&depth=100&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
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
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/neuron_ids/integration_testing/2017_03_31/raw/0/0,512/0,521/0,100/
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=neuron_ids&x=0&y=0&z=0&width=512&height=512&depth=100&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
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
https://ariadne-nda.rc.fas.harvard.edu/api/v0.1/synapse_parent/integration_testing/2017_03_31/raw/0/0,512/0,521/0,100/
```

```
http://butterfly.rc.fas.harvard.edu/api/entity_feature?feature=voxel_list&x=0&y=0&z=0&width=512&height=512&depth=100&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
```

**Response:**

```
[
    "Voxel List not Supported yet"
]
```
&experiment=integration_testing&sample=integration_testing&dataset=2017_03_31&channel=raw
