import os
import sys 
import py2bit


#print Headings
print('Chromosome', 'Feature', 'Start', 'End', 'Strand',"ApA_ratio","ApT_ratio","ApG_ratio","ApC_ratio","TpA_ratio","TpT_ratio","TpG_ratio","TpC_ratio","GpA_ratio","GpT_ratio","GpG_ratio","GpC_ratio","CpA_ratio","CpT_ratio","CpG_ratio","CpC_ratio", sep = '\t')


bit_file = sys.argv[1]
gff_file = sys.argv[2]

bd = py2bit.open(bit_file , True)
def extract_promos():

    ''' 
    Get the coordinates from gff file, fetch the sequence from 2bit file and calculate the ratio 
    '''
    
    with open(gff_file) as fh:

        chrom = ''
        chrom_seq_length = 0
   
        for line in fh:
            if line.startswith('#'):
                    continue
            content = line.strip().split('\t')
            if chrom == '' or chrom != content[0]:
                chrom= content[0]
                chrom_seq_length = len(bd.sequence(str(content[0])))
          
            chrom= content[0]
            feature = content[2]
            start = int(content[3])
            end = int(content[4])
            strand = content[6]
        
            if feature == 'gene':
                if strand == '+':
                    window_start = start - 1000
                    window_end = window_start + 2000
                    if window_start > window_end or window_start < 1 or window_end < 1 or window_start == window_end or window_start > chrom_seq_length or window_end > chrom_seq_length or (window_end - window_start) < 1:
                        continue
                        
                    else:
                        
                        perseq = bd.sequence(chrom,window_start, window_end)
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
                    
            
                   

                else:                
                    window_start = end - 1000
                    window_end = window_start + 2000
                    if window_start > window_end or window_start < 1 or window_end < 1 or window_start == window_end or window_start > chrom_seq_length or window_end > chrom_seq_length or (window_end-window_start) < 1:
                        continue
                        
                    else:
                        perseq = bd.sequence(chrom,window_start, window_end)
                       
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
                print(chrom, start, end,  strand, 'Promoter', AA_ratio, AT_ratio , AG_ratio , AC_ratio , TA_ratio , TT_ratio , TG_ratio , TC_ratio , GA_ratio , GT_ratio , GG_ratio , GC_ratio , CA_ratio , CT_ratio , CG_ratio , CC_ratio, sep = "\t")


#main body
extract_promos()

#closing the files
bd.close()
