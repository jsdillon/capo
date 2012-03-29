''' This is a calibration file for data collected at PAPER in Karoo, South Africa
on JD 2455819 '''

import aipy as a, numpy as n,glob,ephem
import bm_prms as bm
import generic_catalog
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('psa743_v004_gc')

class Antenna(a.pol.Antenna):
    def __init__(self,*args,**kwargs):
        a.pol.Antenna.__init__(self,*args,**kwargs)
        self.dpos = kwargs['dpos']
        self._pos = self.pos.copy()
        self.update()
    def update(self):
        a.pol.Antenna.update(self)
        self.pos = self._pos + self.dpos
        self._bm_gain = a.pol.Antenna.bm_response(self,(0,0,1),pol=self.pol)[0,0]
    def bm_response(self,*args,**kwargs):
        return a.pol.Antenna.bm_response(self,*args,**kwargs)/self._bm_gain
    def get_params(self, prm_list=['*']):
        """Return all fitable parameters in a dictionary."""
        x,y,z = self._pos
        aprms = {'x':x, 'y':y, 'z':z, 'dly':self._phsoff[-2],
            'off':self._phsoff[-1], 'phsoff':self._phsoff}
        aprms['dx'] = self.dpos[0]
        aprms['dy'] = self.dpos[1]
        aprms['dz'] = self.dpos[2]
        aprms['bp_r'] = list(self.bp_r)
        aprms['bp_i'] = list(self.bp_i)
        aprms['amp'] = self.amp
        aprms.update(self.beam.get_params(prm_list))
        prms = {}
        for p in prm_list:
            if p.startswith('*'): return aprms
            try: prms[p] = aprms[p]
            except(KeyError): pass
        return prms
    def set_params(self, prms):
        """Set all parameters from a dictionary."""
        changed = False
        self.beam.set_params(prms)
        try: self._pos[0], changed = prms['x'], True
        except(KeyError): pass
        try: self._pos[1], changed = prms['y'], True
        except(KeyError): pass
        try: self._pos[2], changed = prms['z'], True
        except(KeyError): pass
        try: self.dpos[0], changed = prms['dx'], True
        except(KeyError): pass
        try: self.dpos[1], changed = prms['dy'], True
        except(KeyError): pass
        try: self.dpos[2], changed = prms['dz'], True
        except(KeyError): pass
        try: self._phsoff[-2], changed = prms['dly'], True
        except(KeyError): pass
        try: self._phsoff[-1], changed = prms['off'], True
        except(KeyError): pass
        try: self._phsoff, changed = prms['phsoff'], True
        except(KeyError): pass
        try: self.bp_r, changed = prms['bp_r'], True
        except(KeyError): pass
        try: self.bp_i, changed = prms['bp_i'], True
        except(KeyError): pass
        try: self.amp, changed = prms['amp'], True
        except(KeyError): pass
        if changed: self.update()
        return changed

