```
cmsrel CMSSW_14_1_0_pre5 # also tried with CMSSW_14_0_0_pre3, see error below
cd CMSSW_14_1_0_pre5/src
git cms-init
git cms-merge-topic felicepantaleo:ticlv5_14_1_0_pre2 #TICLv5 already in release so use newer CMSSW version
git cms-merge-topic osschar:g4snitch-14.0-p3

scram b disable-biglib
cmsenv

# USER_CXXFLAGS="-g -O0" scram b -j 16

bash SimG4Core/HelpfulWatchers/g4s-test/make_dict.sh

scram b -j32 # You still have to build it even though you are manually building the file

git clone git@github.com:mnmat/G4SnitchSampleProduction.git

```
