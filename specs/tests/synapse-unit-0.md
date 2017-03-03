# Unit test #0

- **Start with this on Butterfly**
```
{
  neuron1: [   0,   0,   0,   0,   5,   5,   5,   5],
  neuron2: [   1,   2,   3,   4,   6,   7,   8,   0],
  x:       [   0,   0,   0,   0, 512, 512, 512, 512],
  y:       [ 256, 512,1024,2048, 256, 512,1024,2048],
  z:       [ 256,   0,2048, 512, 256,   0,2048, 512]
}
```
- **Start with query**
```
{
  x: 0,
  y: 0,
  z: 0,
  width: 1040,
  height: 1040,
  depth: 1040
}
```
- **Request 0**
```
/api/anatomy/entity_feature?feature=synapse_ids&x=0&y=0&z=0&width=1040&height=1040&depth=1040&experiment=root&sample=test&dataset=iarpa2016_12&channel=synapse-neuroglancer
```
- **Response 0**
```
['s0','s1','s4','s5']
```
- **Request 1 Example for id=s5**
```
/api/anatomy/entity_feature?feature=synapse_parent&id=s5&experiment=root&sample=test&dataset=iarpa2016_12&channel=synapse-neuroglancer
```
- **Response 1 Example**
```
{
  synapse_id = 's5',
  synapse_parent_pre= 'n5',
  synapse_parent_post= 'n7'
}
```
