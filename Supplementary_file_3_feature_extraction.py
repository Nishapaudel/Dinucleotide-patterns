import os
import sys
import py2bit

# This output of this code should look in the format like 'Zerene_cesonia_exon.txt' as uploaded  
# set up variables
bit_file = sys.argv[1] # 'hg38.2bit' # The 2bit file of human we get from  UCSC https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/
gff_file = sys.argv [2] # # The feature file obtained from https://genome.ucsc.edu/cgi-bin/hgTables, It should look like UCSC_feature_file_sample 
  

chr_name = ''
chr_seq_length = 0
#printheadings
print("Chromosome","Feature","Start","End","Strand",  "ApA_ratio","ApT_ratio","ApG_ratio","ApC_ratio","TpA_ratio","TpT_ratio","TpG_ratio","TpC_ratio","GpA_ratio","GpT_ratio","GpG_ratio","GpC_ratio","CpA_ratio","CpT_ratio","CpG_ratio","CpC_ratio", sep='\t')
bd = py2bit.open(bit_file,True)
with open (gff_file) as fh:
    for line in fh:
        if line.startswith('#'):
            continue
        content = line.strip().split('\t')
        print(content)
        if chr_name == '' or chr_name != content[0]:
            chr_name = content [0]
            chr_seq_length = len(bd.sequence(str(content[0])))
        chrom = content[0]
        feature = content[3]
        print(feature)
        start = int(content[1])
        end = int(content[2])
        
        if feature == 'enhancer': ## need to customize this code a little bit by looking at the UCSC coodinate file, use UCSC 2bit file for UCSC coodinates
            f_start = start
            f_end = end
            if exon_start > f_end or f_start < 1 or f_end < 1 or  f_start == f_end or (f_end-f_start) < 1 or f_start > chr_seq_length or f_end > chr_seq_length:
                continue
            perseq = bd.sequence(chrom, f_start, f_end)    
            A = int(perseq.upper().count('A'))
            T = int(perseq.upper().count('T'))
            G = int(perseq.upper().count('G'))
            C = int(perseq.upper().count('C'))
            AA = int(perseq.upper().count('AA'))
            AT = int(perseq.upper().count('AT'))
            AG = int(perseq.upper().count('AG'))
            AC = int(perseq.upper().count('AC'))
            TA = int(perseq.upper().count('TA'))
            TT = int(perseq.upper().count('TT'))
            TG = int(perseq.upper().count('TG'))
            TC = int(perseq.upper().count('TC'))
            
            GA = int(perseq.upper().count('GA'))
            GT = int(perseq.upper().count('GT'))
            GG = int(perseq.upper().count('GG'))
            GC = int(perseq.upper().count('GC'))
            CA = int(perseq.upper().count('CA'))
            CT = int(perseq.upper().count('CT'))
            CG = int(perseq.upper().count('CG'))
            CC = int(perseq.upper().count('CC'))

            seq_len = len(perseq)
                                    
            if AA < 1 or AT < 1 or AG < 1 or AC < 1 or  TA < 1 or TT < 1 or TG < 1 or TC < 1 or  GA < 1 or GT < 1 or GG < 1 or GC < 1 or  CA < 1 or CT < 1 or CG < 1 or CC < 1 or   G < 1 or C < 1 or seq_len < 100:
                continue    
                
            AA_ratio = round(((AA/ (A*A))*seq_len),2)
            AT_ratio = round(((AT/ (A*T))*seq_len),2)
            AG_ratio = round(((AG/ (A*G))*seq_len),2)
            AC_ratio = round(((AC/ (A*C))*seq_len),2)

            TA_ratio = round(((TA/ (T*A))*seq_len),2)
            TT_ratio = round(((TT/ (T*T))*seq_len),2)
            TG_ratio = round(((TG/ (T*G))*seq_len),2)
            TC_ratio = round(((TC/ (T*C))*seq_len),2)

            GA_ratio = round(((GA/ (G*A))*seq_len),2)
            GT_ratio = round(((GT/ (G*T))*seq_len),2)
            GG_ratio = round(((GG/ (G*G))*seq_len),2)
            GC_ratio = round(((GC/ (G*C))*seq_len),2)

            CA_ratio = round(((CA/ (C*A))*seq_len),2)
            CT_ratio = round(((CT/ (C*T))*seq_len),2)
            CG_ratio = round(((CG/ (C*G))*seq_len),2)
            CC_ratio = round(((CC/ (C*C))*seq_len),2)
            #print(content[0],feature, exon_start, exon_end,content[6], CG_ratio, GC_ratio , sep = '\t', file = fout1 )
            
            print( content[0],feature, exon_start, exon_end,content[6],AA_ratio, AT_ratio, AG_ratio , AC_ratio , TA_ratio , TT_ratio , TG_ratio , TC_ratio , GA_ratio , GT_ratio , GG_ratio , GC_ratio , CA_ratio , CT_ratio , CG_ratio , CC_ratio, sep = "\t")
