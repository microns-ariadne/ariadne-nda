hannel Metadata

- **ARIADNE-NDA Layer**
```
/api/anatomy/channel_metadata?experiment=root&sample=test&dataset=iarpa2016_12&channel=img
```
- **butterfly.rc.fas.harvard.edu** [(live url)](https://butterfly.rc.fas.harvard.edu/api/channel_metadata?experiment=root&sample=test&dataset=iarpa2016_12&channel=img)
```
/api/channel_metadata?experiment=root&sample=test&dataset=iarpa2016_12&channel=img
```
- **Response**
```json
{
	"path": "/n/coxfs01/thejohnhoffer/2016/iarpa2016_12/img",
	"data-type": "uint8",
	"dimensions": {
		"y": 2000,
	 	"x": 2000,
		"z": 1774
	},
	"name": "img"
}
```

## Data

- **ARIADNE-NDA Layer**
```
/api/anatomy/data?experiment=root&sample=test&dataset=iarpa2016_12&x=0&y=0&z=0&width=512&height=512&channel=img
```
- **butterfly.rc.fas.harvard.edu** [(live url)](https://butterfly.rc.fas.harvard.edu/api/data?experiment=root&sample=test&dataset=iarpa2016_12&x=0&y=0&z=0&width=512&height=512&channel=img)
```
/api/data?experiment=root&sample=test&dataset=iarpa2016_12&x=0&y=0&z=0&width=512&height=512&channel=img
```
- **Response Examples**

| `&channel=img` | `&channel=ids` | `&channel=ids&format=tif` |
|----------------|----------------|---------------------------|
| [Raw 8-bit PNG (live)](https://butterfly.rc.fas.harvard.edu/api/data?experiment=root&sample=test&dataset=iarpa2016_12&x=0&y=0&z=0&width=512&height=512&channel=img) | [human-viewable PNG (live)](https://butterfly.rc.fas.harvard.edu/api/data?experiment=root&sample=test&dataset=iarpa2016_12&x=0&y=0&z=0&width=512&height=512&channel=ids) | [32-bit grayscale TIFF (live)](https://butterfly.rc.fas.harvard.edu/api/data?experiment=root&sample=test&dataset=iarpa2016_12&x=0&y=0&z=0&width=512&height=512&channel=ids&format=tif) |
|![](http://img.hoff.in/nda/img0.png)|![](http://img.hoff.in/nda/ids0.png)|![32-bit grayscale .tiff](http://img.hoff.in/nda/ids1.png)|

## Channels

- **ARIADNE-NDA Layer**
```
/api/anatomy/channels?experiment=root&sample=test&dataset=iarpa2016_12
```
- **butterfly.rc.fas.harvard.edu** [(live url)](https://butterfly.rc.fas.harvard.edu/api/channels?experiment=root&sample=test&dataset=iarpa2016_12)
```
/api/channels?experiment=root&sample=test&dataset=iarpa2016_12
```
- **Response**
```json
["img", "ids"]
```

## Datasets

- **ARIADNE-NDA Layer**
```
/api/anatomy/datasets?experiment=root&sample=test
```
- **butterfly.rc.fas.harvard.edu** [(live url)](https://butterfly.rc.fas.harvard.edu/api/datasets?experiment=root&sample=test)
```
/api/datasets?experiment=root&sample=test
```
- **Response**
```json
["iarpa2016_12", "gt-2x2x2-seg", "gt-3x6x6", "gt-4x6x6", "gt-3x4x4-synapse"]
```

## Samples

- **ARIADNE-NDA Layer**
```
/api/anatomy/samples?experiment=root
```
- **butterfly.rc.fas.harvard.edu** [(live url)](https://butterfly.rc.fas.harvard.edu/api/samples?experiment=root)
```
/api/samples?experiment=root
```
- **Response**
```json
["test"]
```

## Experiments

- **ARIADNE-NDA Layer**
```
/api/anatomy/experiments
```
- **butterfly.rc.fas.harvard.edu** [(live url)](https://butterfly.rc.fas.harvard.edu/api/experiments)
```
/api/experiments
```
- **Response**
```json
["root"]
```

