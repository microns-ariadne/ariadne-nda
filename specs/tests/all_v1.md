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
{
  "result": true
}
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
  "keypoint": [
    351,
    118,
    57
  ]
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
  "parent_neurons": {
    "5445": 2,
    "18": 1
  }
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
{
  "result": true
}
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
  "keypoint": [
    351,
    118,
    57
  ]
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
  "child_synapses": {
    "14": 2
  }
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
{
  "ids": [
    "14",
    "17"
  ]
}
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
{
  "ids": [
    "18",
    "6487",
    "5445"
  ]
}
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
{
  "x": [],
  "y": [],
  "z": []
}
```
