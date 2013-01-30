"""
Module used to take a wav file and import it into an array
"""
import wave
import struct


class LoadWav:
    """
    Class used to take a wav file and import it into an array
    """

    def __init__(self, input_file):
        self.wav_obj = wave.open(input_file)
        self.num_channels = self.wav_obj.getnchannels()
        self.sample_width = self.wav_obj.getsampwidth()
        self.sample_rate = self.wav_obj.getframerate()
        self.num_frames = self.wav_obj.getnframes()
        self._struct_format = ""
        self.channel_list = []

        for i in range(self.num_channels):
            self.channel_list.append([])

        if self.sample_width == 1:
            self._struct_format = "<b"
        elif self.sample_width == 2:
            self._struct_format = "<h"
        else:
            self._struct_format = "<i"

        chan_list = range(self.num_channels)
        for i in xrange(self.num_frames):
            frame = self.wav_obj.readframes(1)
            for i in chan_list:
                sub_block = frame[i*self.sample_width:(i+1)*self.sample_width]
                self.channel_list[i].append(struct.unpack(self._struct_format, sub_block)[0])


