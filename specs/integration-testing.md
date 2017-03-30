Request for Evaluation - MICrONS Phase 1
*March 2017 Pretest - should be conducted by Friday 3/31/2017*

Description:  This test is primarily designed as an informal proof-of-life test for the NDA.  However, depending on the maturity of the data available for each team, additional testing will be conducted.  It is not a formal deliverable.

We envision that this document will evolve over the next few weeks and form the basis for the official circuit reconstruction submission.  Once the Phase data are delivered, the respective channels will be made "read only" to ensure data integrity for evaluation.

Note that we will test each of the services you've specified in your SSD.  After discussion with teams and internally, we DO require S2 and S6 to avoid underlying ambiguity.  S9 in now optional.


Questions:  Will Gray-Roncal (william.gray.roncal@jhuapl.edu)

Performer Information (required to test):

1.  Location of NDA services (URL)
	- aridne-nda.rc.fas.harvard.edu

2.  Boss collection/experiment/channel for the raw structural image data
	- integration-testing/2017-03-31/raw
		- /n/coxfs01/leek/results/ECS_aff_test_images/image.h5

3.  Boss collection/experiment/channel for the raw functional image data
	- integration-testing/2017-03-31/function_raw
		- /n/coxfs01/thejohnhoffer/data/ASCII.png

4.  Boss collection/experiment/channel for structural neuron information (automated)
	- a) integration-testing/2017-03-31/neuron_seg
		- /n/coxfs01/leek/results/ECS_aff_test_images/neuroproof.h5
	- b) Can IARPA assume that all labels in this channel are neurons for evaluation purposes?
		- all with overlapping synapses in integration-testing/2017-03-31/synapse_seg

5.  Boss collection/experiment/channel for structural synapse information (automated)
	- a) integration-testing/2017-03-31/synapse_seg
		- /n/coxfs01/leek/results/ECS_aff_test_images/synapse-segmentation.h5 
	- b) Can IARPA assume that all labels in this channel are synapses for evaluation purposes?
		- yes, all but id==0

6.  Boss collection/experiment/channel for the functional neuron information containing neuron cell body segmentation or ROIs.
	- integration-testing/2017-03-31/function_neuron
		- /n/coxfs01/thejohnhoffer/data/ASCII.png

7.  Location (x,y,z,resolution) of automated reconstruction bounding box (if not dense, please specify)
	- Dense: full volume

8.  Boss collection/experiment/channel for structural neuron information (ground truth)
	- a) integration-testing/2017-03-31/neuron_gt
		- /n/coxfs01/leek/results/ECS_aff_test_images/gt.h5
	- b) Can IARPA assume that all labels in this channel are neurons for evaluation purposes?
		- yes, all but id==0

9.  Boss collection/experiment/channel for structural synapse information (ground truth)
	- a) integration-testing/2017-03-31/synapse_gt
		- /n/coxfs01/leek/results/ECS_aff_test_images/synapse-gt.h5
	- b) Can IARPA assume that all labels in this channel are synapses for evaluation purposes?
		- yes, all but id==0

10.  Location (x,y,z,resolution) of ground truth bounding box (if not dense, please specify)
	- Dense: full volume

11.  Date(s) of preferred NDA testing.
	- any date after 2017-04-01

12.  Request submitted by (Name, email) - for final phase deliverable this should be performer team lead; for this testing can be any team member
	- The submitter of this document
