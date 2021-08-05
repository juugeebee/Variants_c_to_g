import pandas
import numpy

entree = '15920_ABCC8intronique_snp.txt'
sortie = './SpliceAI/15920_ABCC8intronique_genomique_vcf_format.csv'
chromosome = '11'

dfi = pandas.read_csv(entree, sep='\t', names=['g','c'])
dfa = dfi['g'].str.split(pat='.', n=1, expand=True)
dfb = dfa[1].str.split(pat=':', n=1, expand=True)
vcf = pandas.DataFrame(columns=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO'])
vcf['CHROM'] = chromosome
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
vcf.to_csv(sortie, sep='\t', header=False, index=False)

print('\n' + sortie + 'genere\n')

