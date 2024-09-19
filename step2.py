# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 -s DIGI:pdigi_valid,L1TrackTrigger,L1,DIGI2RAW,HLT:@relval2026 --conditions auto:phase2_realistic_T33 --datatier GEN-SIM-DIGI-RAW -n 10 --eventcontent FEVTDEBUGHLT --geometry Extended2026D110 --era Phase2C17I13M9 --filein file:step1.root --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

en_str = sys.argv[1]
eta_str = sys.argv[2].replace(".","")
nameprefix = sys.argv[3]
nevents = sys.argv[4]
caps = sys.argv[5]
infolder = sys.argv[6]
nthreads = int(sys.argv[8])
idx = str(sys.argv[9])

# Define input and output files
if idx != "none":
    infile_  = "file:{}/step1/step1_{}_e{}GeV_eta{}_z{}_events{}_nopu_{}.root".format(infolder, nameprefix, en_str, eta_str,caps,nevents,idx)
else:
    infile_  = "file:{}/step1/step1_{}_e{}GeV_eta{}_z{}_events{}_nopu.root".format(infolder, nameprefix, en_str, eta_str,caps,nevents)

outfolder = sys.argv[7]
print("Outfolder: ", outfolder)
outfolder = outfolder + '/step2/'

if not os.path.exists(outfolder):
   try:
      os.makedirs(outfolder)
   except OSError as e:
      if e.errno != errno.EEXIST:
         raise
   #os.makedirs(outfolder, exist_ok=True) # only in Python 3
if idx != "-1":
    outfile_  = "file:{}/step2_{}_e{}GeV_eta{}_z{}_events{}_nopu_{}.root".format(outfolder, nameprefix, en_str, eta_str,caps,nevents,idx)
else:
    outfile_  = "file:{}/step2_{}_e{}GeV_eta{}_z{}_events{}_nopu.root".format(outfolder, nameprefix, en_str, eta_str,caps,nevents)


from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9

process = cms.Process('HLT',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D110Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.SimPhase2L1GlobalTriggerEmulator_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.prototypeSeeds')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_75e33_cff')
#process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(int(nevents)),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(infile_),
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_genParticles_*_*',
        'drop *_genParticlesForJets_*_*',
        'drop *_kt4GenJets_*_*',
        'drop *_kt6GenJets_*_*',
        'drop *_iterativeCone5GenJets_*_*',
        'drop *_ak4GenJets_*_*',
        'drop *_ak7GenJets_*_*',
        'drop *_ak8GenJets_*_*',
        'drop *_ak4GenJetsNoNu_*_*',
        'drop *_ak8GenJetsNoNu_*_*',
        'drop *_genCandidatesForMET_*_*',
        'drop *_genParticlesForMETAllVisible_*_*',
        'drop *_genMetCalo_*_*',
        'drop *_genMetCaloAndNonPrompt_*_*',
        'drop *_genMetTrue_*_*',
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

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
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(outfile_),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T33', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1TrackTrigger_step = cms.Path(process.L1TrackTrigger)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.Phase2L1GTProducer = cms.Path(process.l1tGTProducerSequence)
process.Phase2L1GTAlgoBlockProducer = cms.Path(process.l1tGTAlgoBlockProducerSequence)
process.pDoubleEGEle37_24 = cms.Path(process.DoubleEGEle3724)
process.pDoubleIsoTkPho22_12 = cms.Path(process.DoubleIsoTkPho2212)
process.pDoublePuppiJet112_112 = cms.Path(process.DoublePuppiJet112112)
process.pDoublePuppiTau52_52 = cms.Path(process.DoublePuppiTau5252)
process.pDoubleTkEle25_12 = cms.Path(process.DoubleTkEle2512)
process.pDoubleTkMuon15_7 = cms.Path(process.DoubleTkMuon157)
process.pIsoTkEleEGEle22_12 = cms.Path(process.IsoTkEleEGEle2212)
process.pPuppiHT400 = cms.Path(process.PuppiHT400)
process.pPuppiHT450 = cms.Path(process.PuppiHT450)
process.pPuppiMET200 = cms.Path(process.PuppiMET200)
process.pQuadJet70_55_40_40 = cms.Path(process.QuadJet70554040)
process.pSingleEGEle51 = cms.Path(process.SingleEGEle51)
process.pSingleIsoTkEle28 = cms.Path(process.SingleIsoTkEle28)
process.pSingleIsoTkPho36 = cms.Path(process.SingleIsoTkPho36)
process.pSinglePuppiJet230 = cms.Path(process.SinglePuppiJet230)
process.pSingleTkEle36 = cms.Path(process.SingleTkEle36)
process.pSingleTkMuon22 = cms.Path(process.SingleTkMuon22)
process.pTripleTkMuon5_3_3 = cms.Path(process.TripleTkMuon533)
process.digi2raw_step = cms.Path(process.DigiToRaw)
#process.L1T_DoubleNNTau52 = cms.Path(process.HLTL1Sequence+process.hltL1DoubleNNTau52)
#process.L1T_SingleNNTau150 = cms.Path(process.HLTL1Sequence+process.hltL1SingleNNTau150)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.digitisation_step)
process.schedule.insert(1, process.L1TrackTrigger_step)
process.schedule.insert(2, process.L1simulation_step)
process.schedule.insert(3, process.Phase2L1GTProducer)
process.schedule.insert(4, process.Phase2L1GTAlgoBlockProducer)
process.schedule.insert(5, process.pDoubleEGEle37_24)
process.schedule.insert(6, process.pDoubleIsoTkPho22_12)
process.schedule.insert(7, process.pDoublePuppiJet112_112)
process.schedule.insert(8, process.pDoublePuppiTau52_52)
process.schedule.insert(9, process.pDoubleTkEle25_12)
process.schedule.insert(10, process.pDoubleTkMuon15_7)
process.schedule.insert(11, process.pIsoTkEleEGEle22_12)
process.schedule.insert(12, process.pPuppiHT400)
process.schedule.insert(13, process.pPuppiHT450)
process.schedule.insert(14, process.pPuppiMET200)
process.schedule.insert(15, process.pQuadJet70_55_40_40)
process.schedule.insert(16, process.pSingleEGEle51)
process.schedule.insert(17, process.pSingleIsoTkEle28)
process.schedule.insert(18, process.pSingleIsoTkPho36)
process.schedule.insert(19, process.pSinglePuppiJet230)
process.schedule.insert(20, process.pSingleTkEle36)
process.schedule.insert(21, process.pSingleTkMuon22)
process.schedule.insert(22, process.pTripleTkMuon5_3_3)
process.schedule.insert(23, process.digi2raw_step)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# Bug relating to CMSSW_14_0_X where it doesn't overwrite existing root files when using htcondor 
process.add_(cms.Service("AdaptorConfig", native=cms.untracked.vstring("root")))

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
