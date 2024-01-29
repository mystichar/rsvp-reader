#./gui.py
import tkinter as tki
from tkinter.font import Font
from wordfeed import WordFeed
from settings import RSVP_FONT_DICT, RSVP_SHAPE, WPM
from sys import platform

master = tki.Tk()

example_string = '''Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door—
            Only this and nothing more.”

    Ah, distinctly I remember it was in the bleak December;
And each separate dying ember wrought its ghost upon the floor.
    Eagerly I wished the morrow;—vainly I had sought to borrow
    From my books surcease of sorrow—sorrow for the lost Lenore—
For the rare and radiant maiden whom the angels name Lenore—
            Nameless here for evermore.

    And the silken, sad, uncertain rustling of each purple curtain
Thrilled me—filled me with fantastic terrors never felt before;
    So that now, to still the beating of my heart, I stood repeating
    “’Tis some visitor entreating entrance at my chamber door—
Some late visitor entreating entrance at my chamber door;—
            This it is and nothing more.”

    Presently my soul grew stronger; hesitating then no longer,
“Sir,” said I, “or Madam, truly your forgiveness I implore;
    But the fact is I was napping, and so gently you came rapping,
    And so faintly you came tapping, tapping at my chamber door,
That I scarce was sure I heard you”—here I opened wide the door;—
            Darkness there and nothing more.

    Deep into that darkness peering, long I stood there wondering, fearing,
Doubting, dreaming dreams no mortal ever dared to dream before;
    But the silence was unbroken, and the stillness gave no token,
    And the only word there spoken was the whispered word, “Lenore?”
This I whispered, and an echo murmured back the word, “Lenore!”—
            Merely this and nothing more.

    Back into the chamber turning, all my soul within me burning,
Soon again I heard a tapping somewhat louder than before.
    “Surely,” said I, “surely that is something at my window lattice;
      Let me see, then, what thereat is, and this mystery explore—
Let my heart be still a moment and this mystery explore;—
            ’Tis the wind and nothing more!”

    Open here I flung the shutter, when, with many a flirt and flutter,
In there stepped a stately Raven of the saintly days of yore;
    Not the least obeisance made he; not a minute stopped or stayed he;
    But, with mien of lord or lady, perched above my chamber door—
Perched upon a bust of Pallas just above my chamber door—
            Perched, and sat, and nothing more.

Then this ebony bird beguiling my sad fancy into smiling,
By the grave and stern decorum of the countenance it wore,
“Though thy crest be shorn and shaven, thou,” I said, “art sure no craven,
Ghastly grim and ancient Raven wandering from the Nightly shore—
Tell me what thy lordly name is on the Night’s Plutonian shore!”
            Quoth the Raven “Nevermore.”

    Much I marvelled this ungainly fowl to hear discourse so plainly,
Though its answer little meaning—little relevancy bore;
    For we cannot help agreeing that no living human being
    Ever yet was blessed with seeing bird above his chamber door—
Bird or beast upon the sculptured bust above his chamber door,
            With such name as “Nevermore.”

    But the Raven, sitting lonely on the placid bust, spoke only
That one word, as if his soul in that one word he did outpour.
    Nothing farther then he uttered—not a feather then he fluttered—
    Till I scarcely more than muttered “Other friends have flown before—
On the morrow he will leave me, as my Hopes have flown before.”
            Then the bird said “Nevermore.”

    Startled at the stillness broken by reply so aptly spoken,
“Doubtless,” said I, “what it utters is its only stock and store
    Caught from some unhappy master whom unmerciful Disaster
    Followed fast and followed faster till his songs one burden bore—
Till the dirges of his Hope that melancholy burden bore
            Of ‘Never—nevermore’.”

    But the Raven still beguiling all my fancy into smiling,
Straight I wheeled a cushioned seat in front of bird, and bust and door;
    Then, upon the velvet sinking, I betook myself to linking
    Fancy unto fancy, thinking what this ominous bird of yore—
What this grim, ungainly, ghastly, gaunt, and ominous bird of yore
            Meant in croaking “Nevermore.”

    This I sat engaged in guessing, but no syllable expressing
To the fowl whose fiery eyes now burned into my bosom’s core;
    This and more I sat divining, with my head at ease reclining
    On the cushion’s velvet lining that the lamp-light gloated o’er,
But whose velvet-violet lining with the lamp-light gloating o’er,
            She shall press, ah, nevermore!

    Then, methought, the air grew denser, perfumed from an unseen censer
Swung by Seraphim whose foot-falls tinkled on the tufted floor.
    “Wretch,” I cried, “thy God hath lent thee—by these angels he hath sent thee
    Respite—respite and nepenthe from thy memories of Lenore;
Quaff, oh quaff this kind nepenthe and forget this lost Lenore!”
            Quoth the Raven “Nevermore.”

    “Prophet!” said I, “thing of evil!—prophet still, if bird or devil!—
Whether Tempter sent, or whether tempest tossed thee here ashore,
    Desolate yet all undaunted, on this desert land enchanted—
    On this home by Horror haunted—tell me truly, I implore—
Is there—is there balm in Gilead?—tell me—tell me, I implore!”
            Quoth the Raven “Nevermore.”

    “Prophet!” said I, “thing of evil!—prophet still, if bird or devil!
By that Heaven that bends above us—by that God we both adore—
    Tell this soul with sorrow laden if, within the distant Aidenn,
    It shall clasp a sainted maiden whom the angels name Lenore—
Clasp a rare and radiant maiden whom the angels name Lenore.”
            Quoth the Raven “Nevermore.”

    “Be that word our sign of parting, bird or fiend!” I shrieked, upstarting—
“Get thee back into the tempest and the Night’s Plutonian shore!
    Leave no black plume as a token of that lie thy soul hath spoken!
    Leave my loneliness unbroken!—quit the bust above my door!
Take thy beak from out my heart, and take thy form from off my door!”
            Quoth the Raven “Nevermore.”

    And the Raven, never flitting, still is sitting, still is sitting
On the pallid bust of Pallas just above my chamber door;
    And his eyes have all the seeming of a demon’s that is dreaming,
    And the lamp-light o’er him streaming throws his shadow on the floor;
And my soul from out that shadow that lies floating on the floor
            Shall be lifted—nevermore!'''

