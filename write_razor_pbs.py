#! /usr/bin/env python3 

# this script generats a PBS file for the AHPC Razor cluster 

# define some variables


job_name = 'saja_test'
queue = 'tiny16core'
prefix = job_name 
num_nodes = 1  # number of nodes
num_proc = 1  # number of processors
walltime = 1

# this section prints the header/required info for the PBS script

print('#PBS -N %s' % job_name) # job_name
print('#PBS -q %s' % queue) # which queue to use
print('#PBS -j oe' ) # join the STDOUT and STDERR into a single file
print('#PBS -o %s.$PBS_JOBID' % prefix)
print('#PBS -l nodes=%d:ppn=%d' %(num_nodes, num_proc))
print('#PBS -l walltime=%d:00:00' %walltime)
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

modules = ['gcc/7.2.1', 'python/3.6.0-anaconda']
# load the necessary modules
print('# load modules')
print('module purge')
for m in modules:
    print('module load %s' % m )
print()

commands = ['echo HELLO']
# commands for this job
print('# insert commands here')
for c in commands:
    print(c)

