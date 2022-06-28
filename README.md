# Dinucleotide-patterns
Dinucleotide pattern in various genomic regions of Homo sapiens and in exonic region of eukaryotes
Dinucleotide is two adjacent nucleotides in a DNA separated by a single phosphate group. From the four nitrogen bases, (4*4) 16 dinucleotides can be derived, which are<b> ApA,  ApT, ApG, ApC, TpA, TpT, TpG, TpC, GpA, GpT, GpG, GpC, CpA, CpT, CpG</b> and <b>CpC</b>. There is a distinct signature of dinucleotide and its difference among different species (Gentles, A. J. (2001). This may be due to DNA replication and repair mechanisms and biases in DNA modification processes like base-step stacking energies and DNA conformational tendencies, context dependent mutation, and DNA methylation patterns (Karlin 1998).

<p> <b>Supplementary file details  </b></p>
 <p>Supplementary file 1.ipynb - Jupyter notebook python code snippets for data mining, renaming, and filtering. </p> 
<p>Supplementary file 2 - Refseq list  for eukaryotes provided as of Jan2  from NCBI</p>
<p>Supplementary_file_3_feature_extraction.py,  this code will take the input of feature coodrinates such a say SINES or CpGisland and calculates the dinucleotide ratio </p>
<p>Supplementary_file_4_stat.py  , this code will calculate basic statistics such as mean, median, mode , screwness and kurtosis of the ratio</p>
<p>Supplementary_file_5_violin_arranged_data.py , this code will arrange our ratio data file into a formatted input file for violin plot</p>
<p>Supplementary_file_6_violin_plot.py ,  This code will create a violin plot from holoviews library  </p>
<p>Supplementary_file_7_cluster_heatmap.ipynb , this code will create cluster heat map based on euclidean distance </p>
<p>Supplementary_file_8.a_exons_ratio.py , this code calculates the dinucleotide ratio of exons from GFF and 2bit file of an organism </p>
<p>Supplementary_file_8.b_intron_ratio.py , this code calculates the dinucleotide ratio of intron  from GFF and 2bit file of an organism</p>
<p>Supplementary_file_8.c_promo_ratio.py  , this code calculates the dinucleotide ratio of promoter from GFF and 2bit file of an organism </p>




<h2>Data collection</h2>
 
The latest versions of eukaryotic genome sequences available on NCBI’s RefSeq database were downloaded from the FTP site of NCBI (https://ftp.ncbi.nlm.nih.gov/genomes/refseq/ ). A python code (Supplementary file1) was written to mine the GFF and  FASTA files from the NCBI RefSeq list(Supplementary file2). The Fasta files were converted to bit files as they are computationally efficient (requiring low space and faster calculation) using UCSC faToTwoBit (https://genome.ucsc.edu/goldenPath/help/twoBit.html). 
 
<h3>Calculation of ratio</h3>
 
<h3>Calculation of ratio from the various genomic regions of Homo sapiens.</h3>
 
Coordinations for various genome regions were taken from the UCSC genome browser (https://genome.ucsc.edu/cgi-bin/hgTables ). An in-house python code was written to calculate ratios(Supplementary file 3), and statistics (Supplementary file 4). A violin plot was made ( Supplementary files 5 and 6).  A median value was taken from the ratio and a cluster heat map was constructed by Seaborn package python based on euclidian distance (Supplementary file 7).   
 
 
<h3>Calculation of ratio from the exon  of the eukaryotes genome.</h3>
 
Fasta file and GFF file were taken from NCBI RefSeq. 1100 eukaryotes were considered which had well-annotated GFF files,  among them, 436 vertebrates,179 invertebrates, 273 fungi,  84 protozoa and 128 plants.
Coordinates for exon, intron and promotor were taken from the GFF file, python script was written ( Supplementary_file_8) to calculate the observed by expected ratio from all three regions of genomes. A violin plot was made for each organism’s exon, intron and promoter region.The promoter region was defined as 1000 upstream and 1000 downstream of TSS  (Gene, strand ‘+’ ) and TTS (Gene, strand ‘-’) region. General statistics were calculated and the median ratio was taken. From the median ratio of exonic region, cluster heatmap was made.

