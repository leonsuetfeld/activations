"""
Script to manage the schedule / experiments. Controls repetitive script calls
and paricular parameter settings.

@authors: Leon Sütfeld, Flemming Brieger
"""

import time
import os
import sys
import subprocess

"""
################################################################################
### RULES TO CONSTRUCT "AF_SET" ################################################
################################################################################

- must start with the number of AFs, then "_", then the set name
- must contain "swish" if swish AF is used at all
- must contain "scaled" if the scaled version of the respective AF(s) is to be used
- set name is the AFs name (in lowercase) or the name of the AF blend set, e.g., "blendSF7" or "blend9_swish"
- "elu" is called "jelu" ("just elu") to differentiate it from relu and selu
- "lu" (linear unit) is called "linu" for the same reason
- "swish" alone is called "jswish" ("just swish")
- [EXAMPLE] af_set='1_relu'
- [EXAMPLE] af_set='1_jswish'
- [EXAMPLE] af_set='1_scaled_jelu'
- [EXAMPLE] af_set='9_blend9_siwsh_scaled'

################################################################################
################################################################################
################################################################################
"""

################################################################################

# TASK_ID = int(sys.argv[1])

for TASK_ID in range(10):

	################################################################################
	if TASK_ID < 6:
		RUN = TASK_ID-0
		os.system("nvidia-smi")
		command = "python3 "          				+ 'deepnet_main.py' + \
				  " -experiment_name "  			+ 'debugging' + \
				  " -spec_name "        			+ 'allcnnc_cifar10_relu' + \
				  " -run "              			+ str(RUN) + \
				  " -task "             			+ 'cifar10' + \
				  " -network "          			+ 'allcnnc' + \
				  " -mode "             			+ 'training' + \
				  " -n_minibatches "    			+ '70000' + \
				  " -minibatch_size "   			+ '256' + \
				  " -dropout_keep_probs "   		+ '0.8 0.5 0.5' + \
				  " -dropout_keep_probs_inference "	+ '1.0 1.0 1.0' + \
				  " -optimizer "            		+ 'Momentum' + \
				  " -lr "               			+ '0.01' + \
				  " -lr_step_ep "           		+ '200 250 300' + \
				  " -lr_step_multi "        		+ '0.1 0.01 0.001' + \
				  " -use_wd "        				+ 'True' + \
				  " -wd_lambda "        			+ '0.01' + \
				  " -training_schedule "			+ 'epochs' + \
				  " -create_val_set "				+ 'True' + \
				  " -val_set_fraction "				+ '0.05' + \
				  " -af_set "           			+ '1_relu' +\
				  " -af_weights_init "  			+ 'default' + \
				  " -blend_trainable "  			+ 'True' + \
				  " -blend_mode "       			+ 'unrestricted' + \
				  " -swish_beta_trainable " 		+ 'True'
		subprocess.run(command, shell=True)

	################################################################################
	elif TASK_ID < 11:
		RUN = TASK_ID-5
		os.system("nvidia-smi")
		command = "python3 "          				+ 'deepnet_main.py' + \
				  " -experiment_name "  			+ 'debugging' + \
				  " -spec_name "        			+ 'allcnnc_cifar10_jelu' + \
				  " -run "              			+ str(RUN) + \
				  " -task "             			+ 'cifar10' + \
				  " -network "          			+ 'allcnnc' + \
				  " -mode "             			+ 'training' + \
				  " -n_minibatches "    			+ '70000' + \
				  " -minibatch_size "   			+ '256' + \
				  " -dropout_keep_probs "   		+ '0.8 0.5 0.5' + \
				  " -dropout_keep_probs_inference "	+ '1.0 1.0 1.0' + \
				  " -optimizer "            		+ 'Momentum' + \
				  " -lr "               			+ '0.01' + \
				  " -lr_step_ep "           		+ '200 250 300' + \
				  " -lr_step_multi "        		+ '0.1 0.01 0.001' + \
				  " -use_wd "        				+ 'True' + \
				  " -wd_lambda "        			+ '0.01' + \
				  " -training_schedule "			+ 'epochs' + \
				  " -create_val_set "				+ 'True' + \
				  " -val_set_fraction "				+ '0.05' + \
				  " -af_set "           			+ '1_jelu' +\
				  " -af_weights_init "  			+ 'default' + \
				  " -blend_trainable "  			+ 'True' + \
				  " -blend_mode "       			+ 'unrestricted' + \
				  " -swish_beta_trainable " 		+ 'True'
		subprocess.run(command, shell=True)