class Gui(object):

    def __init__(self):
        self.master = master
        self._pause_flag = True
        # ...
        self.input_frame = InputFrame(self.master, self)
        self.input_frame.pack(side=tki.TOP)
        self.rsvp_frame = RsvpFrame(self.master, self)
        self.rsvp_frame.pack(side=tki.TOP)
        self.control_frame = ControlFrame(self.master, self)
        self.control_frame.pack(side=tki.TOP)
        self.rate_string = rs = tki.StringVar()
        self.rate_label = tki.Label(self.master, textvariable=rs)
        self.rate_label.pack(side=tki.TOP)
        self.speed_slider = tki.Scale(self.master, from_=100, to=1000, orient=tki.HORIZONTAL, label="Speed (WPM)", command=self.on_speed_change)
        self.speed_slider.set(WPM)  # Set initial value
        self.speed_slider.pack(side=tki.LEFT)
        # ...
        self.master.bind('<Escape>', lambda e: self.master.destroy())
        self.master.resizable(False, False)
        # ...
        self.wordfeed = None
        self.update_wordfeed()
        # ...
        self.apply_settings()
        # ...
        # Speed control slider

    def apply_settings(self):
        pass

    def export_settings(self, path):
        pass

    def update_wordfeed(self, name=None, index=None, mode=None):
        inext = self.wordfeed.inext if self.wordfeed else 0
        text = self.input_frame.entry.get()
        self.wordfeed = WordFeed(text, inext)
        self.rsvp_frame.update()
        self.update_rate()

    def update_rate(self):
        num_words, total_minutes = self.wordfeed.get_statistics()
        if num_words < 1:
            return
        stat_format = '{0} words in {1:.2f} minutes = {2} WPM.'
        self.rate_string.set(stat_format.format(
            num_words,
            total_minutes,
            int(num_words / total_minutes)))

    def update_wpm(self, new_wpm):
        global WPM
        WPM = new_wpm
        print('WPM = {0}'.format(WPM))
        self.update_wordfeed()
        self.update_rate()
        
    def on_speed_change(self, value):
        self.update_wpm(int(value))

    def update_rsvp(self):
        text, delay_ms = self.wordfeed.next()
        if text == None:
            self.pause()
        else:
            self.rsvp_frame.display_text(text)
        return delay_ms

    def rsvp_kernel(self):
        if self._pause_flag:
            return
        delay_ms = self.update_rsvp()
        if delay_ms:
            self.master.after(delay_ms, self.rsvp_kernel)

    def pause_resume(self, event=None):
        if self._pause_flag: self.resume()
        else: self.pause()

    def pause(self, event=None):
        self._pause_flag = True
        print('pause')

    def resume(self, event=None):
        self._pause_flag = False
        print('resume')
        self.rsvp_kernel()

    def back10(self, event=None):
        print('back 10')
        self.wordfeed.inext -= 10
        self.update_rsvp()

    def back50(self, event=None):
        print('back 50')
        self.wordfeed.inext -= 50
        self.update_rsvp()


class InputFrame(tki.Frame):
    def __init__(self, master, gui):
        tki.Frame.__init__(self, master)
        self.gui = gui
        self.inputvar = tki.StringVar(value=example_string)
        self.inputvar.trace('w', lambda name, index, mode: self.gui.update_wordfeed())
        self.entry = tki.Entry(self, textvariable=self.inputvar, width=50)
        self.entry.pack()
        sel_all_cmd = '<Command-a>' if platform == 'darwin' else '<Control-a>'
        self.entry.bind(sel_all_cmd, self.select_all)

    def select_all(self, event=None):
        self.entry.selection_range(0, tki.END)
        return 'break'


class RsvpFrame(tki.Frame):
    def __init__(self, master, gui):
        tki.Frame.__init__(self, master)
        self.gui = gui
        self.font = Font(**RSVP_FONT_DICT)
        self.shape = width,height = RSVP_SHAPE
        self.text_id = None
        c = self.canvas = tki.Canvas(self, width=width, height=height)
        c.pack()
        c.bind('<Button-1>', self.gui.pause_resume)
        self.clear_canvas()

    def display_text(self, text):
        width, height = self.shape
        if self.text_id != None:
            self.canvas.delete(self.text_id)
            self.text_id = None
        self.text_id = self.canvas.create_text(
            (width/2, height/2),
            text=text,
            font=self.font)

    def clear_canvas(self):
        self.canvas.delete()
        self.canvas.create_rectangle(0,0,*self.shape,fill='white')


class ControlFrame(tki.Frame):
    def __init__(self, master, gui):
        tki.Frame.__init__(self, master)
        self.gui = gui
        #
        b = self.pause_button = tki.Button(
            self,
            text='PP',
            command=gui.pause_resume)
        b.pack(side=tki.LEFT)
        #
        b = self.back10_button = tki.Button(
            self,
            text='< 10',
            command=gui.back10)
        b.pack(side=tki.LEFT)
        #
        b = self.back50_button = tki.Button(
            self,
            text='< 50',
            command=gui.back50)
        b.pack(side=tki.LEFT)
