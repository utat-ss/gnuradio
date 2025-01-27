#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Dec 29 14:16:00 2018
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import math
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.lowpass2 = lowpass2 = 10e3
        self.lowpass = lowpass = 10e3
        self.base = base = "/home/ali/Documents/UTAT/GNURadio/2018-12-28/es_pipe_U@?U@?U@?"
        self.samp_rate = samp_rate = 4003200
        self.filename_2_0 = filename_2_0 = base+"_mmclock"
        self.filename_2 = filename_2 = base+"_bits"
        self.filename_1 = filename_1 = base+"_quaddemod_lpf_"+str((lowpass/1000.0))+"lpf2_"+str((lowpass2/1000.0))
        self.filename_0 = filename_0 = base+"_quaddemod_lpf_"+str((lowpass/1000.0))
        self.filename = filename = base+"_lpf_"+str((lowpass/1000.0))

        ##################################################
        # Blocks
        ##################################################
        self.low_pass_filter_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, lowpass2, lowpass2, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, lowpass, lowpass/3, firdes.WIN_HAMMING, 6.76))
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(417*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, base, False)
        self.blocks_file_sink_0_2 = blocks.file_sink(gr.sizeof_float*1, filename_2_0, False)
        self.blocks_file_sink_0_2.set_unbuffered(False)
        self.blocks_file_sink_0_1_0 = blocks.file_sink(gr.sizeof_char*1, filename_2, False)
        self.blocks_file_sink_0_1_0.set_unbuffered(False)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-15, ))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1e6, 1, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(2123.8262)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.blocks_file_sink_0_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.blocks_file_sink_0_2, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_add_const_vxx_0, 0))

    def get_lowpass2(self):
        return self.lowpass2

    def set_lowpass2(self, lowpass2):
        self.lowpass2 = lowpass2
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.lowpass2, self.lowpass2, firdes.WIN_HAMMING, 6.76))
        self.set_filename_1(self.base+"_quaddemod_lpf_"+str((self.lowpass/1000.0))+"lpf2_"+str((self.lowpass2/1000.0)))

    def get_lowpass(self):
        return self.lowpass

    def set_lowpass(self, lowpass):
        self.lowpass = lowpass
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lowpass, self.lowpass/3, firdes.WIN_HAMMING, 6.76))
        self.set_filename_1(self.base+"_quaddemod_lpf_"+str((self.lowpass/1000.0))+"lpf2_"+str((self.lowpass2/1000.0)))
        self.set_filename_0(self.base+"_quaddemod_lpf_"+str((self.lowpass/1000.0)))
        self.set_filename(self.base+"_lpf_"+str((self.lowpass/1000.0)))

    def get_base(self):
        return self.base

    def set_base(self, base):
        self.base = base
        self.set_filename_2_0(self.base+"_mmclock")
        self.set_filename_2(self.base+"_bits")
        self.set_filename_1(self.base+"_quaddemod_lpf_"+str((self.lowpass/1000.0))+"lpf2_"+str((self.lowpass2/1000.0)))
        self.set_filename_0(self.base+"_quaddemod_lpf_"+str((self.lowpass/1000.0)))
        self.set_filename(self.base+"_lpf_"+str((self.lowpass/1000.0)))
        self.blocks_file_source_0.open(self.base, False)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.lowpass2, self.lowpass2, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lowpass, self.lowpass/3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_filename_2_0(self):
        return self.filename_2_0

    def set_filename_2_0(self, filename_2_0):
        self.filename_2_0 = filename_2_0
        self.blocks_file_sink_0_2.open(self.filename_2_0)

    def get_filename_2(self):
        return self.filename_2

    def set_filename_2(self, filename_2):
        self.filename_2 = filename_2
        self.blocks_file_sink_0_1_0.open(self.filename_2)

    def get_filename_1(self):
        return self.filename_1

    def set_filename_1(self, filename_1):
        self.filename_1 = filename_1

    def get_filename_0(self):
        return self.filename_0

    def set_filename_0(self, filename_0):
        self.filename_0 = filename_0

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
