import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *  

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock, 
        processParameters = cms.vstring(  
            'Tune:pp 5',
            'Tune:ee 3',
            'PartonLevel:MPI = on',
            'PartonLevel:ISR = on',
            'PartonLevel:FSR = on',
            'SUSY:all = on',
                        'SLHA:readFrom = 2',
                        'SLHA:file = leptonJet.spc',


                        '4900001:m0 = 6.5',
                        '4900002:m0 = 0.1',
                        '4900003:m0 = 4.5',
                        '4900004:m0 = 2',

                        '4900001:spinType = 1',
                        '4900002:spinType = 1',
                        '4900003:spinType = 1',
                        '4900004:spinType = 2',

                        '4900001:chargeType = 0',
                        '4900002:chargeType = 0',
                        '4900003:chargeType = 0',
                        '4900004:chargeType = 0',

                        '4900001:colType = 0',
                        '4900002:colType = 0',
                        '4900003:colType = 0',
                        '4900004:colType = 0',

                        '4900001:name = darkPseudoScalar',
                        '4900002:name = darkLightHiggs',
                        '4900003:name = darkHeavyHiggs',
                        '4900004:name = darkFermion',

                        '4900001:antiname = darkPseudoScalarBar',
                        '4900002:antiname = darkLightHiggsBar',
                        '4900003:antiname = darkHeavyHiggsBar',
                        '4900004:antiname = darkFermionBar',

                        '4900005:m0 = 1000000',
                        '4900006:m0 = 1000000',
                        '4900011:m0 = 1000000',
                        '4900012:m0 = 1000000',
                        '4900013:m0 = 1000000',
                        '4900014:m0 = 1000000',
                        '4900015:m0 = 1000000',
                        '4900016:m0 = 1000000',
                        '4900021:m0 = 1000000',
                        '4900023:m0 = 1000000',
                        '4900101:m0 = 1000000',
                        '4900111:m0 = 1000000',
                        '4900113:m0 = 1000000',
                        '4900211:m0 = 1000000',
                        '4900213:m0 = 1000000',
                        '4900991:m0 = 1000000',

                        '4900022:mayDecay = true',
                        '1000022:mayDecay = true',
                        '4900002:mayDecay = off',
                        '4900004:mayDecay = off',
                        '4900022:m0 = 0.4',
                        '4900022:0:meMode = 0',

                        'HiddenValley:Ngauge = 1',
                        'HiddenValley:doKinMix = on',
                        'HiddenValley:FSR = on',
                        'HiddenValley:alphaFSR = 0'
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
            'pythia8CP5Settings',
            #'pythia8PSweightsSettings',
            'processParameters',
            )
        )
    )