prms = {
    'loc': ('-30:43:17.5', '21:25:41.9'), # KAT, SA (GPS)
    'antpos':{
        0:[147.659407413, 336.269469733, 264.566180759],
        1:[-120.566931266, -270.142735412, -201.208899961],
        2:[175.483874,-282.046474,309.593714],
        3:[-24.5939776529, -369.022493234, -35.9049669793],
        #--------------------------------------------------------
        4:[-135.977107,-65.373043,-223.715356],
        5:[-184.222167454,  60.9256169154, -307.675312464],
        6:[84.568610,-397.906007,151.703088],
        7:[60.9037241018, 422.222408268, 116.124879563],
        #--------------------------------------------------------
        8:[148.405177,-231.475974,263.305593],
        9:[-121.15655,-329.37685,-197.06224],
        10:[-28.800063,-420.849441,-43.564604],
        11:[-180.112865,-190.297251,-301.062917],
        #--------------------------------------------------------
        12:[161.032208592, 207.530151484, 286.703007713],
        13:[-79.830818,266.416356,-122.828467],
        14:[90.491568,406.666552,171.303074],
        15:[136.833937217,-349.10409, 256.16691],
        #========================================================
	    16:[75.008275,-366.663944,135.807286],
        17:[-170.082246,113.392564,-280.090332],
        18:[-173.308984588, -52.5844630491, -289.495946419],
        19:[35.6156894023, -76.4247822222, 68.8003235664],
        #-------------------------------------------------------
        20:[ 223.405495506, -111.371927382, 391.352958368],
        21:[ 211.984088554, -181.820834933, 372.672243377],
        22:[-52.9274701935, -409.284993158, -84.1268196632],
        23:[-75.327786,379.129646,-113.829018],
        #--------------------------------------------------------
        24:[-90.374808,3.548977,-144.207995],
        25:[-23.653561,-153.921245,-31.289596],
        26:[208.418197,189.287085,370.725255],
        27:[-22.2282015089, 311.926612877, -26.8228657991],
        #--------------------------------------------------------
        28:[-18.1453146192, 166.083642242, -21.2052534495],
        29:[89.6597220746, -22.1294190136, 162.698139384],
        30:[-139.053365,312.917932,-223.870462],
        31:[229.945829,48.161862,406.414507],
        #--------------------------------------------------------
        32:[-112.893563,109.228967,-182.880941],
        33:[121.355347,-319.429590,209.575748],
        34:[-1.186004,298.790781,-1.572735],
        35:[-150.754218,-224.460782,-258.594058],
        #--------------------------------------------------------
        36:[-148.166345,285.390149,-254.152706],
        37:[73.704070,-378.161280,127.753480],
        38:[183.238623,145.046381,314.997386],
        39:[201.110057,270.608943,345.388038],
        #--------------------------------------------------------
        40:[-187.753175,101.634584,-322.330703],
        41:[32.859445,-311.361270,57.492402],
        42:[111.791791,-360.752264,193.124569],
        43:[185.296482,12.473870,318.948404],
        #--------------------------------------------------------
        44:[66.840886,269.989165,115.139909],
        45:[208.327549,-181.024029,358.713760],
        46:[222.401981,114.559981,382.329808],
        47:[82.998742,-157.005822,143.375763],
        #-------------------------------------------------------
        48:[-123.364050,7.568406,-211.391982],
        49:[42.324815,-394.596554,73.800150],
        50:[155.428104,103.981800,267.545140],
        51:[4.002712,454.858259,7.086482],
        #-------------------------------------------------------
        52:[40.840441,382.998141,70.689703],
        53:[228.948582,78.038958,393.662509],
        54:[208.232148,171.396294,357.761446],
        55:[22.162702,221.120016,38.449461],
        #--------------------------------------------------------
        56:[-85.962903,360.456826,-147.018238],
        57:[-22.182170,447.517664,-37.585541],
        58:[-40.132905,-349.207661,-68.174661],
        59:[-38.864384,362.866457,-66.270033],
        #--------------------------------------------------------
        60:[134.062901,401.074665,230.468279],
        61:[-81.496611,-277.174777,-139.301327],
        62:[-161.608043,226.512058,-277.243397],
        63:[170.275635,-299.764724,293.554481],
    }, 
    'dpos':{
        },
    'delays': {
	 0 : {'x':-0.323347002962, 'y': 0.514709128944}, 
     1 : {'x':-0.435716868684, 'y': -3.05313559537},  
     2 : {'x': -6.72889198357, 'y': -9.77206692449},  
     3 : {'x':-0.655692883541, 'y': -3.39131642022}, 
     4 : {'x': -9.66844585543, 'y':  -16.045239594},  
     5 : {'x':  5.45022969862, 'y':  1.62705345891}, 
     6 : {'x': -10.5168712615, 'y': -17.3611879177}, 
     7 : {'x':  3.32820389355, 'y': 0.714899827941}, 
     8 : {'x': -8.50134340321, 'y': -11.8816414268},  
     9 : {'x':0.0541678187689, 'y':  0.19211313648},
    10 : {'x': -14.2915049516, 'y': -17.0331953219},
    11 : {'x': -7.88871275196, 'y': -11.6261499614},
    12 : {'x':  1.56814805445, 'y': -2.55324568351}, 
    13 : {'x': -13.3159835651, 'y':  -16.136696721},
    14 : {'x': -8.74743145547, 'y': -16.7388911247},
    15 : {'x':  2.57737106347, 'y': 0.440575176979},
    16 : {'x':  14.8127174377, 'y':  12.0820184423},
    17 : {'x':-0.347368240356, 'y': 0.709252294336},
    18 : {'x': -1.81631383052, 'y':             0.}, 
    19 : {'x':             0., 'y': -2.72708338361}, 
    20 : {'x':  0.59043549604, 'y': -2.60521559533}, 
    21 : {'x':-0.346789237918, 'y': -2.97456770209},
    22 : {'x':  3.19651892237, 'y': -1.95158891802}, 
    23 : {'x': -12.4464112872, 'y': -14.7304249398},
    25 : {'x':  -16.536067567, 'y':  -21.874137694},
    26 : {'x': -10.3255433007, 'y': -16.3115326254},
    27 : {'x':   3.3031259953, 'y':  -4.6218641885},
    28 : {'x':  3.21017690925, 'y':-0.813489753942},
    29 : {'x':  6.27235336236, 'y':-0.724582381456},
    30 : {'x': -0.47391921657, 'y': -4.19526492031},
    31 : {'x': -13.6543355382, 'y': -15.6246143921},
    63 : {'x':-0.457457485972, 'y':-0.313338617724},
    },
    'amps': {
     0 : {'x': 13.9014459211, 'y': 15.1691865934}, 
     1 : {'x': 16.2087777648, 'y': 15.9409134791}, 
     2 : {'x':  14.686783514, 'y': 15.5884745646}, 
     3 : {'x': 16.7294575414, 'y': 16.7948107221}, 
     4 : {'x': 15.6230095001, 'y': 14.6659258529}, 
     5 : {'x': 17.0217217395, 'y': 15.4734378873},
     6 : {'x': 14.3237729886, 'y': 12.9963900087}, 
     7 : {'x': 14.0362800059, 'y': 11.3835125661}, 
     8 : {'x': 15.0851448384, 'y': 15.3055918971}, 
     9 : {'x':  14.061393096, 'y': 15.1892977077},
    10 : {'x': 12.9857412167, 'y': 13.8896536396}, 
    11 : {'x': 14.9648254516, 'y': 15.3516799822}, 
    12 : {'x': 18.2935339965, 'y': 19.0222835776}, 
    13 : {'x': 14.4216703969, 'y': 14.3496970969}, 
    14 : {'x': 15.2432016466, 'y': 13.6660666837}, 
    15 : {'x': 16.0108854364, 'y':  16.571653689}, 
    16 : {'x': 14.9117284897, 'y': 15.4916861335},
    17 : {'x':  14.960952262, 'y': 15.3829545612}, 
    18 : {'x': 18.0715553865, 'y':            0.},  
    19 : {'x':            0., 'y': 14.8799557719},  
    20 : {'x': 16.0830459234, 'y': 14.3451228941}, 
    21 : {'x': 16.4103444781, 'y': 14.5627406348}, 
    22 : {'x':  14.753471386, 'y': 15.8487603595},  
    23 : {'x': 14.0561280189, 'y': 10.4362337049}, 
    25 : {'x': 15.5554525212, 'y': 15.5793187455}, 
    26 : {'x':  12.869695577, 'y':   13.97863668}, 
    27 : {'x': 10.2439567268, 'y': 12.1482563898}, 
    28 : {'x': 17.2676518038, 'y': 16.2081265491}, 
    29 : {'x': 15.9099292161, 'y': 15.8966826809}, 
    30 : {'x':  14.154182691, 'y': 15.2077579135}, 
    31 : {'x': 15.3787864425, 'y': 15.1260803772}, 
    63 : {'x': 12.9251949593, 'y': 16.5897323407},
    },
    'off':{
        },
    'bp_r':  n.array([-167333390752.98276, 198581623581.65594, -102487141227.4993, 30027423590.548084, -5459067124.669095, 630132740.98792362, -45056600.848056234, 1822654.0034047314, -31892.9279846797]) * 1.0178**0.5,
    '32_64_pos_offset': n.array([-13.44311,-21.21483,-2.31634])
}

