# Joshua-Levy-Synteny-Analysis
### Analysis of Synteny (Multiple Synteny Comparison for Multiple Alignment, Circos Outputs, Genome Reconstruction, Identify and Analyze CNS Elements from Multiple Alignment Files



##Using Integrated Analysis:

## Setup:
##SyntenyFinal.py : generates Fasta files that essentially stitch together pairwise comparisons of syntenic sequences across multiple species/comparisons.
Input:
1. synteny files: header specifies start/end genes for a syntenic sequence (eg. 3012974 – 3013249) for a particular chromosome of a species. start and end genes will be matched up with geneIDs/names to identify exact coordinates and orientation of synteny between two species
2. .sort2 files- The gff files MUST be parsed using gff2sort to generate .sort2 files. This is a simplified version of the .gff file and is used for a fast and speedy final analysis. Each line is organized by 
geneID   ChromosomeName   startCoordinate   endCoordinate of gene. The genes are referenced in the unout file and found in the sort2 files during the analysis. 
3. .fa files- These are the files that contain the entire sequence of the genome for particular species. These files will be turned into python Fasta objects during the analysis and their syntenic sequences will be exported into another fasta file
4.  syntenicConfig.txt : File used to set up entire analysis. If you wish to have a different file name, please edit it within the python script for syntenyFinal.

## Run the scripts:
1. Setup main folder where analysis will be performed
2. make subdirs and copy over files:
FastaFileOutputsAnalysis  GFFFiles  Genomes  SortFiles	SyntenyFinal.py  UnOutFiles  syntenicConfig.txt
3. Edit the paths listed to reflect your analysis. Edit pathPythonModule (the path where to find modules you have installed so it can run the right libraries), pathUnOut, pathSort, XXX Test Analysis path, genomePath… Also, change name from N Test Analysis to XXX(your analysisname) Test Analysis and replace N with XXX for analysisName= XXX. XXX will also be input argument to the main function in syntenyFinal. You can erase all other info from any other analysis (N or K in this case)…
4. 1.	Drag .fa genome files to the genomes folder and add names of genome .fa files to syntenicConfig.txt (the .fai files in the picture will be generated from the analysis Fasta structure). Species number (eg. 383 should be surrounded by two ‘_’ for file name)
Use softmasked genome assemblies
5. 1.	Drag/copy gff2sort.py and all .gff files to folder GFFfiles and rename by the following conventions:
a.	Rename file with either ‘q.’ or ‘t.’ followed by ‘PAC4GC.’ Or ‘PAC2_0.’ Followed by species name/number (eg. 383, needs to correspond to species number on .fa) followed by .gff or .gff3.
b.	Example: t.PAC2_0.383.gff3 corresponds to Pvirgatum_383_v3.0.softmasked.fa
524 and 523 are both special cases… Try to follow usual naming convention
6. Edit gff2sort.py by changing the list variable gffFiles. You will erase the contents of the variable gffFiles and type in the name of the gff files you need to convert to sort2 files. Save and run this script from the terminal. .sort2 files will be created, and copy all of them over to the SortFiles folder.
7. Copy all unout pairwise Synteny comparisons files to the UnOutFiles folder.

OtherFiles/AdditionalAnalysisScripts/gff2sort.py



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
### run code
4. export PYTHONPATH=/global/dna/projectdirs/plant/pangenomics/python_modules:$PYTHONPATH
5. module load bedtools/2.25.0
6. change directory back to working directory and run workWithMAF.py: python ./workWithMAF.py on gpint
(manipulateFilesTest.py concatenates files for the genome-wide analysis that Adam described to you which can be analyzed for trees.  It also calculates the ratios of subgenome conserved CS as a fraction of all CS for old and new CS.)
7. change directory to CS dir
8. python ./pythonPhylip.py in CS dir (it calls Fasta2Phylip.pl to convert fasta format to Phylip format)
    can check lengths of fasta seqs with fasta_size.pl ( this gives sequence lengths that I know we need as Fasta2Phylip.pl has some bug or PhyML doesn't like the Phylip format written above, but how do we utilize this?
9. module load PhyML/3.1
10. python ./pythonRunPhyML.py in CS dir
( this one takes the Phylip formated files and runs PhyML)
### visualize
11. Can visualize these trees using FigTree.  Download the tree and use figtree on mac.



  
  