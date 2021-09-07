#!/usr/bin/env python
# encoding: utf-8

print('\n****************************')
print('***** VariantValidator *****')
print('****************************')

import requests

file = '/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques/15814_ABCC8intronique.csv'
output = '/media/jbogoin/Sep2020-JGB/Donnees_brutes/hg19/Metabo/variants_introniques/15814_genomique.txt'
input_list = []
output_list = []

fichier = open(output, "a")

with open(file, 'r') as filin:
    
    for variant_description in filin:
    
        link = 'https://rest.variantvalidator.org/' + '/VariantValidator/variantvalidator/' \
            + 'hg19/' + variant_description + '/NM_001287174.1'

        r = requests.get(link)

        if r.status_code == 200:
            
            rd = r.json()

            for cle, valeur in rd.items():
                if cle.startswith('NM'):
                    fichier.write(rd[cle]['primary_assembly_loci']['hg19']['hgvs_genomic_description'] \
                     + '\t' + cle + '\n')

        elif response.status_code == 404:
            print('Not Found.')

fichier.close()

print('****************************')
print('******* JOB DONE ! *********')
print('****************************\n')
     

