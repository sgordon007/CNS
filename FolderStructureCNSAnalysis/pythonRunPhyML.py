import subprocess
phylipfiles = ["NKHDS01111_CS.phylip","NKHDS01111_Mixed_CS.phylip","NKHDS01111_NonProteinCodingN_CS.phylip","NKHDS01111_ProteinCoding_CS.phylip","NKHDS10111_CS.phylip","NKHDS10111_Mixed_CS.phylip","NKHDS10111_NonProteinCodingN_CS.phylip","NKHDS10111_ProteinCoding_CS.phylip","NKHDS11100_CS.phylip","NKHDS11100_Mixed_CS.phylip","NKHDS11100_NonProteinCodingN_CS.phylip","NKHDS11100_ProteinCoding_CS.phylip","NKHDS11111_CS.phylip","NKHDS11111_Mixed_CS.phylip","NKHDS11111_NonProteinCodingN_CS.phylip","NKHDS11111_ProteinCoding_CS.phylip"]

for file in phylipfiles:
	subprocess.call(['PhyML','-i',file,'-s','BEST','-q','-b','250','-m','GTR'])
