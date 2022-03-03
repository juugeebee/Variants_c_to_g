#!/usr/bin/env python
# encoding: utf-8

print('\n****************************')
print('***** VariantValidator *****')
print('****************************')

import requests

file = '15920_vv_input.txt'
output = '15920_vv_output.txt'

fichier = open(output, "a")

with open(file, 'r') as filin:
    
    for variant_description in filin:

        print(variant_description)
    
        link = 'https://rest.variantvalidator.org' + \
            '/VariantValidator/variantvalidator/hg19/' + \
            variant_description + '/NM_001287174.1'

        r = requests.get(link)

        if r.status_code == 200:

            print('VV ok\n')
            
            rd = r.json()

            for cle, valeur in rd.items():
                if cle.startswith('NM'):
                    fichier.write(rd[cle]['primary_assembly_loci']['hg19']['hgvs_genomic_description'] \
                     + '\t' + cle + '\n')

        elif r.status_code == 404:
            
            print('Not Found.')

fichier.close()

print('****************************')
print('******* JOB DONE ! *********')
print('****************************\n')
     

