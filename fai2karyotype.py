from random import randint
def fai2karyotype(faiFilePath,karyotypesFilesPath,convertFiles,mainSpeciesFai):
    splitSubgenome = [0,0]
    listKaryotypes = []
    #sortFunction = lambda scaffold1, scaffold2: cmp(scaffold1[0], scaffold2[0])
    for file in convertFiles:
        # for N and K


        inputFile = open(faiFilePath+file,'r')
        outputFilename = 'karyotype.'+file[:file.rfind('_')]+'.txt'
        listKaryotypes.append(outputFilename)
        if '383' in file:
            splitSubgenome = [1, outputFilename]
        open(karyotypesFilesPath+outputFilename,'w').close()
        outputFile = open(karyotypesFilesPath+outputFilename,'w')
        chrCount = 1
        scaffoldOutList = []
        for line in inputFile:
            # generate output tuple from parsing input
            lineList = line.split()
            if int(lineList[1])>300000 and chrCount < 25:
                if '_' in lineList[0]:
                    outputTuple = (lineList[0],lineList[0][0]+lineList[0].split('_')[-1],lineList[1],chrCount)
                else:
                    outputTuple = (lineList[0], lineList[0], lineList[1], chrCount)
                if 'scaffold_' in line or 'super_' in line or 'ta_' in line:
                    scaffoldOutList += [list(outputTuple)]
                else:
                    if file == mainSpeciesFai:
                        outputFile.write('chr - %s %s 0 %s chr0\n'%tuple(list(outputTuple)[:3]))
                    else:
                        outputFile.write('chr - %s %s 0 %s chr%d\n' % outputTuple)
                        chrCount += 1
            if chrCount == 25:
                print('Chromosome count exceeded in %s (anymore chromosomes will not generate useful display...'
                      %outputFilename)
        # WORKING ON THIS!!! #FIXME
        if scaffoldOutList:
            try:
                scaffoldOutList.sort(key = lambda x: int(x[0].split('_')[-1]))
            except:
                print 'There is an error in '+ file
                exit()
            for scaffold in scaffoldOutList:
                scaffold[-1] = chrCount
                if 'ta' in scaffold[0]:
                    outputFile.write('chr - %s %s 0 %s %d,%d,%d\n' % tuple(scaffold[:3]+[randint(1,255),randint(1,255),
                                                                                      randint(1,255)]))
                elif chrCount < 25:
                    if file == mainSpeciesFai:
                        outputFile.write('chr - %s %s 0 %s chr0\n' % tuple(scaffold[:3]))
                    else:
                        outputFile.write('chr - %s %s 0 %s chr%d\n' % tuple(scaffold))
                        chrCount += 1

        outputFile.close()
        inputFile.close()

    if splitSubgenome[0] == 1:
        inputFile = open(karyotypesFilesPath+splitSubgenome[1],'r')
        outFilenameN = splitSubgenome[1][:splitSubgenome[1].rfind('_')+1]+'523.txt'
        outFilenameK = splitSubgenome[1][:splitSubgenome[1].rfind('_')+1]+'524.txt'
        listKaryotypes.append(outFilenameN)
        listKaryotypes.append(outFilenameK)


        open(karyotypesFilesPath+outFilenameN,'w').close()
        open(karyotypesFilesPath + outFilenameK, 'w').close()

        outputFileN = open(karyotypesFilesPath+outFilenameN,'w')
        outputFileK = open(karyotypesFilesPath+outFilenameK,'w')


        for line in inputFile:
            if 'N' in line:
                outputFileN.write(line[:line.rfind(' ')+1]+'blue\n')
            elif 'K' in line:
                outputFileK.write(line[:line.rfind(' ') + 1] + 'chr0\n')


        outputFileN.close()
        outputFileK.close()
        inputFile.close()
    return listKaryotypes


    # edit file to liking afterwards...


    """Bd1	75071545	5	80	81
    Bd1_centromere_containing_Bradi1g41430	46184	76009985	80	81
    Bd2	59130575	76056752	80	81
    Bd3	59640145	135926465	80	81
    Bd4	48594894	196312117	80	81
    Bd5	28630136	245514453	80	81
    scaffold_12	23566	274502479	80	81
    scaffold_135	3881	274526354	80	81
    scaffold_14	20560	274530297	80	81
    scaffold_180	1933	274551128	80	81"""

    """chr - hsX X 0 153692391 chrx
    chr - hsY Y 0 50286555 chry
    chr - hs1 1 0 246127941 chr1
    chr - hs2 2 0 243615958 chr2
    chr - hs3 3 0 199344050 chr3
    chr - hs4 4 0 191731959 chr4
    chr - hs5 5 0 181034922 chr5
    chr - hs6 6 0 170914576 chr6
    chr - hs7 7 0 158545518 chr7
    chr - hs8 8 0 146308819 chr8
    chr - hs9 9 0 136372045 chr9
    chr - hs10 10 0 135037215 chr10
    chr - hs11 11 0 134482954 chr11
    chr - hs12 12 0 132078379 chr12
    chr - hs13 13 0 113042980 chr13
    chr - hs14 14 0 105311216 chr14
    chr - hs15 15 0 100256656 chr15
    chr - hs16 16 0 90041932 chr16"""

    """Bstacei_316_v1.0.softmasked.fa.fai
    Osativa_323_v7.0.softmasked.fa.fai
    Phallii_308_v2.0.softmasked.fa.fai
    Pvirgatum_383_v3.0.softmasked.fa.fai
    Sbicolor_313_v3.0.softmasked.fa.fai
    Sitalica_312_v2.softmasked.fa.fai
    Sviridis_311_v1.0.softmasked.fa.fai"""