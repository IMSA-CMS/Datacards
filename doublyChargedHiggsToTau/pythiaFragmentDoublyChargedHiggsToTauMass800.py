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
			'Main:timesAllowErrors = 10000',
			'ParticleDecays:limitTau0 = on',
			'ParticleDecays:tauMax = 10',
			'PartonLevel:MPI = on',
			'PartonLevel:ISR = on',
			'PartonLevel:FSR = on',
			'PhaseSpace:mHatMax = -1',                       
			'PhaseSpace:mHatMin = -1',
			'9900041:onMode = off',
			'9900041:onIfAll = 15', #Turns on tau
			'9900041:offIfAny = 13 13', #Turns off muon
			'9900041:offIfAny = 11 11', #Turns off electron                        
			'9900042:onMode = off',
			'9900042:offIfAny = 11 13',
			'9900042:onIfAll = 15',                                                 
			'LeftRightSymmmetry:ffbar2HLHL = on',                        
			'LeftRightSymmmetry:ffbar2HRHR = off',
			'LeftRightSymmmetry:coupHee = 0',
			'LeftRightSymmmetry:coupHmue = 0',
			'LeftRightSymmmetry:coupHmumu = 0',
			'LeftRightSymmmetry:coupHtaue = 0',
			'LeftRightSymmmetry:coupHtaumu = 0',
			'LeftRightSymmmetry:coupHtautau = .02',                        
			'LeftRightSymmmetry:vL = 0',
			'9900041:m0 = 800',
			'9900042:m0 = 800',
			'WeakDoubleBoson:ffbar2gmZgmZ = off',
			'WeakZ0:gmZmode = 2',
			'15:onMode = off', 
			'15:onIfAny = 11 13',
			),
		parameterSets = cms.vstring('pythia8CommonSettings',
			'pythia8CP5Settings',
			'pythia8PSweightsSettings',
			'processParameters',
			)
		)
	)
