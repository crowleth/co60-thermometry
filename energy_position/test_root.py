import ROOT

# Create a histogram
h = ROOT.TH1F("h", "My First PyROOT Histogram", 100, -5, 5)
h.FillRandom("gaus", 1000)

# Create a canvas and draw
c = ROOT.TCanvas("c", "c", 800, 600)
h.Draw()

# Keep the window open
input("Press Enter to close...")