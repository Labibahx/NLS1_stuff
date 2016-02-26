# Feb 9th 2016
# plot spectra to examine their model fittings and flag the bad ones

import numpy as np
from astropy.table import Table, Column
import seaborn as sns

def spec_inspec(n1,n2):
    '''
    param:
    n1: start line
    n2: end line
    
    '''

    #t = Table.read("/Users/tammour/NLS1_sept2015/data-fig/NLS1-Data.fits") #read table with the names of the files containing the spectra and their fits

    #spec_ls= t['spSpec'] # list of the spectra files
    #spec_ls= Table.read('plt_ls.txt', format= 'ascii')
    spec_ls= open('plt_ls.txt', 'r')
    s= spec_ls.readlines()
    
    flags= [] # list of flags for bad fits
    f_out = open("./obj_flg"+str(n1)+"_"+str(n2)+".txt", 'wr')
    

    for i in s[n1:n2]:
        spec_name= i.rstrip()
        try:

            spec= Table.read(spec_name, format= 'ascii', data_start=2)
        
            fig= figure(figsize= (20,12))
            ax1= subplot2grid((10,10), (0, 0), colspan=10, rowspan=8)
            ymax= max(spec['col2'])
            ax1.set_ylim(0, ymax)
            ax1.set_xlim(4500, 5400)
            text(4600, ymax-(ymax/10), s)
        
            # plot spectrum and model fit components
        
            plot(spec['col1'], spec['col2'], lw= 2, c= '0.5') # spectrum
            plot(spec['col1'], spec['col4'], lw= 1, c= 'r') # full model
            plot(spec['col1'], spec['col5'], lw= 1, c= 'y') # powerlaw continuum
            plot(spec['col1'], spec['col6'], lw= 1, c= 'c') # narrow Hbeta
            plot(spec['col1'], spec['col7'], lw= 1, c= 'b') # Lorentzian Hbeta
            plot(spec['col1'], spec['col8'], lw= 1, c= 'm') # narrow [OIII]
            plot(spec['col1'], spec['col9'], lw= 1, c= 'c') # broad [OIII]
            plot(spec['col1'], spec['col10'], lw= 1, c= 'm') # narrow [OIII]
            plot(spec['col1'], spec['col11'], lw= 1, c= 'c') # broad [OIII]
            plot(spec['col1'], spec['col12'], lw= 1, c= 'gold') # FeII
        
            # vertical lines to mark line restframe wavelengths
        
            axvline(4863, ls=':', c='k')
            axvline(4960, ls= ':', c='k')
            axvline(5007, ls= ':', c='k')
       
        
            xlabel('Restframe wavelength ($\AA$)')
            ax1.set_xticklabels([])
            ylabel('Normalized flux')
        
        
            ax2= subplot2grid((10,10), (8, 0), colspan=10, rowspan=2)
            ylabel('Residuals')
            ax2.set_ylim(-10,10)
            ax2.set_xlim(4500, 5400)
            scatter(spec['col1'], spec['col2']-spec['col4'], marker='+', color= '0.3')
            print "plotting obj", spec_name
            flg= input("Good fit= 0, Bad fit= 1 \n flag= ")
            flags.append(flg)
            f_out.write(spec_name + ","+ str(flg) + '\n')
            
            resume = input("Press Enter to plot next spectrum on list.")
            clf()
    
        except SyntaxError:
            pass

            #clf()
        close(fig)

    f_out.close()
        
    #c= Column(name= 'fit_flg', data= flags)
        
    #t.add_column(c)
        
    #t.write('NLS1_data_flgs.fits')

    return()



