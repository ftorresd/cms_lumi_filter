import json
import ROOT
from tqdm import tqdm

ROOT.PyConfig.DisableRootLogon = True
ROOT.PyConfig.IgnoreCommandLineOptions = False
ROOT.gROOT.SetBatch(True)



## Data
data_chain = ROOT.TChain("Events")
print "--> Adding Data files to chain..."
# Dataset: /SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD
# List all files.
# dasgoclient -query="file dataset=/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD"

data_chain.Add("/eos/cms/store/user/ftorresd/forSanila/SingleMuon_Data/02E7A5CB-7E72-DD45-A973-BA4114267C73.root")



def good_event(run,lumi):
    # Check whether this a good event
    with open('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt') as json_file:
      JSONlist = json.load(json_file)

      if str(run) in JSONlist.keys():
          for rg in JSONlist[str(run)]:
              if len(rg) ==2:
                  if lumi>=rg[0] and lumi<=rg[1]:
                      return True
      
      return False

if __name__ == "__main__"
    for ievt, evt in tqdm(enumerate(data_chain), desc ="Events"):     #(REAL CMS DATA)
        print good_event(evt.run, evt.luminosityBlock)
