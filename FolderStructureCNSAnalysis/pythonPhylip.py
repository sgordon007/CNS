import subprocess

listFasta = ["NKHDS01100_CS.fasta","NKHDS01100_Mixed_CS.fasta","NKHDS01100_NonProteinCodingN_CS.fasta","NKHDS01100_ProteinCoding_CS.fasta","NKHDS01111_CS.fasta","NKHDS01111_Mixed_CS.fasta","NKHDS01111_NonProteinCodingN_CS.fasta","NKHDS01111_ProteinCoding_CS.fasta","NKHDS10100_CS.fasta","NKHDS10100_Mixed_CS.fasta","NKHDS10100_NonProteinCodingN_CS.fasta","NKHDS10100_ProteinCoding_CS.fasta","NKHDS10111_CS.fasta","NKHDS10111_Mixed_CS.fasta","NKHDS10111_NonProteinCodingN_CS.fasta","NKHDS10111_ProteinCoding_CS.fasta","NKHDS11100_CS.fasta","NKHDS11100_Mixed_CS.fasta","NKHDS11100_NonProteinCodingN_CS.fasta","NKHDS11100_ProteinCoding_CS.fasta","NKHDS11111_CS.fasta","NKHDS11111_Mixed_CS.fasta","NKHDS11111_NonProteinCodingN_CS.fasta","NKHDS11111_ProteinCoding_CS.fasta"]

for fasta in listFasta:
	phylName = fasta.replace('.fasta','.phylip')
	subprocess.call(['perl','Fasta2Phylip.pl',fasta,phylName])
