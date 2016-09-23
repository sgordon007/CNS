# Joshua-Levy-Synteny-Analysis
###Integrated Analysis of Synteny (Multiple Synteny Comparison for Multiple Alignment, Circos Outputs, Allmaps Genome Reconstructions), Find Ghost Genes, Identify and Analyze CNS Elements from Multiple Alignment Files and More!


##Using Integrated Analysis:
1. 


Note: Delete Sort Files after every analysis

###Using SyntenyFinal.py and Circos.py:
1. See their relevant readmes

###Using AllMAPS: (Must run on linux or linux server, for now)
Recommend: Run through the integrated analysis by setting performALLMAPS = 1
1. 


###Using ALLMAPS_alternate: (Must run on linux or linux server, for now)
Recommend: Run through the integrated analysis by setting performALLMAPSAlt = 1, must set performALLMAPS = 0
1. 

##Using findGhostSegments:
1. 



##Using CNS Analysis (workwithMAF and manipulateFilesTest):

### preparation
1.  make an analysis working directory that you populate with the relevant files.  For example:
a. all *.maf files e.g. FastaOut10.maf
b. all *.softmasked.fa and softmasked.fa.fai files
c. all query and target *.bed; target t.*.gff3, t.*.sort2, t.*CDS.bed3, t.*Genes.bed3
d. the workWithMAF.py file
e. configCNSAnalysis.txt file
f. the manipulateFilesTest.py script which is called by  workWithMAF.py if present in the working dir.
2.  make a CS directory within the working dir (modify joshua's makeFolders.sh to use mkdir -p to make CS dir and subdirs when run from working dir)
3. copy makeFolders.sh into that CS dir and run to create subdirs
4. export PYTHONPATH=/global/dna/projectdirs/plant/pangenomics/python_modules:$PYTHONPATH
5. module load bedtools/2.25.0
6. change directory back to working directory and run workWithMAF.py: python ./workWithMAF.py on gpint
7. change directory to CS dir
8. run python pythonPhylip.py in CS dir (it calls Fasta2Phylip.pl to convert format to Phylip format)
 

manipulateFilesTest.py concatenates files for the genome-wide analysis that Adam described to you which can be analyzed for trees.  It also calculates the ratios of subgenome conserved CS as a fraction of all CS for old and new CS.

6.  pythonPhylip.py (OK, I undertand this one, it just calls Fasta2Phylip.pl to convert format to Phylip format)

where does this one go? :   fasta_size.pl ( this gives sequence lengths that I know we need as Fasta2Phylip.pl has some bug or PhyML doesn't like the Phylip format written above, but how do we utilize this?

7.  pythonRunPhyML.py ( this one takes the Phylip formated files and runs PhyML)

fasta2phyAll.sh ( this script looks broken to me. Where does it fit? )
  
  
  
###What to do after CNS Analysis Completes:
1. Convert fasta files to phylip files and run them under PhyML to generate trees. Can visualize these trees using FigTree.
2. If using NERSC, module load PhyML. ^^^
