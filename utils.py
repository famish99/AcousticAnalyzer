"""
Utilities Module
"""

def downsample(array, factor, sample_rate):
    """
    Return a time axis array and a downsampled signal array

    @param factor: Positive integer downsampling factor, aka array stride amount
    """
    t = [ x * 1.0 * factor/sample_rate for x in xrange(len(array)/512+1) ]
    return (t, array[::factor])