def get_aa(freqs):
    '''Return the AntennaArray to be used for simulation.'''
    location = prms['loc']
    antennas = []
    nants = len(prms['antpos'])
    for pi in ('x','y'):
        for i in prms['antpos'].keys():
            beam = bm.prms['beam'](freqs,nside=32,lmax=20,mmax=20,deg=7)
            try: beam.set_params(bm.prms['bm_prms'])
            except(AttributeError): pass
            pos = prms['antpos'][i]
            if i > 31: pos += prms['32_64_pos_offset'] 
            try: dly = prms['delays'][i][pi]
            except(KeyError): dly = 0.
            try: off = prms['off'][i][pi]
            except(KeyError): off = 0.
            bp_r = prms['bp_r']
            try: amp = prms['amps'][i][pi]
            except(KeyError): amp = 1.
            try: dpos = prms['dpos'][i]
            except(KeyError): dpos = n.array([0.,0.,0.,])
            antennas.append(
                Antenna(pos[0],pos[1],pos[2], beam, dpos=dpos, num=i, pol=pi, phsoff=[dly,off], amp=amp, bp_r = bp_r, lat=prms['loc'][0] )
                )
    aa = a.pol.AntennaArray(prms['loc'], antennas)
    return aa

src_prms = {
    'pic' :{'jys':600.,'ra':'5:19:49.70','dec':'-45:46.45.0','mfreq':0.150,'index':-1.},#NVSS positions 
    'forA':{'jys':210.,'ra':'3:22:41.7','dec':'-37:12:30','mfreq':0.150,'index':-1.},   #NVSS positions 
    'forB':{'jys': 96.,'ra':'3:23:19.3','dec':'-37:10:58','mfreq':0.150,'index':-1.},   #NVSS positions 
    'J0445-23':{'jys':174.,'ra':'4:45:43','dec':'-28:05:56','mfreq':0.150,'index':-1.},
    'J0522-36':{'jys':96.,'ra':'5:23:43','dec':'-36:22:48','mfreq':0.150,'index':-1.},
    'J0625-53':{'jys':60.,'ra':'6:25:11','dec':'-53:39:31','mfreq':0.150,'index':-1.},
}

