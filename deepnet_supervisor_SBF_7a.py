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

# runs: 240

TASK_ID = int(sys.argv[1])


RUN = TASK_ID
os.system("nvidia-smi")
command = "python3 "          				+ 'deepnet_main.py' + \
		  " -experiment_name "  			+ 'SBF_7a' + \
		  " -spec_name "        			+ 'blend5_unrest' + \
		  " -run "              			+ str(RUN) + \
		  " -task="             			+ 'cifar10' + \
		  " -preprocessing="				+ 'ztrans' +\
		  " -network="          			+ 'smcnLin' + \
		  " -mode "             			+ 'training' + \
		  " -n_minibatches "    			+ '10000' + \
		  " -minibatch_size "   			+ '256' + \
		  " -dropout_keep_probs "   		+ '0.5' + \
		  " -dropout_keep_probs_inference "	+ '1.0' + \
		  " -optimizer "            		+ 'Adam' + \
		  " -lr "               			+ '0.001' + \
		  " -lr_step_ep "           		+ '0' + \
		  " -lr_step_multi "        		+ '1' + \
		  " -use_wd "        				+ 'False' + \
		  " -wd_lambda "        			+ '0.01' + \
		  " -training_schedule "			+ 'epochs' + \
		  " -create_val_set "				+ 'False' + \
		  " -val_set_fraction "				+ '0.0' + \
		  " -af_set "           			+ '5_blend5_swish' +\
		  " -af_weights_init "  			+ 'default' + \
		  " -blend_trainable "  			+ 'True' + \
		  " -blend_mode "       			+ 'unrestricted' + \
		  " -swish_beta_trainable " 		+ 'True'
subprocess.run(command, shell=True)










