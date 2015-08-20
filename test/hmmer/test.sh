hmmsearch --notextw -o MHC_I.txt --domtblout MHC_I_domtbl.txt HMMs/MHC_I.hmm seq/6frames.fa

exonerate --model protein2genome --ryo ">match\n%tas\n\n" seq/pep_matches.fa seq/dna.fa > exonerate.txt
