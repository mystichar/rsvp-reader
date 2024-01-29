from settings import FREQUENCY_DELAY
from os.path import dirname, join

class FrequencyDict(object):
    def __init__(self, csv_path):
        self.fd = {}
        with open(csv_path, encoding='utf-8') as csv_file:  # Added UTF-8 encoding for compatibility
            rank = 0
            for line in csv_file:
                if '\t' not in line:
                    continue
                rank += 1
                split = line.strip().split('\t')  # Strip newline characters
                word = split[0]
                freq = int(split[1])
                self.fd[word] = (freq, rank)
        self.min_freq = min(self.fd.values(), default=(0,0))  # Changed from itervalues() and added default
        self.max_freq = max(self.fd.values(), default=(0,0))  # Added default value

    def get_delay_words(self, text):
        freq, rank = self.fd.get(text, (0, len(self.fd)))
        return FREQUENCY_DELAY(freq, rank, self.min_freq, self.max_freq)

try:
    from __main__ import __file__ as main_path
except ImportError:
    main_path = None
    csv_path = None
    FREQ_DICT = None
else:
    csv_path = join(dirname(main_path), 'frequent-words.csv')
    FREQ_DICT = FrequencyDict(csv_path)

if __name__ == '__main__':
    FREQ_DICT = FrequencyDict('frequent-words.csv')
