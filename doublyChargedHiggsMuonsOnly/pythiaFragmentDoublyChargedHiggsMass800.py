import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(  
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',
            'LeftRightSymmmetry:ffbar2HLHL = on',
            '9900041:onMode = off',
            '9900041:m0 = 800',
            '9900041:onIfAll = 13 13',#Turn on dimuon
            'LeftRightSymmmetry:coupHee = 0', #Turn off electron coupling
            'LeftRightSymmmetry:coupHmue = 0',
            'LeftRightSymmmetry:coupHmumu = .02',
            'LeftRightSymmmetry:coupHtaue = 0',
            'LeftRightSymmmetry:coupHtaumu = 0',
            'LeftRightSymmmetry:coupHtautau = 0',
            'LeftRightSymmmetry:vL = 0'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters',
            )
        )
    )
