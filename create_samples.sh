#! /bin/bash

folderin='/eos/cms/store/group/dpg_hgcal/comm_hgcal/mmatthew/G4Snitch/debug'
folderout='/eos/cms/store/group/dpg_hgcal/comm_hgcal/mmatthew/G4Snitch/debug'


eta="$1"
en="$2"
nevents="$3"
idx="$4"
step="$5"
mode="$6"
nthreads="1"
particle="singlemuon"

if [ "$mode" != "" ]
then
    python3 run_singlestep.py --folderin $folderin --folderout $folderout --sample $particle --energies $en --etas $eta --nevents $nevents --caps pos --nthreads $nthreads --idx $idx --step $step --mode $mode 
else
    python3 run_singlestep.py --folderin $folderin --folderout $folderout --sample $particle --energies $en --etas $eta --nevents $nevents --caps pos --nthreads $nthreads --idx $idx --step $step
fi

