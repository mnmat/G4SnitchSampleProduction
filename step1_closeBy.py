# Last update with 12_0_1_pre4
# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: CloseByParticle_Photon_ERZRanges_cfi --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent FEVTDEBUG --relval 9000,100 -s GEN,SIM --datatier GEN-SIM --beamspot HLLHC --geometry Extended2026D49 --no_exec --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

import sys, os, errno

en_str = sys.argv[1]
eta_str = sys.argv[2]
nameprefix = sys.argv[3]
nevents = sys.argv[4]
caps = sys.argv[5]
folder = sys.argv[6]
nthreads = int(sys.argv[7])
idx = str(sys.argv[8])
print(caps,folder,nthreads,idx)
seed = int(sys.argv[9])
seed = 1

# Set variables for particle gun
en = float(en_str)
en_min = float(en-0.01)
en_max = float(en+0.01)

if "pi" in nameprefix :
  part_id = 211
elif "el" in nameprefix :
  part_id = 11
elif "mu" in nameprefix :
  part_id = 13
elif "ka" in nameprefix :
  part_id = 321
else:
  print('no part id valid')
  sys.exit()

if "_" in eta_str: # in case we want to specify an eta range, i.e. 1.7_2.7
    eta_min = float(eta_str.split("_")[0])
    eta_max = float(eta_str.split("_")[1])
else:
    eta = float(eta_str)
    eta_min = eta - 0.00001
    eta_max = eta + 0.00001

if caps == "neg":
    eta_min = - eta_min
    eta_max = - eta_max
elif caps!="pos":
    raise Exception('%s is an invalid keyword argument for the z position. Should be either "pos" or "neg".'%caps)


eta_str = eta_str.replace(".","")
outfolder = folder + '/step1/'
if not os.path.exists(outfolder):
   try:
      os.makedirs(outfolder)
   except OSError as e:
      if e.errno != errno.EEXIST:
         raise
   #os.makedirs(outfolder, exist_ok=True) # only in Python 3
outfile_  = "file:{}/step1_{}_e{}GeV_eta{}_z{}_events{}_nopu_{}.root".format(outfolder, nameprefix, en_str, eta_str,caps,nevents,idx)


from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9

process = cms.Process('SIM',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D110Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D110_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedHLLHC14TeV_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(int(nevents)),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('CloseByParticle_Photon_ERZRanges_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:%s'%(outfile_)),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T33', '')

process.generator = cms.EDProducer("CloseByParticleGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        ControlledByEta = cms.bool(False),
        Delta = cms.double(10),
        VarMin = cms.double(en_max),
        VarMax = cms.double(en_min),
        MaxVarSpread = cms.bool(False),
        MaxEta = cms.double(eta_max),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(eta_min),
        MinPhi = cms.double(-3.14159265359),
        NParticles = cms.int32(1),
        Overlapping = cms.bool(False),
        PartID = cms.vint32(int(part_id)),
        Pointing = cms.bool(True),
        RMax = cms.double(135.01), #HGC min = 60.
        RMin = cms.double(134.99), #HGC max = 120
        RandomShoot = cms.bool(False),
        ZMax = cms.double(321.01), #HGC max = 650
        ZMin = cms.double(320.99) #HGC min = 320
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('random particles in phi and r windows')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)
process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(seed)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

g4SnitchFile_  = "file:{}/g4Snitch_{}_e{}GeV_eta{}_z{}_events{}_nopu_{}.root".format(outfolder, nameprefix, en_str, eta_str,caps,nevents,idx)
#process.TFileService = cms.Service("TFileService", 
#    fileName = cms.string(g4SnitchFile_),
#    closeFileFast = cms.untracked.bool(True)
#    )

process.g4SimHits.Watchers = cms.VPSet(cms.PSet(
    type = cms.string('G4Snitch'),
    verbose = cms.untracked.bool(False),
    verbose_stack_level = cms.untracked.bool(False),
    verbose_transport = cms.untracked.bool(False),
    verbose_skip = cms.untracked.bool(False),
    verbose_skip_with_ids = cms.untracked.bool(False),
    verbose_fname = cms.untracked.string(g4SnitchFile_)
    ))


# Bug relating to CMSSW_14_0_X where it doesn't overwrite existing root files when using htcondor 
process.add_(cms.Service("AdaptorConfig", native=cms.untracked.vstring("root")))
