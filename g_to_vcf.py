import pandas
import numpy
import subprocess

entree = '15814_vv_output.txt'
sortie = '15814_vcf_format.txt'

dfi = pandas.read_csv(entree, sep='\t', names=['g','c'])
dfb = dfi['g'].str.split(pat=':', n=1, expand=True)

vcf = pandas.DataFrame(columns=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO'])

dfc = dfb[1].str.split(pat='.', n=2, expand=True)
vcf['ID'] = dfb[1]

vcf['POS'] = dfb[1].str.extract('(\d+)')

dfd = dfb[1].str.split(pat='(\d+)', n=2, expand=True)
dfe = dfd[2].str.split(pat='>', n=3, expand=True)
vcf['REF'] = dfe[0].replace(numpy.nan, '.')
vcf['ALT'] = dfe[1].replace(numpy.nan, '.')

vcf['REF'] = vcf['REF'].replace('dup', '.')
vcf['REF'] = vcf['REF'].replace('ins', '.')
vcf['REF'] = vcf['REF'].replace('del', '.')
vcf['REF'] = vcf['REF'].replace('_', '.')

vcf['QUAL'] = '.'
vcf['FILTER'] = '.'
vcf['INFO'] = '.'

vcf['CHROM'] = '11'

vcf.to_csv(sortie, sep='\t', header=False, index=False)

subprocess.call("cat vcf_header.txt 15814_vcf_format.txt > \
    15814_spliceai_input.vcf", shell="/bin/bash")

subprocess.call("spliceai -I 15814_spliceai_input.vcf \
    -O 15814_spliceai_output.vcf \
    -R /media/jbogoin/Data1/References/fa_hg19/hg19_std_M-rCRS_Y-PAR-mask.fa \
    -A grch37 -D 4999", shell="/bin/bash")

print('\n' + sortie + ' genere !\n')