def get_catalog(srcs=None, cutoff=None, catalogs=['helm','misc']):
    '''Return a catalog containing the listed sources.'''
    log.info("psa743_v002_gc")
    specials = ['pic','forA','forB','J0445-23','J0522-36','J0625-53']
    srclist =[]
    for c in catalogs:     
        log.info("looking for %s in a local file"%(c,))
        this_srcs = generic_catalog.get_srcs(srcs=srcs,
              cutoff=cutoff,catalogs=[c])
        if len(this_srcs)==0:
            log.warning("no sources found with genericfile, trying built in catalog")
            tcat = a.src.get_catalog(srcs=srcs, 
                   cutoff=cutoff, catalogs=[c])
            srclist += [tcat[src] for src in tcat]
        else: srclist += this_srcs
    cat = a.fit.SrcCatalog(srclist)
    #Add specials.  All fixed radio sources must be in catalog, for completeness
    if not srcs is None:
        for src in srcs:
            if src in src_prms.keys():
                if src in specials:
                    cat[src] = a.fit.RadioFixedBody(**src_prms[src])
    return cat

if __name__=='__main__':
    import sys, numpy as n
    if len(sys.argv)>1:
        print "loading catalog: ",sys.argv[1]
        logging.basicConfig(level=logging.DEBUG)
        cat = get_catalog(catalogs=[sys.argv[1]])
        names = [cat[src].src_name for src in cat]
        print "loaded",len(names)," sources"
        flx = [cat[src]._jys for src in cat]
        print names
        print "brightest source in catalog"
        print names[flx.index(n.max(flx))],n.max(flx)
        log.info("loaded %d items from %s"%(len(cat),sys.argv[1]))
        try: assert([cat[src].e_S_nu for src in cat])
        except(AttributeError): print "this catalog does not have flux errors"
