import sys
import os
import pathlib


#file = sys.argv[1]
file = 'list'
current_path = str(pathlib.Path().absolute())
print (current_path)
with open(file,'r') as fh:
    for file_list in fh:
        file_list = file_list.strip()
        print("Running for ",end='\t')
        print(file_list)
        file_path = current_path+'/'+file_list
        directory_content = os.listdir(file_path)
        #print(directory_content)
        gff_file = file_list + '.gff'
        bit2_file = file_list + '.2bit'
     


        input_gff = file_path+'/'+gff_file
        #print(input_gff)
        input_2bit = file_path+'/'+bit2_file
        input1 = file_path+'/'+file_list+'_exon.txt'
        
        input2 = file_path+'/'+file_list +'_exon_violin_arranged.txt'
        #output_stat = file_path+'/'+file_list+'_exon_stat.txt'

        input1intron = file_path+'/'+file_list+'_intron.txt'
        
        input2intron = file_path+'/'+file_list +'_intron_violin_arranged.txt'
        #output_statintron = file_path+'/'+file_list+'_intron_stat.txt'

        input1promo = file_path+'/'+file_list+'_promo.txt'
        
        input2promo = file_path+'/'+file_list +'_promo_violin_arranged.txt'
        #output_statpromo = file_path+'/'+file_list+'_promo_stat.txt'

        # input1igene = file_path+'/'+file_list+'_igene.txt'
        
        # input2igene = file_path+'/'+file_list +'_igene_violin_arranged.txt'
        # #output_statigene = file_path+'/'+file_list+'_igene_stat.txt'

        command1 = 'python3 exons_ratio.py '+input_2bit+ ' ' + input_gff + '> ' +input1
        command2 = 'python3 violin_arranged_data.py '+  input1 + '> ' + input2
        #command3 = 'python3 stat.py '+input1+ '  > ' + output_stat

        command4 = 'python3 introns_ratio.py '+input_2bit+ ' ' + input_gff + '> ' +input1intron
        command5 = 'python3 violin_arranged_data.py '+  input1intron + '> ' + input2intron
        #command6 = 'python3 stat.py '+input1intron+ '  > ' + output_statintron

        command7 = 'python3 promo_ratio.py '+input_2bit+ ' ' + input_gff + '> ' +input1promo
        command8 = 'python3 violin_arranged_data.py '+  input1promo + '> ' + input2promo
        #command9 = 'python3 stat.py '+input1promo+ '  > ' + output_statpromo

        
        os.system(command1) 
        print('exons ratio extracted')
        os.system(command2)
        print('exon data arranged for violin plot')
        #os.system(command3)
        print('exon stats done')
        os.system(command4)
        print('introns_ratio_extracted')
        os.system(command5)
        print('intron data arranged for violin plot')
        #os.system(command6)
        print('intron stats done')
        os.system(command7)
        print('promo_ratio_extracted')
        
        os.system(command8)
        print('promo data arranged for violin plot')
        #os.system(command9)
        print('promo stats done')

     
        print("Run completed for ",end='\t')
        print(file_list)


