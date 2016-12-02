def gff2bedobjs(self):
    outputfilename = self.gffFile.replace('.gff', '_Genes.bed').replace('.gff3', '_Genes.bed')
    outputfilename2 = self.gffFile.replace('.gff', '_CDS.bed').replace('.gff3', '_CDS.bed')
    open(outputfilename, 'w').close()
    open(outputfilename2, 'w').close()
    outputFile = open(outputfilename, 'w')
    outputFile2 = open(outputfilename2, 'w')
    for line in open(self.gffFile, 'r'):
        if line:
            if 'mRNA' in line and 'longest=1' in line:
                geneName = line.split()[-1].split(';')[1].replace('Name=', '')
                outputFile.write(
                    '%s\t%d\t%s\t%s\n' % (line.split()[0], int(line.split()[3]) - 1, line.split()[4], geneName))

            if 'CDS' in line:
                if not geneName:
                    geneName = 'NoCNSName'
                outputFile2.write(
                    '%s\t%d\t%s\t%s\n' % (line.split()[0], int(line.split()[3]) - 1, line.split()[4], geneName))

                # outputFile.write('%s\t%d\t%s\n' % (line.split()[1],int(line.split()[2])-1,line.split()[3]))
    outputFile.close()
    outputFile2.close()
    self.bedGenes = BedTool(outputfilename).sort()
    self.bedCDS = BedTool(outputfilename2).sort()