"""

################################################################################
if TASK_ID < 41:
	RUN = TASK_ID-0
	os.system("nvidia-smi")
	command = "python3 "          				+ 'deepnet_main.py' + \
			  " -experiment_name "  			+ 'SBF_7a' + \
			  " -spec_name "        			+ 'linu' + \
			  " -run "              			+ str(RUN) + \
			  " -task="             			+ 'cifar10' + \
			  " -preprocessing="				+ 'ztrans' +\
			  " -network="          			+ 'smcnLin' + \
			  " -mode "             			+ 'training' + \
			  " -n_minibatches "    			+ '10000' + \
			  " -minibatch_size "   			+ '256' + \
			  " -dropout_keep_probs "   		+ '0.5' + \
			  " -dropout_keep_probs_inference "	+ '1.0' + \
			  " -optimizer "            		+ 'Adam' + \
			  " -lr "               			+ '0.001' + \
			  " -lr_step_ep "           		+ '0' + \
			  " -lr_step_multi "        		+ '1' + \
			  " -use_wd "        				+ 'False' + \
			  " -wd_lambda "        			+ '0.01' + \
			  " -training_schedule "			+ 'epochs' + \
			  " -create_val_set "				+ 'False' + \
			  " -val_set_fraction "				+ '0.0' + \
			  " -af_set "           			+ '1_linu' +\
			  " -af_weights_init "  			+ 'default' + \
			  " -blend_trainable "  			+ 'False' + \
			  " -blend_mode "       			+ 'unrestricted' + \
			  " -swish_beta_trainable " 		+ 'False'
	subprocess.run(command, shell=True)

################################################################################
elif TASK_ID < 81:
	RUN = TASK_ID-40
	os.system("nvidia-smi")
	command = "python3 "          				+ 'deepnet_main.py' + \
			  " -experiment_name "  			+ 'SBF_7a' + \
			  " -spec_name "        			+ 'relu' + \
			  " -run "              			+ str(RUN) + \
			  " -task="             			+ 'cifar10' + \
			  " -preprocessing="				+ 'ztrans' +\
			  " -network="          			+ 'smcnLin' + \
			  " -mode "             			+ 'training' + \
			  " -n_minibatches "    			+ '10000' + \
			  " -minibatch_size "   			+ '256' + \
			  " -dropout_keep_probs "   		+ '0.5' + \
			  " -dropout_keep_probs_inference "	+ '1.0' + \
			  " -optimizer "            		+ 'Adam' + \
			  " -lr "               			+ '0.001' + \
			  " -lr_step_ep "           		+ '0' + \
			  " -lr_step_multi "        		+ '1' + \
			  " -use_wd "        				+ 'False' + \
			  " -wd_lambda "        			+ '0.01' + \
			  " -training_schedule "			+ 'epochs' + \
			  " -create_val_set "				+ 'False' + \
			  " -val_set_fraction "				+ '0.0' + \
			  " -af_set "           			+ '1_relu' +\
			  " -af_weights_init "  			+ 'default' + \
			  " -blend_trainable "  			+ 'False' + \
			  " -blend_mode "       			+ 'unrestricted' + \
			  " -swish_beta_trainable " 		+ 'False'
	subprocess.run(command, shell=True)

################################################################################
elif TASK_ID < 121:
	RUN = TASK_ID-80
	os.system("nvidia-smi")
	command = "python3 "          				+ 'deepnet_main.py' + \
			  " -experiment_name "  			+ 'SBF_7a' + \
			  " -spec_name "        			+ 'elu' + \
			  " -run "              			+ str(RUN) + \
			  " -task="             			+ 'cifar10' + \
			  " -preprocessing="				+ 'ztrans' +\
			  " -network="          			+ 'smcnLin' + \
			  " -mode "             			+ 'training' + \
			  " -n_minibatches "    			+ '10000' + \
			  " -minibatch_size "   			+ '256' + \
			  " -dropout_keep_probs "   		+ '0.5' + \
			  " -dropout_keep_probs_inference "	+ '1.0' + \
			  " -optimizer "            		+ 'Adam' + \
			  " -lr "               			+ '0.001' + \
			  " -lr_step_ep "           		+ '0' + \
			  " -lr_step_multi "        		+ '1' + \
			  " -use_wd "        				+ 'False' + \
			  " -wd_lambda "        			+ '0.01' + \
			  " -training_schedule "			+ 'epochs' + \
			  " -create_val_set "				+ 'False' + \
			  " -val_set_fraction "				+ '0.0' + \
			  " -af_set "           			+ '1_jelu' +\
			  " -af_weights_init "  			+ 'default' + \
			  " -blend_trainable "  			+ 'False' + \
			  " -blend_mode "       			+ 'unrestricted' + \
			  " -swish_beta_trainable " 		+ 'False'
	subprocess.run(command, shell=True)

################################################################################
elif TASK_ID < 161:
	RUN = TASK_ID-120
	os.system("nvidia-smi")
	command = "python3 "          				+ 'deepnet_main.py' + \
			  " -experiment_name "  			+ 'SBF_7a' + \
			  " -spec_name "        			+ 'adaptive_linu' + \
			  " -run "              			+ str(RUN) + \
			  " -task="             			+ 'cifar10' + \
			  " -preprocessing="				+ 'ztrans' +\
			  " -network="          			+ 'smcnLin' + \
			  " -mode "             			+ 'training' + \
			  " -n_minibatches "    			+ '10000' + \
			  " -minibatch_size "   			+ '256' + \
			  " -dropout_keep_probs "   		+ '0.5' + \
			  " -dropout_keep_probs_inference "	+ '1.0' + \
			  " -optimizer "            		+ 'Adam' + \
			  " -lr "               			+ '0.001' + \
			  " -lr_step_ep "           		+ '0' + \
			  " -lr_step_multi "        		+ '1' + \
			  " -use_wd "        				+ 'False' + \
			  " -wd_lambda "        			+ '0.01' + \
			  " -training_schedule "			+ 'epochs' + \
			  " -create_val_set "				+ 'False' + \
			  " -val_set_fraction "				+ '0.0' + \
			  " -af_set "           			+ '1_linu' +\
			  " -af_weights_init "  			+ 'default' + \
			  " -blend_trainable "  			+ 'True' + \
			  " -blend_mode "       			+ 'unrestricted' + \
			  " -swish_beta_trainable " 		+ 'False'
	subprocess.run(command, shell=True)


################################################################################
elif TASK_ID < 201:
	RUN = TASK_ID-160
	os.system("nvidia-smi")
	command = "python3 "          				+ 'deepnet_main.py' + \
			  " -experiment_name "  			+ 'SBF_7a' + \
			  " -spec_name "        			+ 'adaptive_relu' + \
			  " -run "              			+ str(RUN) + \
			  " -task="             			+ 'cifar10' + \
			  " -preprocessing="				+ 'ztrans' +\
			  " -network="          			+ 'smcnLin' + \
			  " -mode "             			+ 'training' + \
			  " -n_minibatches "    			+ '10000' + \
			  " -minibatch_size "   			+ '256' + \
			  " -dropout_keep_probs "   		+ '0.5' + \
			  " -dropout_keep_probs_inference "	+ '1.0' + \
			  " -optimizer "            		+ 'Adam' + \
			  " -lr "               			+ '0.001' + \
			  " -lr_step_ep "           		+ '0' + \
			  " -lr_step_multi "        		+ '1' + \
			  " -use_wd "        				+ 'False' + \
			  " -wd_lambda "        			+ '0.01' + \
			  " -training_schedule "			+ 'epochs' + \
			  " -create_val_set "				+ 'False' + \
			  " -val_set_fraction "				+ '0.0' + \
			  " -af_set "           			+ '1_relu' +\
			  " -af_weights_init "  			+ 'default' + \
			  " -blend_trainable "  			+ 'True' + \
			  " -blend_mode "       			+ 'unrestricted' + \
			  " -swish_beta_trainable " 		+ 'False'
	subprocess.run(command, shell=True)

################################################################################
elif TASK_ID < 241:
	RUN = TASK_ID-200
	os.system("nvidia-smi")
	command = "python3 "          				+ 'deepnet_main.py' + \
			  " -experiment_name "  			+ 'SBF_7a' + \
			  " -spec_name "        			+ 'adaptive_elu' + \
			  " -run "              			+ str(RUN) + \
			  " -task="             			+ 'cifar10' + \
			  " -preprocessing="				+ 'ztrans' +\
			  " -network="          			+ 'smcnLin' + \
			  " -mode "             			+ 'training' + \
			  " -n_minibatches "    			+ '10000' + \
			  " -minibatch_size "   			+ '256' + \
			  " -dropout_keep_probs "   		+ '0.5' + \
			  " -dropout_keep_probs_inference "	+ '1.0' + \
			  " -optimizer "            		+ 'Adam' + \
			  " -lr "               			+ '0.001' + \
			  " -lr_step_ep "           		+ '0' + \
			  " -lr_step_multi "        		+ '1' + \
			  " -use_wd "        				+ 'False' + \
			  " -wd_lambda "        			+ '0.01' + \
			  " -training_schedule "			+ 'epochs' + \
			  " -create_val_set "				+ 'False' + \
			  " -val_set_fraction "				+ '0.0' + \
			  " -af_set "           			+ '1_jelu' +\
			  " -af_weights_init "  			+ 'default' + \
			  " -blend_trainable "  			+ 'True' + \
			  " -blend_mode "       			+ 'unrestricted' + \
			  " -swish_beta_trainable " 		+ 'False'
	subprocess.run(command, shell=True)

################################################################################
elif TASK_ID < 281:
	RUN = TASK_ID-240
	os.system("nvidia-smi")
	command = "python3 "          				+ 'deepnet_main.py' + \
			  " -experiment_name "  			+ 'SBF_7a' + \
			  " -spec_name "        			+ 'blend5_unrest' + \
			  " -run "              			+ str(RUN) + \
			  " -task="             			+ 'cifar10' + \
			  " -preprocessing="				+ 'ztrans' +\
			  " -network="          			+ 'smcnLin' + \
			  " -mode "             			+ 'training' + \
			  " -n_minibatches "    			+ '10000' + \
			  " -minibatch_size "   			+ '256' + \
			  " -dropout_keep_probs "   		+ '0.5' + \
			  " -dropout_keep_probs_inference "	+ '1.0' + \
			  " -optimizer "            		+ 'Adam' + \
			  " -lr "               			+ '0.001' + \
			  " -lr_step_ep "           		+ '0' + \
			  " -lr_step_multi "        		+ '1' + \
			  " -use_wd "        				+ 'False' + \
			  " -wd_lambda "        			+ '0.01' + \
			  " -training_schedule "			+ 'epochs' + \
			  " -create_val_set "				+ 'False' + \
			  " -val_set_fraction "				+ '0.0' + \
			  " -af_set "           			+ '5_blend5_swish' +\
			  " -af_weights_init "  			+ 'default' + \
			  " -blend_trainable "  			+ 'True' + \
			  " -blend_mode "       			+ 'unrestricted' + \
			  " -swish_beta_trainable " 		+ 'True'
	subprocess.run(command, shell=True)
"""
