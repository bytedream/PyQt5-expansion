from PyQt5 import QtGui, QtCore, QtWidgets
import typing


class QEmojiPicker(QtWidgets.QDialog):
    """A simple emoji picker"""

    def __init__(self, parent: QtWidgets = None, flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = None, items_per_row=8, performance_search=True):
        """
        Args:
            parent: The parent window
            flags: Qt flags
            items_per_row: How many items per row should be displayed
            performance_search: If True, the search input will display the emojis faster. See `self.on_input(...)` for more details
        """
        if flags:
            super().__init__(parent, flags)
        else:
            super().__init__(parent)
        # initializes the ui
        self.setupUi(self)
        self.retranslateUi(self)

        self.items_per_row = items_per_row
        self.performance_search = performance_search

        self.selected_emoji = None

        # connects `self.on_input(...)` whenever the search input text is changed
        self.search_line_edit.textChanged.connect(self.on_input)

        # the emojis. a pretty long dict...
        self.emojis = {
            'Smileys & People': {
                "😀": "Grinning Face",
                "😃": "Grinning Face with Big Eyes",
                "😄": "Grinning Face with Smiling Eyes",
                "😁": "Beaming Face with Smiling Eyes",
                "😆": "Grinning Squinting Face",
                "😅": "Grinning Face with Sweat",
                "🤣": "Rolling on the Floor Laughing",
                "😂": "Face with Tears of Joy",
                "🙂": "Slightly Smiling Face",
                "🙃": "Upside-Down Face",
                "😉": "Winking Face",
                "😊": "Smiling Face with Smiling Eyes",
                "😇": "Smiling Face with Halo",
                "🥰": "Smiling Face with Hearts",
                "😍": "Smiling Face with Heart-Eyes",
                "🤩": "Star-Struck",
                "😘": "Face Blowing a Kiss",
                "😗": "Kissing Face",
                "☺️": "Smiling Face",
                "😚": "Kissing Face with Closed Eyes",
                "😙": "Kissing Face with Smiling Eyes",
                "🥲": "Smiling Face with Tear",
                "😋": "Face Savoring Food",
                "😛": "Face with Tongue",
                "😜": "Winking Face with Tongue",
                "🤪": "Zany Face",
                "😝": "Squinting Face with Tongue",
                "🤑": "Money-Mouth Face",
                "🤗": "Hugging Face",
                "🤭": "Face with Hand Over Mouth",
                "🤫": "Shushing Face",
                "🤔": "Thinking Face",
                "🤐": "Zipper-Mouth Face",
                "🤨": "Face with Raised Eyebrow",
                "😐": "Neutral Face",
                "😑": "Expressionless Face",
                "😶": "Face Without Mouth",
                "😏": "Smirking Face",
                "😒": "Unamused Face",
                "🙄": "Face with Rolling Eyes",
                "😬": "Grimacing Face",
                "🤥": "Lying Face",
                "😌": "Relieved Face",
                "😔": "Pensive Face",
                "😪": "Sleepy Face",
                "🤤": "Drooling Face",
                "😴": "Sleeping Face",
                "😷": "Face with Medical Mask",
                "🤒": "Face with Thermometer",
                "🤕": "Face with Head-Bandage",
                "🤢": "Nauseated Face",
                "🤮": "Face Vomiting",
                "🤧": "Sneezing Face",
                "🥵": "Hot Face",
                "🥶": "Cold Face",
                "🥴": "Woozy Face",
                "😵": "Dizzy Face",
                "🤯": "Exploding Head",
                "🤠": "Cowboy Hat Face",
                "🥳": "Partying Face",
                "🥸": "Disguised Face",
                "😎": "Smiling Face with Sunglasses",
                "🤓": "Nerd Face",
                "🧐": "Face with Monocle",
                "😕": "Confused Face",
                "😟": "Worried Face",
                "🙁": "Slightly Frowning Face",
                "☹️": "Frowning Face",
                "😮": "Face with Open Mouth",
                "😯": "Hushed Face",
                "😲": "Astonished Face",
                "😳": "Flushed Face",
                "🥺": "Pleading Face",
                "😦": "Frowning Face with Open Mouth",
                "😧": "Anguished Face",
                "😨": "Fearful Face",
                "😰": "Anxious Face with Sweat",
                "😥": "Sad but Relieved Face",
                "😢": "Crying Face",
                "😭": "Loudly Crying Face",
                "😱": "Face Screaming in Fear",
                "😖": "Confounded Face",
                "😣": "Persevering Face",
                "😞": "Disappointed Face",
                "😓": "Downcast Face with Sweat",
                "😩": "Weary Face",
                "😫": "Tired Face",
                "🥱": "Yawning Face",
                "😤": "Face with Steam From Nose",
                "😡": "Pouting Face",
                "😠": "Angry Face",
                "🤬": "Face with Symbols on Mouth",
                "😈": "Smiling Face with Horns",
                "👿": "Angry Face with Horns",
                "💀": "Skull",
                "☠️": "Skull and Crossbones",
                "💩": "Pile of Poo",
                "🤡": "Clown Face",
                "👹": "Ogre",
                "👺": "Goblin",
                "👻": "Ghost",
                "👽": "Alien",
                "👾": "Alien Monster",
                "🤖": "Robot",
                "😺": "Grinning Cat",
                "😸": "Grinning Cat with Smiling Eyes",
                "😹": "Cat with Tears of Joy",
                "😻": "Smiling Cat with Heart-Eyes",
                "😼": "Cat with Wry Smile",
                "😽": "Kissing Cat",
                "🙀": "Weary Cat",
                "😿": "Crying Cat",
                "😾": "Pouting Cat",
                "💋": "Kiss Mark",
                "👋": "Waving Hand",
                "🤚": "Raised Back of Hand",
                "🖐️": "Hand with Fingers Splayed",
                "✋": "Raised Hand",
                "🖖": "Vulcan Salute",
                "👌": "OK Hand",
                "🤌": "Pinched Fingers",
                "🤏": "Pinching Hand",
                "✌️": "Victory Hand",
                "🤞": "Crossed Fingers",
                "🤟": "Love-You Gesture",
                "🤘": "Sign of the Horns",
                "🤙": "Call Me Hand",
                "👈": "Backhand Index Pointing Left",
                "👉": "Backhand Index Pointing Right",
                "👆": "Backhand Index Pointing Up",
                "🖕": "Middle Finger",
                "👇": "Backhand Index Pointing Down",
                "☝️": "Index Pointing Up",
                "👍": "Thumbs Up",
                "👎": "Thumbs Down",
                "✊": "Raised Fist",
                "👊": "Oncoming Fist",
                "🤛": "Left-Facing Fist",
                "🤜": "Right-Facing Fist",
                "👏": "Clapping Hands",
                "🙌": "Raising Hands",
                "👐": "Open Hands",
                "🤲": "Palms Up Together",
                "🤝": "Handshake",
                "🙏": "Folded Hands",
                "✍️": "Writing Hand",
                "💅": "Nail Polish",
                "🤳": "Selfie",
                "💪": "Flexed Biceps",
                "🦾": "Mechanical Arm",
                "🦿": "Mechanical Leg",
                "🦵": "Leg",
                "🦶": "Foot",
                "👂": "Ear",
                "🦻": "Ear with Hearing Aid",
                "👃": "Nose",
                "🧠": "Brain",
                "🫀": "Anatomical Heart",
                "🫁": "Lungs",
                "🦷": "Tooth",
                "🦴": "Bone",
                "👀": "Eyes",
                "👁️": "Eye",
                "👅": "Tongue",
                "👄": "Mouth",
                "👶": "Baby",
                "🧒": "Child",
                "👦": "Boy",
                "👧": "Girl",
                "🧑": "Person",
                "👱": "Person: Blond Hair",
                "👨": "Man",
                "🧔": "Person: Beard",
                "👨‍🦰": "Man: Red Hair",
                "👨‍🦱": "Man: Curly Hair",
                "👨‍🦳": "Man: White Hair",
                "👨‍🦲": "Man: Bald",
                "👩": "Woman",
                "👩‍🦰": "Woman: Red Hair",
                "🧑‍🦰": "Person: Red Hair",
                "👩‍🦱": "Woman: Curly Hair",
                "🧑‍🦱": "Person: Curly Hair",
                "👩‍🦳": "Woman: White Hair",
                "🧑‍🦳": "Person: White Hair",
                "👩‍🦲": "Woman: Bald",
                "🧑‍🦲": "Person: Bald",
                "👱‍♀️": "Woman: Blond Hair",
                "👱‍♂️": "Man: Blond Hair",
                "🧓": "Older Person",
                "👴": "Old Man",
                "👵": "Old Woman",
                "🙍": "Person Frowning",
                "🙍‍♂️": "Man Frowning",
                "🙍‍♀️": "Woman Frowning",
                "🙎": "Person Pouting",
                "🙎‍♂️": "Man Pouting",
                "🙎‍♀️": "Woman Pouting",
                "🙅": "Person Gesturing No",
                "🙅‍♂️": "Man Gesturing No",
                "🙅‍♀️": "Woman Gesturing No",
                "🙆": "Person Gesturing OK",
                "🙆‍♂️": "Man Gesturing OK",
                "🙆‍♀️": "Woman Gesturing OK",
                "💁": "Person Tipping Hand",
                "💁‍♂️": "Man Tipping Hand",
                "💁‍♀️": "Woman Tipping Hand",
                "🙋": "Person Raising Hand",
                "🙋‍♂️": "Man Raising Hand",
                "🙋‍♀️": "Woman Raising Hand",
                "🧏": "Deaf Person",
                "🧏‍♂️": "Deaf Man",
                "🧏‍♀️": "Deaf Woman",
                "🙇": "Person Bowing",
                "🙇‍♂️": "Man Bowing",
                "🙇‍♀️": "Woman Bowing",
                "🤦": "Person Facepalming",
                "🤦‍♂️": "Man Facepalming",
                "🤦‍♀️": "Woman Facepalming",
                "🤷": "Person Shrugging",
                "🤷‍♂️": "Man Shrugging",
                "🤷‍♀️": "Woman Shrugging",
                "🧑‍⚕️": "Health Worker",
                "👨‍⚕️": "Man Health Worker",
                "👩‍⚕️": "Woman Health Worker",
                "🧑‍🎓": "Student",
                "👨‍🎓": "Man Student",
                "👩‍🎓": "Woman Student",
                "🧑‍🏫": "Teacher",
                "👨‍🏫": "Man Teacher",
                "👩‍🏫": "Woman Teacher",
                "🧑‍⚖️": "Judge",
                "👨‍⚖️": "Man Judge",
                "👩‍⚖️": "Woman Judge",
                "🧑‍🌾": "Farmer",
                "👨‍🌾": "Man Farmer",
                "👩‍🌾": "Woman Farmer",
                "🧑‍🍳": "Cook",
                "👨‍🍳": "Man Cook",
                "👩‍🍳": "Woman Cook",
                "🧑‍🔧": "Mechanic",
                "👨‍🔧": "Man Mechanic",
                "👩‍🔧": "Woman Mechanic",
                "🧑‍🏭": "Factory Worker",
                "👨‍🏭": "Man Factory Worker",
                "👩‍🏭": "Woman Factory Worker",
                "🧑‍💼": "Office Worker",
                "👨‍💼": "Man Office Worker",
                "👩‍💼": "Woman Office Worker",
                "🧑‍🔬": "Scientist",
                "👨‍🔬": "Man Scientist",
                "👩‍🔬": "Woman Scientist",
                "🧑‍💻": "Technologist",
                "👨‍💻": "Man Technologist",
                "👩‍💻": "Woman Technologist",
                "🧑‍🎤": "Singer",
                "👨‍🎤": "Man Singer",
                "👩‍🎤": "Woman Singer",
                "🧑‍🎨": "Artist",
                "👨‍🎨": "Man Artist",
                "👩‍🎨": "Woman Artist",
                "🧑‍✈️": "Pilot",
                "👨‍✈️": "Man Pilot",
                "👩‍✈️": "Woman Pilot",
                "🧑‍🚀": "Astronaut",
                "👨‍🚀": "Man Astronaut",
                "👩‍🚀": "Woman Astronaut",
                "🧑‍🚒": "Firefighter",
                "👨‍🚒": "Man Firefighter",
                "👩‍🚒": "Woman Firefighter",
                "👮": "Police Officer",
                "👮‍♂️": "Man Police Officer",
                "👮‍♀️": "Woman Police Officer",
                "🕵️": "Detective",
                "🕵️‍♂️": "Man Detective",
                "🕵️‍♀️": "Woman Detective",
                "💂": "Guard",
                "💂‍♂️": "Man Guard",
                "💂‍♀️": "Woman Guard",
                "🥷": "Ninja",
                "👷": "Construction Worker",
                "👷‍♂️": "Man Construction Worker",
                "👷‍♀️": "Woman Construction Worker",
                "🤴": "Prince",
                "👸": "Princess",
                "👳": "Person Wearing Turban",
                "👳‍♂️": "Man Wearing Turban",
                "👳‍♀️": "Woman Wearing Turban",
                "👲": "Person With Skullcap",
                "🧕": "Woman with Headscarf",
                "🤵": "Person in Tuxedo",
                "🤵‍♂️": "Man in Tuxedo",
                "🤵‍♀️": "Woman in Tuxedo",
                "👰": "Person With Veil",
                "👰‍♂️": "Man with Veil",
                "👰‍♀️": "Woman with Veil",
                "🤰": "Pregnant Woman",
                "🤱": "Breast-Feeding",
                "👩‍🍼": "Woman Feeding Baby",
                "👨‍🍼": "Man Feeding Baby",
                "🧑‍🍼": "Person Feeding Baby",
                "👼": "Baby Angel",
                "🎅": "Santa Claus",
                "🤶": "Mrs. Claus",
                "🧑‍🎄": "Mx Claus",
                "🦸": "Superhero",
                "🦸‍♂️": "Man Superhero",
                "🦸‍♀️": "Woman Superhero",
                "🦹": "Supervillain",
                "🦹‍♂️": "Man Supervillain",
                "🦹‍♀️": "Woman Supervillain",
                "🧙": "Mage",
                "🧙‍♂️": "Man Mage",
                "🧙‍♀️": "Woman Mage",
                "🧚": "Fairy",
                "🧚‍♂️": "Man Fairy",
                "🧚‍♀️": "Woman Fairy",
                "🧛": "Vampire",
                "🧛‍♂️": "Man Vampire",
                "🧛‍♀️": "Woman Vampire",
                "🧜": "Merperson",
                "🧜‍♂️": "Merman",
                "🧜‍♀️": "Mermaid",
                "🧝": "Elf",
                "🧝‍♂️": "Man Elf",
                "🧝‍♀️": "Woman Elf",
                "🧞": "Genie",
                "🧞‍♂️": "Man Genie",
                "🧞‍♀️": "Woman Genie",
                "🧟": "Zombie",
                "🧟‍♂️": "Man Zombie",
                "🧟‍♀️": "Woman Zombie",
                "💆": "Person Getting Massage",
                "💆‍♂️": "Man Getting Massage",
                "💆‍♀️": "Woman Getting Massage",
                "💇": "Person Getting Haircut",
                "💇‍♂️": "Man Getting Haircut",
                "💇‍♀️": "Woman Getting Haircut",
                "🚶": "Person Walking",
                "🚶‍♂️": "Man Walking",
                "🚶‍♀️": "Woman Walking",
                "🧍": "Person Standing",
                "🧍‍♂️": "Man Standing",
                "🧍‍♀️": "Woman Standing",
                "🧎": "Person Kneeling",
                "🧎‍♂️": "Man Kneeling",
                "🧎‍♀️": "Woman Kneeling",
                "🧑‍🦯": "Person with White Cane",
                "👨‍🦯": "Man with White Cane",
                "👩‍🦯": "Woman with White Cane",
                "🧑‍🦼": "Person in Motorized Wheelchair",
                "👨‍🦼": "Man in Motorized Wheelchair",
                "👩‍🦼": "Woman in Motorized Wheelchair",
                "🧑‍🦽": "Person in Manual Wheelchair",
                "👨‍🦽": "Man in Manual Wheelchair",
                "👩‍🦽": "Woman in Manual Wheelchair",
                "🏃": "Person Running",
                "🏃‍♂️": "Man Running",
                "🏃‍♀️": "Woman Running",
                "💃": "Woman Dancing",
                "🕺": "Man Dancing",
                "🕴️": "Person in Suit Levitating",
                "👯": "People with Bunny Ears",
                "👯‍♂️": "Men with Bunny Ears",
                "👯‍♀️": "Women with Bunny Ears",
                "🧖": "Person in Steamy Room",
                "🧖‍♂️": "Man in Steamy Room",
                "🧖‍♀️": "Woman in Steamy Room",
                "🧘": "Person in Lotus Position",
                "🧑‍🤝‍🧑": "People Holding Hands",
                "👭": "Women Holding Hands",
                "👫": "Woman and Man Holding Hands",
                "👬": "Men Holding Hands",
                "💏": "Kiss",
                "👩‍❤️‍💋‍👨": "Kiss: Woman, Man",
                "👨‍❤️‍💋‍👨": "Kiss: Man, Man",
                "👩‍❤️‍💋‍👩": "Kiss: Woman, Woman",
                "💑": "Couple with Heart",
                "👩‍❤️‍👨": "Couple with Heart: Woman, Man",
                "👨‍❤️‍👨": "Couple with Heart: Man, Man",
                "👩‍❤️‍👩": "Couple with Heart: Woman, Woman",
                "👪": "Family",
                "👨‍👩‍👦": "Family: Man, Woman, Boy",
                "👨‍👩‍👧": "Family: Man, Woman, Girl",
                "👨‍👩‍👧‍👦": "Family: Man, Woman, Girl, Boy",
                "👨‍👩‍👦‍👦": "Family: Man, Woman, Boy, Boy",
                "👨‍👩‍👧‍👧": "Family: Man, Woman, Girl, Girl",
                "👨‍👨‍👦": "Family: Man, Man, Boy",
                "👨‍👨‍👧": "Family: Man, Man, Girl",
                "👨‍👨‍👧‍👦": "Family: Man, Man, Girl, Boy",
                "👨‍👨‍👦‍👦": "Family: Man, Man, Boy, Boy",
                "👨‍👨‍👧‍👧": "Family: Man, Man, Girl, Girl",
                "👩‍👩‍👦": "Family: Woman, Woman, Boy",
                "👩‍👩‍👧": "Family: Woman, Woman, Girl",
                "👩‍👩‍👧‍👦": "Family: Woman, Woman, Girl, Boy",
                "👩‍👩‍👦‍👦": "Family: Woman, Woman, Boy, Boy",
                "👩‍👩‍👧‍👧": "Family: Woman, Woman, Girl, Girl",
                "👨‍👦": "Family: Man, Boy",
                "👨‍👦‍👦": "Family: Man, Boy, Boy",
                "👨‍👧": "Family: Man, Girl",
                "👨‍👧‍👦": "Family: Man, Girl, Boy",
                "👨‍👧‍👧": "Family: Man, Girl, Girl",
                "👩‍👦": "Family: Woman, Boy",
                "👩‍👦‍👦": "Family: Woman, Boy, Boy",
                "👩‍👧": "Family: Woman, Girl",
                "👩‍👧‍👦": "Family: Woman, Girl, Boy",
                "👩‍👧‍👧": "Family: Woman, Girl, Girl",
                "🗣️": "Speaking Head",
                "👤": "Bust in Silhouette",
                "👥": "Busts in Silhouette",
                "🫂": "People Hugging",
                "👣": "Footprints",
                "🧳": "Luggage",
                "🌂": "Closed Umbrella",
                "☂️": "Umbrella",
                "🎃": "Jack-O-Lantern",
                "🧵": "Thread",
                "🧶": "Yarn",
                "👓": "Glasses",
                "🕶️": "Sunglasses",
                "🥽": "Goggles",
                "🥼": "Lab Coat",
                "🦺": "Safety Vest",
                "👔": "Necktie",
                "👕": "T-Shirt",
                "👖": "Jeans",
                "🧣": "Scarf",
                "🧤": "Gloves",
                "🧥": "Coat",
                "🧦": "Socks",
                "👗": "Dress",
                "👘": "Kimono",
                "🥻": "Sari",
                "🩱": "One-Piece Swimsuit",
                "🩲": "Briefs",
                "🩳": "Shorts",
                "👙": "Bikini",
                "👚": "Woman’s Clothes",
                "👛": "Purse",
                "👜": "Handbag",
                "👝": "Clutch Bag",
                "🎒": "Backpack",
                "🩴": "Thong Sandal",
                "👞": "Man’s Shoe",
                "👟": "Running Shoe",
                "🥾": "Hiking Boot",
                "🥿": "Flat Shoe",
                "👠": "High-Heeled Shoe",
                "👡": "Woman’s Sandal",
                "🩰": "Ballet Shoes",
                "👢": "Woman’s Boot",
                "👑": "Crown",
                "👒": "Woman’s Hat",
                "🎩": "Top Hat",
                "🎓": "Graduation Cap",
                "🧢": "Billed Cap",
                "🪖": "Military Helmet",
                "⛑️": "Rescue Worker’s Helmet",
                "💄": "Lipstick",
                "💍": "Ring",
                "💼": "Briefcase",
                "🩸": "Drop of Blood",
                "😮‍💨": "Face Exhaling",
                "😵‍💫": "Face with Spiral Eyes",
                "😶‍🌫️": "Face in Clouds"
            },
            'Animals & Nature': {
                "🙈": "See-No-Evil Monkey",
                "🙉": "Hear-No-Evil Monkey",
                "🙊": "Speak-No-Evil Monkey",
                "💥": "Collision",
                "💫": "Dizzy",
                "💦": "Sweat Droplets",
                "💨": "Dashing Away",
                "🐵": "Monkey Face",
                "🐒": "Monkey",
                "🦍": "Gorilla",
                "🦧": "Orangutan",
                "🐶": "Dog Face",
                "🐕": "Dog",
                "🦮": "Guide Dog",
                "🐕‍🦺": "Service Dog",
                "🐩": "Poodle",
                "🐺": "Wolf",
                "🦊": "Fox",
                "🦝": "Raccoon",
                "🐱": "Cat Face",
                "🐈": "Cat",
                "🐈‍⬛": "Black Cat",
                "🦁": "Lion",
                "🐯": "Tiger Face",
                "🐅": "Tiger",
                "🐆": "Leopard",
                "🐴": "Horse Face",
                "🐎": "Horse",
                "🦄": "Unicorn",
                "🦓": "Zebra",
                "🦌": "Deer",
                "🦬": "Bison",
                "🐮": "Cow Face",
                "🐂": "Ox",
                "🐃": "Water Buffalo",
                "🐄": "Cow",
                "🐷": "Pig Face",
                "🐖": "Pig",
                "🐗": "Boar",
                "🐽": "Pig Nose",
                "🐏": "Ram",
                "🐑": "Ewe",
                "🐐": "Goat",
                "🐪": "Camel",
                "🐫": "Two-Hump Camel",
                "🦙": "Llama",
                "🦒": "Giraffe",
                "🐘": "Elephant",
                "🦣": "Mammoth",
                "🦏": "Rhinoceros",
                "🦛": "Hippopotamus",
                "🐭": "Mouse Face",
                "🐁": "Mouse",
                "🐀": "Rat",
                "🐹": "Hamster",
                "🐰": "Rabbit Face",
                "🐇": "Rabbit",
                "🐿️": "Chipmunk",
                "🦫": "Beaver",
                "🦔": "Hedgehog",
                "🦇": "Bat",
                "🐻": "Bear",
                "🐻‍❄️": "Polar Bear",
                "🐨": "Koala",
                "🐼": "Panda",
                "🦥": "Sloth",
                "🦦": "Otter",
                "🦨": "Skunk",
                "🦘": "Kangaroo",
                "🦡": "Badger",
                "🐾": "Paw Prints",
                "🦃": "Turkey",
                "🐔": "Chicken",
                "🐓": "Rooster",
                "🐣": "Hatching Chick",
                "🐤": "Baby Chick",
                "🐥": "Front-Facing Baby Chick",
                "🐦": "Bird",
                "🐧": "Penguin",
                "🕊️": "Dove",
                "🦅": "Eagle",
                "🦆": "Duck",
                "🦢": "Swan",
                "🦉": "Owl",
                "🦤": "Dodo",
                "🪶": "Feather",
                "🦩": "Flamingo",
                "🦚": "Peacock",
                "🦜": "Parrot",
                "🐸": "Frog",
                "🐊": "Crocodile",
                "🐢": "Turtle",
                "🦎": "Lizard",
                "🐍": "Snake",
                "🐲": "Dragon Face",
                "🐉": "Dragon",
                "🦕": "Sauropod",
                "🦖": "T-Rex",
                "🐳": "Spouting Whale",
                "🐋": "Whale",
                "🐬": "Dolphin",
                "🦭": "Seal",
                "🐟": "Fish",
                "🐠": "Tropical Fish",
                "🐡": "Blowfish",
                "🦈": "Shark",
                "🐙": "Octopus",
                "🐚": "Spiral Shell",
                "🐌": "Snail",
                "🦋": "Butterfly",
                "🐛": "Bug",
                "🐜": "Ant",
                "🐝": "Honeybee",
                "🪲": "Beetle",
                "🐞": "Lady Beetle",
                "🦗": "Cricket",
                "🪳": "Cockroach",
                "🕷️": "Spider",
                "🕸️": "Spider Web",
                "🦂": "Scorpion",
                "🦟": "Mosquito",
                "🪰": "Fly",
                "🪱": "Worm",
                "🦠": "Microbe",
                "💐": "Bouquet",
                "🌸": "Cherry Blossom",
                "💮": "White Flower",
                "🏵️": "Rosette",
                "🌹": "Rose",
                "🥀": "Wilted Flower",
                "🌺": "Hibiscus",
                "🌻": "Sunflower",
                "🌼": "Blossom",
                "🌷": "Tulip",
                "🌱": "Seedling",
                "🪴": "Potted Plant",
                "🌲": "Evergreen Tree",
                "🌳": "Deciduous Tree",
                "🌴": "Palm Tree",
                "🌵": "Cactus",
                "🌾": "Sheaf of Rice",
                "🌿": "Herb",
                "☘️": "Shamrock",
                "🍀": "Four Leaf Clover",
                "🍁": "Maple Leaf",
                "🍂": "Fallen Leaf",
                "🍃": "Leaf Fluttering in Wind",
                "🍄": "Mushroom",
                "🌰": "Chestnut",
                "🦀": "Crab",
                "🦞": "Lobster",
                "🦐": "Shrimp",
                "🦑": "Squid",
                "🌍": "Globe Showing Europe-Africa",
                "🌎": "Globe Showing Americas",
                "🌏": "Globe Showing Asia-Australia",
                "🌐": "Globe with Meridians",
                "🪨": "Rock",
                "🌑": "New Moon",
                "🌒": "Waxing Crescent Moon",
                "🌓": "First Quarter Moon",
                "🌔": "Waxing Gibbous Moon",
                "🌕": "Full Moon",
                "🌖": "Waning Gibbous Moon",
                "🌗": "Last Quarter Moon",
                "🌘": "Waning Crescent Moon",
                "🌙": "Crescent Moon",
                "🌚": "New Moon Face",
                "🌛": "First Quarter Moon Face",
                "🌜": "Last Quarter Moon Face",
                "☀️": "Sun",
                "🌝": "Full Moon Face",
                "🌞": "Sun with Face",
                "⭐": "Star",
                "🌟": "Glowing Star",
                "🌠": "Shooting Star",
                "☁️": "Cloud",
                "⛅": "Sun Behind Cloud",
                "⛈️": "Cloud with Lightning and Rain",
                "🌤️": "Sun Behind Small Cloud",
                "🌥️": "Sun Behind Large Cloud",
                "🌦️": "Sun Behind Rain Cloud",
                "🌧️": "Cloud with Rain",
                "🌨️": "Cloud with Snow",
                "🌩️": "Cloud with Lightning",
                "🌪️": "Tornado",
                "🌫️": "Fog",
                "🌬️": "Wind Face",
                "🌈": "Rainbow",
                "☂️": "Umbrella",
                "☔": "Umbrella with Rain Drops",
                "⚡": "High Voltage",
                "❄️": "Snowflake",
                "☃️": "Snowman",
                "⛄": "Snowman Without Snow",
                "☄️": "Comet",
                "🔥": "Fire",
                "💧": "Droplet",
                "🌊": "Water Wave",
                "🎄": "Christmas Tree",
                "✨": "Sparkles",
                "🎋": "Tanabata Tree",
                "🎍": "Pine Decoration"
            },
            'Food & Drink': {
                "🍇": "Grapes",
                "🍈": "Melon",
                "🍉": "Watermelon",
                "🍊": "Tangerine",
                "🍋": "Lemon",
                "🍌": "Banana",
                "🍍": "Pineapple",
                "🥭": "Mango",
                "🍎": "Red Apple",
                "🍏": "Green Apple",
                "🍐": "Pear",
                "🍑": "Peach",
                "🍒": "Cherries",
                "🍓": "Strawberry",
                "🫐": "Blueberries",
                "🥝": "Kiwi Fruit",
                "🍅": "Tomato",
                "🫒": "Olive",
                "🥥": "Coconut",
                "🥑": "Avocado",
                "🍆": "Eggplant",
                "🥔": "Potato",
                "🥕": "Carrot",
                "🌽": "Ear of Corn",
                "🌶️": "Hot Pepper",
                "🫑": "Bell Pepper",
                "🥒": "Cucumber",
                "🥬": "Leafy Green",
                "🥦": "Broccoli",
                "🧄": "Garlic",
                "🧅": "Onion",
                "🍄": "Mushroom",
                "🥜": "Peanuts",
                "🌰": "Chestnut",
                "🍞": "Bread",
                "🥐": "Croissant",
                "🥖": "Baguette Bread",
                "🫓": "Flatbread",
                "🥨": "Pretzel",
                "🥯": "Bagel",
                "🥞": "Pancakes",
                "🧇": "Waffle",
                "🧀": "Cheese Wedge",
                "🍖": "Meat on Bone",
                "🍗": "Poultry Leg",
                "🥩": "Cut of Meat",
                "🥓": "Bacon",
                "🍔": "Hamburger",
                "🍟": "French Fries",
                "🍕": "Pizza",
                "🌭": "Hot Dog",
                "🥪": "Sandwich",
                "🌮": "Taco",
                "🌯": "Burrito",
                "🫔": "Tamale",
                "🥙": "Stuffed Flatbread",
                "🧆": "Falafel",
                "🥚": "Egg",
                "🍳": "Cooking",
                "🥘": "Shallow Pan of Food",
                "🍲": "Pot of Food",
                "🫕": "Fondue",
                "🥣": "Bowl with Spoon",
                "🥗": "Green Salad",
                "🍿": "Popcorn",
                "🧈": "Butter",
                "🧂": "Salt",
                "🥫": "Canned Food",
                "🍱": "Bento Box",
                "🍘": "Rice Cracker",
                "🍙": "Rice Ball",
                "🍚": "Cooked Rice",
                "🍛": "Curry Rice",
                "🍜": "Steaming Bowl",
                "🍝": "Spaghetti",
                "🍠": "Roasted Sweet Potato",
                "🍢": "Oden",
                "🍣": "Sushi",
                "🍤": "Fried Shrimp",
                "🍥": "Fish Cake with Swirl",
                "🥮": "Moon Cake",
                "🍡": "Dango",
                "🥟": "Dumpling",
                "🥠": "Fortune Cookie",
                "🥡": "Takeout Box",
                "🦪": "Oyster",
                "🍦": "Soft Ice Cream",
                "🍧": "Shaved Ice",
                "🍨": "Ice Cream",
                "🍩": "Doughnut",
                "🍪": "Cookie",
                "🎂": "Birthday Cake",
                "🍰": "Shortcake",
                "🧁": "Cupcake",
                "🥧": "Pie",
                "🍫": "Chocolate Bar",
                "🍬": "Candy",
                "🍭": "Lollipop",
                "🍮": "Custard",
                "🍯": "Honey Pot",
                "🍼": "Baby Bottle",
                "🥛": "Glass of Milk",
                "☕": "Hot Beverage",
                "🫖": "Teapot",
                "🍵": "Teacup Without Handle",
                "🍶": "Sake",
                "🍾": "Bottle with Popping Cork",
                "🍷": "Wine Glass",
                "🍸": "Cocktail Glass",
                "🍹": "Tropical Drink",
                "🍺": "Beer Mug",
                "🍻": "Clinking Beer Mugs",
                "🥂": "Clinking Glasses",
                "🥃": "Tumbler Glass",
                "🥤": "Cup with Straw",
                "🧋": "Bubble Tea",
                "🧃": "Beverage Box",
                "🧉": "Mate",
                "🧊": "Ice",
                "🥢": "Chopsticks",
                "🍽️": "Fork and Knife with Plate",
                "🍴": "Fork and Knife",
                "🥄": "Spoon"
            },
            'Activity': {
                "🕴️": "Person in Suit Levitating",
                "🧗": "Person Climbing",
                "🧗‍♂️": "Man Climbing",
                "🧗‍♀️": "Woman Climbing",
                "🤺": "Person Fencing",
                "🏇": "Horse Racing",
                "⛷️": "Skier",
                "🏂": "Snowboarder",
                "🏌️": "Person Golfing",
                "🏌️‍♂️": "Man Golfing",
                "🏌️‍♀️": "Woman Golfing",
                "🏄": "Person Surfing",
                "🏄‍♂️": "Man Surfing",
                "🏄‍♀️": "Woman Surfing",
                "🚣": "Person Rowing Boat",
                "🚣‍♂️": "Man Rowing Boat",
                "🚣‍♀️": "Woman Rowing Boat",
                "🏊": "Person Swimming",
                "🏊‍♂️": "Man Swimming",
                "🏊‍♀️": "Woman Swimming",
                "⛹️": "Person Bouncing Ball",
                "⛹️‍♂️": "Man Bouncing Ball",
                "⛹️‍♀️": "Woman Bouncing Ball",
                "🏋️": "Person Lifting Weights",
                "🏋️‍♂️": "Man Lifting Weights",
                "🏋️‍♀️": "Woman Lifting Weights",
                "🚴": "Person Biking",
                "🚴‍♂️": "Man Biking",
                "🚴‍♀️": "Woman Biking",
                "🚵": "Person Mountain Biking",
                "🚵‍♂️": "Man Mountain Biking",
                "🚵‍♀️": "Woman Mountain Biking",
                "🤸": "Person Cartwheeling",
                "🤸‍♂️": "Man Cartwheeling",
                "🤸‍♀️": "Woman Cartwheeling",
                "🤼": "People Wrestling",
                "🤼‍♂️": "Men Wrestling",
                "🤼‍♀️": "Women Wrestling",
                "🤽": "Person Playing Water Polo",
                "🤽‍♂️": "Man Playing Water Polo",
                "🤽‍♀️": "Woman Playing Water Polo",
                "🤾": "Person Playing Handball",
                "🤾‍♂️": "Man Playing Handball",
                "🤾‍♀️": "Woman Playing Handball",
                "🤹": "Person Juggling",
                "🤹‍♂️": "Man Juggling",
                "🤹‍♀️": "Woman Juggling",
                "🧘": "Person in Lotus Position",
                "🧘‍♂️": "Man in Lotus Position",
                "🧘‍♀️": "Woman in Lotus Position",
                "🎪": "Circus Tent",
                "🛹": "Skateboard",
                "🛼": "Roller Skate",
                "🛶": "Canoe",
                "🎗️": "Reminder Ribbon",
                "🎟️": "Admission Tickets",
                "🎫": "Ticket",
                "🎖️": "Military Medal",
                "🏆": "Trophy",
                "🏅": "Sports Medal",
                "🥇": "1st Place Medal",
                "🥈": "2nd Place Medal",
                "🥉": "3rd Place Medal",
                "⚽": "Soccer Ball",
                "⚾": "Baseball",
                "🥎": "Softball",
                "🏀": "Basketball",
                "🏐": "Volleyball",
                "🏈": "American Football",
                "🏉": "Rugby Football",
                "🎾": "Tennis",
                "🥏": "Flying Disc",
                "🎳": "Bowling",
                "🏏": "Cricket Game",
                "🏑": "Field Hockey",
                "🏒": "Ice Hockey",
                "🥍": "Lacrosse",
                "🏓": "Ping Pong",
                "🏸": "Badminton",
                "🥊": "Boxing Glove",
                "🥋": "Martial Arts Uniform",
                "🥅": "Goal Net",
                "⛳": "Flag in Hole",
                "⛸️": "Ice Skate",
                "🎣": "Fishing Pole",
                "🎽": "Running Shirt",
                "🎿": "Skis",
                "🛷": "Sled",
                "🥌": "Curling Stone",
                "🎯": "Direct Hit",
                "🎱": "Pool 8 Ball",
                "🎮": "Video Game",
                "🎰": "Slot Machine",
                "🎲": "Game Die",
                "🧩": "Puzzle Piece",
                "♟️": "Chess Pawn",
                "🎭": "Performing Arts",
                "🎨": "Artist Palette",
                "🧵": "Thread",
                "🧶": "Yarn",
                "🎼": "Musical Score",
                "🎤": "Microphone",
                "🎧": "Headphone",
                "🎷": "Saxophone",
                "🪗": "Accordion",
                "🎸": "Guitar",
                "🎹": "Musical Keyboard",
                "🎺": "Trumpet",
                "🎻": "Violin",
                "🥁": "Drum",
                "🪘": "Long Drum",
                "🎬": "Clapper Board",
                "🏹": "Bow and Arrow"
            },
            'Travel & Places': {
                "🚣": "Person Rowing Boat",
                "🗾": "Map of Japan",
                "🏔️": "Snow-Capped Mountain",
                "⛰️": "Mountain",
                "🌋": "Volcano",
                "🗻": "Mount Fuji",
                "🏕️": "Camping",
                "🏖️": "Beach with Umbrella",
                "🏜️": "Desert",
                "🏝️": "Desert Island",
                "🏞️": "National Park",
                "🏟️": "Stadium",
                "🏛️": "Classical Building",
                "🏗️": "Building Construction",
                "🛖": "Hut",
                "🏘️": "Houses",
                "🏚️": "Derelict House",
                "🏠": "House",
                "🏡": "House with Garden",
                "🏢": "Office Building",
                "🏣": "Japanese Post Office",
                "🏤": "Post Office",
                "🏥": "Hospital",
                "🏦": "Bank",
                "🏨": "Hotel",
                "🏩": "Love Hotel",
                "🏪": "Convenience Store",
                "🏫": "School",
                "🏬": "Department Store",
                "🏭": "Factory",
                "🏯": "Japanese Castle",
                "🏰": "Castle",
                "💒": "Wedding",
                "🗼": "Tokyo Tower",
                "🗽": "Statue of Liberty",
                "⛪": "Church",
                "🕌": "Mosque",
                "🛕": "Hindu Temple",
                "🕍": "Synagogue",
                "⛩️": "Shinto Shrine",
                "🕋": "Kaaba",
                "⛲": "Fountain",
                "⛺": "Tent",
                "🌁": "Foggy",
                "🌃": "Night with Stars",
                "🏙️": "Cityscape",
                "🌄": "Sunrise Over Mountains",
                "🌅": "Sunrise",
                "🌆": "Cityscape at Dusk",
                "🌇": "Sunset",
                "🌉": "Bridge at Night",
                "🎠": "Carousel Horse",
                "🎡": "Ferris Wheel",
                "🎢": "Roller Coaster",
                "🚂": "Locomotive",
                "🚃": "Railway Car",
                "🚄": "High-Speed Train",
                "🚅": "Bullet Train",
                "🚆": "Train",
                "🚇": "Metro",
                "🚈": "Light Rail",
                "🚉": "Station",
                "🚊": "Tram",
                "🚝": "Monorail",
                "🚞": "Mountain Railway",
                "🚋": "Tram Car",
                "🚌": "Bus",
                "🚍": "Oncoming Bus",
                "🚎": "Trolleybus",
                "🚐": "Minibus",
                "🚑": "Ambulance",
                "🚒": "Fire Engine",
                "🚓": "Police Car",
                "🚔": "Oncoming Police Car",
                "🚕": "Taxi",
                "🚖": "Oncoming Taxi",
                "🚗": "Automobile",
                "🚘": "Oncoming Automobile",
                "🚙": "Sport Utility Vehicle",
                "🛻": "Pickup Truck",
                "🚚": "Delivery Truck",
                "🚛": "Articulated Lorry",
                "🚜": "Tractor",
                "🏎️": "Racing Car",
                "🏍️": "Motorcycle",
                "🛵": "Motor Scooter",
                "🛺": "Auto Rickshaw",
                "🚲": "Bicycle",
                "🛴": "Kick Scooter",
                "🚏": "Bus Stop",
                "🛣️": "Motorway",
                "🛤️": "Railway Track",
                "⛽": "Fuel Pump",
                "🚨": "Police Car Light",
                "🚥": "Horizontal Traffic Light",
                "🚦": "Vertical Traffic Light",
                "🚧": "Construction",
                "⚓": "Anchor",
                "⛵": "Sailboat",
                "🚤": "Speedboat",
                "🛳️": "Passenger Ship",
                "⛴️": "Ferry",
                "🛥️": "Motor Boat",
                "🚢": "Ship",
                "✈️": "Airplane",
                "🛩️": "Small Airplane",
                "🛫": "Airplane Departure",
                "🛬": "Airplane Arrival",
                "🪂": "Parachute",
                "💺": "Seat",
                "🚁": "Helicopter",
                "🚟": "Suspension Railway",
                "🚠": "Mountain Cableway",
                "🚡": "Aerial Tramway",
                "🛰️": "Satellite",
                "🚀": "Rocket",
                "🛸": "Flying Saucer",
                "🪐": "Ringed Planet",
                "🌠": "Shooting Star",
                "🌌": "Milky Way",
                "⛱️": "Umbrella on Ground",
                "🎆": "Fireworks",
                "🎇": "Sparkler",
                "🎑": "Moon Viewing Ceremony",
                "💴": "Yen Banknote",
                "💵": "Dollar Banknote",
                "💶": "Euro Banknote",
                "💷": "Pound Banknote",
                "🗿": "Moai",
                "🛂": "Passport Control",
                "🛃": "Customs",
                "🛄": "Baggage Claim",
                "🛅": "Left Luggage"
            },
            'Objects': {
                "💌": "Love Letter",
                "🕳️": "Hole",
                "💣": "Bomb",
                "🛀": "Person Taking Bath",
                "🛌": "Person in Bed",
                "🔪": "Kitchen Knife",
                "🏺": "Amphora",
                "🗺️": "World Map",
                "🧭": "Compass",
                "🧱": "Brick",
                "💈": "Barber Pole",
                "🦽": "Manual Wheelchair",
                "🦼": "Motorized Wheelchair",
                "🛢️": "Oil Drum",
                "🛎️": "Bellhop Bell",
                "🧳": "Luggage",
                "⌛": "Hourglass Done",
                "⏳": "Hourglass Not Done",
                "⌚": "Watch",
                "⏰": "Alarm Clock",
                "⏱️": "Stopwatch",
                "⏲️": "Timer Clock",
                "🕰️": "Mantelpiece Clock",
                "🌡️": "Thermometer",
                "⛱️": "Umbrella on Ground",
                "🧨": "Firecracker",
                "🎈": "Balloon",
                "🎉": "Party Popper",
                "🎊": "Confetti Ball",
                "🎎": "Japanese Dolls",
                "🎏": "Carp Streamer",
                "🎐": "Wind Chime",
                "🧧": "Red Envelope",
                "🎀": "Ribbon",
                "🎁": "Wrapped Gift",
                "🤿": "Diving Mask",
                "🪀": "Yo-Yo",
                "🪁": "Kite",
                "🔮": "Crystal Ball",
                "🪄": "Magic Wand",
                "🧿": "Nazar Amulet",
                "🕹️": "Joystick",
                "🧸": "Teddy Bear",
                "🪅": "Piñata",
                "🪆": "Nesting Dolls",
                "🖼️": "Framed Picture",
                "🧵": "Thread",
                "🪡": "Sewing Needle",
                "🧶": "Yarn",
                "🪢": "Knot",
                "🛍️": "Shopping Bags",
                "📿": "Prayer Beads",
                "💎": "Gem Stone",
                "📯": "Postal Horn",
                "🎙️": "Studio Microphone",
                "🎚️": "Level Slider",
                "🎛️": "Control Knobs",
                "📻": "Radio",
                "🪕": "Banjo",
                "📱": "Mobile Phone",
                "📲": "Mobile Phone with Arrow",
                "☎️": "Telephone",
                "📞": "Telephone Receiver",
                "📟": "Pager",
                "📠": "Fax Machine",
                "🔋": "Battery",
                "🔌": "Electric Plug",
                "💻": "Laptop",
                "🖥️": "Desktop Computer",
                "🖨️": "Printer",
                "⌨️": "Keyboard",
                "🖱️": "Computer Mouse",
                "🖲️": "Trackball",
                "💽": "Computer Disk",
                "💾": "Floppy Disk",
                "💿": "Optical Disk",
                "📀": "DVD",
                "🧮": "Abacus",
                "🎥": "Movie Camera",
                "🎞️": "Film Frames",
                "📽️": "Film Projector",
                "📺": "Television",
                "📷": "Camera",
                "📸": "Camera with Flash",
                "📹": "Video Camera",
                "📼": "Videocassette",
                "🔍": "Magnifying Glass Tilted Left",
                "🔎": "Magnifying Glass Tilted Right",
                "🕯️": "Candle",
                "💡": "Light Bulb",
                "🔦": "Flashlight",
                "🏮": "Red Paper Lantern",
                "🪔": "Diya Lamp",
                "📔": "Notebook with Decorative Cover",
                "📕": "Closed Book",
                "📖": "Open Book",
                "📗": "Green Book",
                "📘": "Blue Book",
                "📙": "Orange Book",
                "📚": "Books",
                "📓": "Notebook",
                "📒": "Ledger",
                "📃": "Page with Curl",
                "📜": "Scroll",
                "📄": "Page Facing Up",
                "📰": "Newspaper",
                "🗞️": "Rolled-Up Newspaper",
                "📑": "Bookmark Tabs",
                "🔖": "Bookmark",
                "🏷️": "Label",
                "💰": "Money Bag",
                "🪙": "Coin",
                "💴": "Yen Banknote",
                "💵": "Dollar Banknote",
                "💶": "Euro Banknote",
                "💷": "Pound Banknote",
                "💸": "Money with Wings",
                "💳": "Credit Card",
                "🧾": "Receipt",
                "✉️": "Envelope",
                "📧": "E-Mail",
                "📨": "Incoming Envelope",
                "📩": "Envelope with Arrow",
                "📤": "Outbox Tray",
                "📥": "Inbox Tray",
                "📦": "Package",
                "📫": "Closed Mailbox with Raised Flag",
                "📪": "Closed Mailbox with Lowered Flag",
                "📬": "Open Mailbox with Raised Flag",
                "📭": "Open Mailbox with Lowered Flag",
                "📮": "Postbox",
                "🗳️": "Ballot Box with Ballot",
                "✏️": "Pencil",
                "✒️": "Black Nib",
                "🖋️": "Fountain Pen",
                "🖊️": "Pen",
                "🖌️": "Paintbrush",
                "🖍️": "Crayon",
                "📝": "Memo",
                "📁": "File Folder",
                "📂": "Open File Folder",
                "🗂️": "Card Index Dividers",
                "📅": "Calendar",
                "📆": "Tear-Off Calendar",
                "🗒️": "Spiral Notepad",
                "🗓️": "Spiral Calendar",
                "📇": "Card Index",
                "📈": "Chart Increasing",
                "📉": "Chart Decreasing",
                "📊": "Bar Chart",
                "📋": "Clipboard",
                "📌": "Pushpin",
                "📍": "Round Pushpin",
                "📎": "Paperclip",
                "🖇️": "Linked Paperclips",
                "📏": "Straight Ruler",
                "📐": "Triangular Ruler",
                "✂️": "Scissors",
                "🗃️": "Card File Box",
                "🗄️": "File Cabinet",
                "🗑️": "Wastebasket",
                "🔒": "Locked",
                "🔓": "Unlocked",
                "🔏": "Locked with Pen",
                "🔐": "Locked with Key",
                "🔑": "Key",
                "🗝️": "Old Key",
                "🔨": "Hammer",
                "🪓": "Axe",
                "⛏️": "Pick",
                "⚒️": "Hammer and Pick",
                "🛠️": "Hammer and Wrench",
                "🗡️": "Dagger",
                "⚔️": "Crossed Swords",
                "🔫": "Pistol",
                "🪃": "Boomerang",
                "🛡️": "Shield",
                "🪚": "Carpentry Saw",
                "🔧": "Wrench",
                "🪛": "Screwdriver",
                "🔩": "Nut and Bolt",
                "⚙️": "Gear",
                "🗜️": "Clamp",
                "⚖️": "Balance Scale",
                "🦯": "White Cane",
                "🔗": "Link",
                "⛓️": "Chains",
                "🪝": "Hook",
                "🧰": "Toolbox",
                "🧲": "Magnet",
                "🪜": "Ladder",
                "⚗️": "Alembic",
                "🧪": "Test Tube",
                "🧫": "Petri Dish",
                "🧬": "DNA",
                "🔬": "Microscope",
                "🔭": "Telescope",
                "📡": "Satellite Antenna",
                "💉": "Syringe",
                "🩸": "Drop of Blood",
                "💊": "Pill",
                "🩹": "Adhesive Bandage",
                "🩺": "Stethoscope",
                "🚪": "Door",
                "🪞": "Mirror",
                "🪟": "Window",
                "🛏️": "Bed",
                "🛋️": "Couch and Lamp",
                "🪑": "Chair",
                "🚽": "Toilet",
                "🪠": "Plunger",
                "🚿": "Shower",
                "🛁": "Bathtub",
                "🪤": "Mouse Trap",
                "🪒": "Razor",
                "🧴": "Lotion Bottle",
                "🧷": "Safety Pin",
                "🧹": "Broom",
                "🧺": "Basket",
                "🧻": "Roll of Paper",
                "🪣": "Bucket",
                "🧼": "Soap",
                "🪥": "Toothbrush",
                "🧽": "Sponge",
                "🧯": "Fire Extinguisher",
                "🛒": "Shopping Cart",
                "🚬": "Cigarette",
                "⚰️": "Coffin",
                "🪦": "Headstone",
                "⚱️": "Funeral Urn",
                "🗿": "Moai",
                "🪧": "Placard",
                "🚰": "Potable Water"
            },
            'Symbols': {
                "💘": "Heart with Arrow",
                "💝": "Heart with Ribbon",
                "💖": "Sparkling Heart",
                "💗": "Growing Heart",
                "💓": "Beating Heart",
                "💞": "Revolving Hearts",
                "💕": "Two Hearts",
                "💟": "Heart Decoration",
                "❣️": "Heart Exclamation",
                "💔": "Broken Heart",
                "❤️": "Red Heart",
                "🧡": "Orange Heart",
                "💛": "Yellow Heart",
                "💚": "Green Heart",
                "💙": "Blue Heart",
                "💜": "Purple Heart",
                "🤎": "Brown Heart",
                "🖤": "Black Heart",
                "🤍": "White Heart",
                "💯": "Hundred Points",
                "💢": "Anger Symbol",
                "💬": "Speech Balloon",
                "👁️‍🗨️": "Eye in Speech Bubble",
                "🗨️": "Left Speech Bubble",
                "🗯️": "Right Anger Bubble",
                "💭": "Thought Balloon",
                "💤": "Zzz",
                "💮": "White Flower",
                "♨️": "Hot Springs",
                "💈": "Barber Pole",
                "🛑": "Stop Sign",
                "🕛": "Twelve O’Clock",
                "🕧": "Twelve-Thirty",
                "🕐": "One O’Clock",
                "🕜": "One-Thirty",
                "🕑": "Two O’Clock",
                "🕝": "Two-Thirty",
                "🕒": "Three O’Clock",
                "🕞": "Three-Thirty",
                "🕓": "Four O’Clock",
                "🕟": "Four-Thirty",
                "🕔": "Five O’Clock",
                "🕠": "Five-Thirty",
                "🕕": "Six O’Clock",
                "🕡": "Six-Thirty",
                "🕖": "Seven O’Clock",
                "🕢": "Seven-Thirty",
                "🕗": "Eight O’Clock",
                "🕣": "Eight-Thirty",
                "🕘": "Nine O’Clock",
                "🕤": "Nine-Thirty",
                "🕙": "Ten O’Clock",
                "🕥": "Ten-Thirty",
                "🕚": "Eleven O’Clock",
                "🕦": "Eleven-Thirty",
                "🌀": "Cyclone",
                "♠️": "Spade Suit",
                "♥️": "Heart Suit",
                "♦️": "Diamond Suit",
                "♣️": "Club Suit",
                "🃏": "Joker",
                "🀄": "Mahjong Red Dragon",
                "🎴": "Flower Playing Cards",
                "🔇": "Muted Speaker",
                "🔈": "Speaker Low Volume",
                "🔉": "Speaker Medium Volume",
                "🔊": "Speaker High Volume",
                "📢": "Loudspeaker",
                "📣": "Megaphone",
                "📯": "Postal Horn",
                "🔔": "Bell",
                "🔕": "Bell with Slash",
                "🎵": "Musical Note",
                "🎶": "Musical Notes",
                "💹": "Chart Increasing with Yen",
                "🛗": "Elevator",
                "🏧": "ATM Sign",
                "🚮": "Litter in Bin Sign",
                "🚰": "Potable Water",
                "♿": "Wheelchair Symbol",
                "🚹": "Men’s Room",
                "🚺": "Women’s Room",
                "🚻": "Restroom",
                "🚼": "Baby Symbol",
                "🚾": "Water Closet",
                "⚠️": "Warning",
                "🚸": "Children Crossing",
                "⛔": "No Entry",
                "🚫": "Prohibited",
                "🚳": "No Bicycles",
                "🚭": "No Smoking",
                "🚯": "No Littering",
                "🚱": "Non-Potable Water",
                "🚷": "No Pedestrians",
                "📵": "No Mobile Phones",
                "🔞": "No One Under Eighteen",
                "☢️": "Radioactive",
                "☣️": "Biohazard",
                "⬆️": "Up Arrow",
                "↗️": "Up-Right Arrow",
                "➡️": "Right Arrow",
                "↘️": "Down-Right Arrow",
                "⬇️": "Down Arrow",
                "↙️": "Down-Left Arrow",
                "⬅️": "Left Arrow",
                "↖️": "Up-Left Arrow",
                "↕️": "Up-Down Arrow",
                "↔️": "Left-Right Arrow",
                "↩️": "Right Arrow Curving Left",
                "↪️": "Left Arrow Curving Right",
                "⤴️": "Right Arrow Curving Up",
                "⤵️": "Right Arrow Curving Down",
                "🔃": "Clockwise Vertical Arrows",
                "🔄": "Counterclockwise Arrows Button",
                "🔙": "Back Arrow",
                "🔚": "End Arrow",
                "🔛": "On! Arrow",
                "🔜": "Soon Arrow",
                "🔝": "Top Arrow",
                "🛐": "Place of Worship",
                "⚛️": "Atom Symbol",
                "🕉️": "Om",
                "✡️": "Star of David",
                "☸️": "Wheel of Dharma",
                "☯️": "Yin Yang",
                "✝️": "Latin Cross",
                "☦️": "Orthodox Cross",
                "☪️": "Star and Crescent",
                "☮️": "Peace Symbol",
                "🕎": "Menorah",
                "🔯": "Dotted Six-Pointed Star",
                "♈": "Aries",
                "♉": "Taurus",
                "♊": "Gemini",
                "♋": "Cancer",
                "♌": "Leo",
                "♍": "Virgo",
                "♎": "Libra",
                "♏": "Scorpio",
                "♐": "Sagittarius",
                "♑": "Capricorn",
                "♒": "Aquarius",
                "♓": "Pisces",
                "⛎": "Ophiuchus",
                "🔀": "Shuffle Tracks Button",
                "🔁": "Repeat Button",
                "🔂": "Repeat Single Button",
                "▶️": "Play Button",
                "⏩": "Fast-Forward Button",
                "⏭️": "Next Track Button",
                "⏯️": "Play or Pause Button",
                "◀️": "Reverse Button",
                "⏪": "Fast Reverse Button",
                "⏮️": "Last Track Button",
                "🔼": "Upwards Button",
                "⏫": "Fast Up Button",
                "🔽": "Downwards Button",
                "⏬": "Fast Down Button",
                "⏸️": "Pause Button",
                "⏹️": "Stop Button",
                "⏺️": "Record Button",
                "⏏️": "Eject Button",
                "🎦": "Cinema",
                "🔅": "Dim Button",
                "🔆": "Bright Button",
                "📶": "Antenna Bars",
                "📳": "Vibration Mode",
                "📴": "Mobile Phone Off",
                "♀️": "Female Sign",
                "♂️": "Male Sign",
                "✖️": "Multiply",
                "➕": "Plus",
                "➖": "Minus",
                "➗": "Divide",
                "♾️": "Infinity",
                "‼️": "Double Exclamation Mark",
                "⁉️": "Exclamation Question Mark",
                "❓": "Question Mark",
                "❔": "White Question Mark",
                "❕": "White Exclamation Mark",
                "❗": "Exclamation Mark",
                "〰️": "Wavy Dash",
                "💱": "Currency Exchange",
                "💲": "Heavy Dollar Sign",
                "⚕️": "Medical Symbol",
                "♻️": "Recycling Symbol",
                "⚜️": "Fleur-de-lis",
                "🔱": "Trident Emblem",
                "📛": "Name Badge",
                "🔰": "Japanese Symbol for Beginner",
                "⭕": "Hollow Red Circle",
                "✅": "Check Mark Button",
                "☑️": "Check Box with Check",
                "✔️": "Check Mark",
                "❌": "Cross Mark",
                "❎": "Cross Mark Button",
                "➰": "Curly Loop",
                "➿": "Double Curly Loop",
                "〽️": "Part Alternation Mark",
                "✳️": "Eight-Spoked Asterisk",
                "✴️": "Eight-Pointed Star",
                "❇️": "Sparkle",
                "©️": "Copyright",
                "®️": "Registered",
                "™️": "Trade Mark",
                "#️⃣": "Keycap Number Sign",
                "*️⃣": "Keycap Asterisk",
                "0️⃣": "Keycap Digit Zero",
                "1️⃣": "Keycap Digit One",
                "2️⃣": "Keycap Digit Two",
                "3️⃣": "Keycap Digit Three",
                "4️⃣": "Keycap Digit Four",
                "5️⃣": "Keycap Digit Five",
                "6️⃣": "Keycap Digit Six",
                "7️⃣": "Keycap Digit Seven",
                "8️⃣": "Keycap Digit Eight",
                "9️⃣": "Keycap Digit Nine",
                "🔟": "Keycap: 10",
                "🔠": "Input Latin Uppercase",
                "🔡": "Input Latin Lowercase",
                "🔢": "Input Numbers",
                "🔣": "Input Symbols",
                "🔤": "Input Latin Letters",
                "🅰️": "A Button (Blood Type)",
                "🆎": "AB Button (Blood Type)",
                "🅱️": "B Button (Blood Type)",
                "🆑": "CL Button",
                "🆒": "Cool Button",
                "🆓": "Free Button",
                "ℹ️": "Information",
                "🆔": "ID Button",
                "Ⓜ️": "Circled M",
                "🆕": "New Button",
                "🆖": "NG Button",
                "🅾️": "O Button (Blood Type)",
                "🆗": "OK Button",
                "🅿️": "P Button",
                "🆘": "SOS Button",
                "🆙": "Up! Button",
                "🆚": "Vs Button",
                "🈁": "Japanese “Here” Button",
                "🈂️": "Japanese “Service Charge” Button",
                "🈷️": "Japanese “Monthly Amount” Button",
                "🈶": "Japanese “Not Free of Charge” Button",
                "🈯": "Japanese “Reserved” Button",
                "🉐": "Japanese “Bargain” Button",
                "🈹": "Japanese “Discount” Button",
                "🈚": "Japanese “Free of Charge” Button",
                "🈲": "Japanese “Prohibited” Button",
                "🉑": "Japanese “Acceptable” Button",
                "🈸": "Japanese “Application” Button",
                "🈴": "Japanese “Passing Grade” Button",
                "🈳": "Japanese “Vacancy” Button",
                "㊗️": "Japanese “Congratulations” Button",
                "㊙️": "Japanese “Secret” Button",
                "🈺": "Japanese “Open for Business” Button",
                "🈵": "Japanese “No Vacancy” Button",
                "🔴": "Red Circle",
                "🟠": "Orange Circle",
                "🟡": "Yellow Circle",
                "🟢": "Green Circle",
                "🔵": "Blue Circle",
                "🟣": "Purple Circle",
                "🟤": "Brown Circle",
                "⚫": "Black Circle",
                "⚪": "White Circle",
                "🟥": "Red Square",
                "🟧": "Orange Square",
                "🟨": "Yellow Square",
                "🟩": "Green Square",
                "🟦": "Blue Square",
                "🟪": "Purple Square",
                "🟫": "Brown Square",
                "⬛": "Black Large Square",
                "⬜": "White Large Square",
                "◼️": "Black Medium Square",
                "◻️": "White Medium Square",
                "◾": "Black Medium-Small Square",
                "◽": "White Medium-Small Square",
                "▪️": "Black Small Square",
                "▫️": "White Small Square",
                "🔶": "Large Orange Diamond",
                "🔷": "Large Blue Diamond",
                "🔸": "Small Orange Diamond",
                "🔹": "Small Blue Diamond",
                "🔺": "Red Triangle Pointed Up",
                "🔻": "Red Triangle Pointed Down",
                "💠": "Diamond with a Dot",
                "🔘": "Radio Button",
                "🔳": "White Square Button",
                "🔲": "Black Square Button",
                "❤️‍🔥": "Heart on Fire",
                "❤️‍🩹": "Mending Heart"
            },
            'Flags': {
                "🏁": "Chequered Flag",
                "🚩": "Triangular Flag",
                "🎌": "Crossed Flags",
                "🏴": "Black Flag",
                "🏳️": "White Flag",
                "🏳️‍🌈": "Rainbow Flag",
                "🏳️‍⚧️": "Transgender Flag",
                "🏴‍☠️": "Pirate Flag",
                "🇦🇨": "Flag: Ascension Island",
                "🇦🇩": "Flag: Andorra",
                "🇦🇪": "Flag: United Arab Emirates",
                "🇦🇫": "Flag: Afghanistan",
                "🇦🇬": "Flag: Antigua & Barbuda",
                "🇦🇮": "Flag: Anguilla",
                "🇦🇱": "Flag: Albania",
                "🇦🇲": "Flag: Armenia",
                "🇦🇴": "Flag: Angola",
                "🇦🇶": "Flag: Antarctica",
                "🇦🇷": "Flag: Argentina",
                "🇦🇸": "Flag: American Samoa",
                "🇦🇹": "Flag: Austria",
                "🇦🇺": "Flag: Australia",
                "🇦🇼": "Flag: Aruba",
                "🇦🇽": "Flag: Åland Islands",
                "🇦🇿": "Flag: Azerbaijan",
                "🇧🇦": "Flag: Bosnia & Herzegovina",
                "🇧🇧": "Flag: Barbados",
                "🇧🇩": "Flag: Bangladesh",
                "🇧🇪": "Flag: Belgium",
                "🇧🇫": "Flag: Burkina Faso",
                "🇧🇬": "Flag: Bulgaria",
                "🇧🇭": "Flag: Bahrain",
                "🇧🇮": "Flag: Burundi",
                "🇧🇯": "Flag: Benin",
                "🇧🇱": "Flag: St. Barthélemy",
                "🇧🇲": "Flag: Bermuda",
                "🇧🇳": "Flag: Brunei",
                "🇧🇴": "Flag: Bolivia",
                "🇧🇶": "Flag: Caribbean Netherlands",
                "🇧🇷": "Flag: Brazil",
                "🇧🇸": "Flag: Bahamas",
                "🇧🇹": "Flag: Bhutan",
                "🇧🇻": "Flag: Bouvet Island",
                "🇧🇼": "Flag: Botswana",
                "🇧🇾": "Flag: Belarus",
                "🇧🇿": "Flag: Belize",
                "🇨🇦": "Flag: Canada",
                "🇨🇨": "Flag: Cocos (Keeling) Islands",
                "🇨🇩": "Flag: Congo - Kinshasa",
                "🇨🇫": "Flag: Central African Republic",
                "🇨🇬": "Flag: Congo - Brazzaville",
                "🇨🇭": "Flag: Switzerland",
                "🇨🇮": "Flag: Côte d’Ivoire",
                "🇨🇰": "Flag: Cook Islands",
                "🇨🇱": "Flag: Chile",
                "🇨🇲": "Flag: Cameroon",
                "🇨🇳": "Flag: China",
                "🇨🇴": "Flag: Colombia",
                "🇨🇵": "Flag: Clipperton Island",
                "🇨🇷": "Flag: Costa Rica",
                "🇨🇺": "Flag: Cuba",
                "🇨🇻": "Flag: Cape Verde",
                "🇨🇼": "Flag: Curaçao",
                "🇨🇽": "Flag: Christmas Island",
                "🇨🇾": "Flag: Cyprus",
                "🇨🇿": "Flag: Czechia",
                "🇩🇪": "Flag: Germany",
                "🇩🇬": "Flag: Diego Garcia",
                "🇩🇯": "Flag: Djibouti",
                "🇩🇰": "Flag: Denmark",
                "🇩🇲": "Flag: Dominica",
                "🇩🇴": "Flag: Dominican Republic",
                "🇩🇿": "Flag: Algeria",
                "🇪🇦": "Flag: Ceuta & Melilla",
                "🇪🇨": "Flag: Ecuador",
                "🇪🇪": "Flag: Estonia",
                "🇪🇬": "Flag: Egypt",
                "🇪🇭": "Flag: Western Sahara",
                "🇪🇷": "Flag: Eritrea",
                "🇪🇸": "Flag: Spain",
                "🇪🇹": "Flag: Ethiopia",
                "🇪🇺": "Flag: European Union",
                "🇫🇮": "Flag: Finland",
                "🇫🇯": "Flag: Fiji",
                "🇫🇰": "Flag: Falkland Islands",
                "🇫🇲": "Flag: Micronesia",
                "🇫🇴": "Flag: Faroe Islands",
                "🇫🇷": "Flag: France",
                "🇬🇦": "Flag: Gabon",
                "🇬🇧": "Flag: United Kingdom",
                "🇬🇩": "Flag: Grenada",
                "🇬🇪": "Flag: Georgia",
                "🇬🇫": "Flag: French Guiana",
                "🇬🇬": "Flag: Guernsey",
                "🇬🇭": "Flag: Ghana",
                "🇬🇮": "Flag: Gibraltar",
                "🇬🇱": "Flag: Greenland",
                "🇬🇲": "Flag: Gambia",
                "🇬🇳": "Flag: Guinea",
                "🇬🇵": "Flag: Guadeloupe",
                "🇬🇶": "Flag: Equatorial Guinea",
                "🇬🇷": "Flag: Greece",
                "🇬🇸": "Flag: South Georgia & South Sandwich Islands",
                "🇬🇹": "Flag: Guatemala",
                "🇬🇺": "Flag: Guam",
                "🇬🇼": "Flag: Guinea-Bissau",
                "🇬🇾": "Flag: Guyana",
                "🇭🇰": "Flag: Hong Kong SAR China",
                "🇭🇲": "Flag: Heard & McDonald Islands",
                "🇭🇳": "Flag: Honduras",
                "🇭🇷": "Flag: Croatia",
                "🇭🇹": "Flag: Haiti",
                "🇭🇺": "Flag: Hungary",
                "🇮🇨": "Flag: Canary Islands",
                "🇮🇩": "Flag: Indonesia",
                "🇮🇪": "Flag: Ireland",
                "🇮🇱": "Flag: Israel",
                "🇮🇲": "Flag: Isle of Man",
                "🇮🇳": "Flag: India",
                "🇮🇴": "Flag: British Indian Ocean Territory",
                "🇮🇶": "Flag: Iraq",
                "🇮🇷": "Flag: Iran",
                "🇮🇸": "Flag: Iceland",
                "🇮🇹": "Flag: Italy",
                "🇯🇪": "Flag: Jersey",
                "🇯🇲": "Flag: Jamaica",
                "🇯🇴": "Flag: Jordan",
                "🇯🇵": "Flag: Japan",
                "🇰🇪": "Flag: Kenya",
                "🇰🇬": "Flag: Kyrgyzstan",
                "🇰🇭": "Flag: Cambodia",
                "🇰🇮": "Flag: Kiribati",
                "🇰🇲": "Flag: Comoros",
                "🇰🇳": "Flag: St. Kitts & Nevis",
                "🇰🇵": "Flag: North Korea",
                "🇰🇷": "Flag: South Korea",
                "🇰🇼": "Flag: Kuwait",
                "🇰🇾": "Flag: Cayman Islands",
                "🇰🇿": "Flag: Kazakhstan",
                "🇱🇦": "Flag: Laos",
                "🇱🇧": "Flag: Lebanon",
                "🇱🇨": "Flag: St. Lucia",
                "🇱🇮": "Flag: Liechtenstein",
                "🇱🇰": "Flag: Sri Lanka",
                "🇱🇷": "Flag: Liberia",
                "🇱🇸": "Flag: Lesotho",
                "🇱🇹": "Flag: Lithuania",
                "🇱🇺": "Flag: Luxembourg",
                "🇱🇻": "Flag: Latvia",
                "🇱🇾": "Flag: Libya",
                "🇲🇦": "Flag: Morocco",
                "🇲🇨": "Flag: Monaco",
                "🇲🇩": "Flag: Moldova",
                "🇲🇪": "Flag: Montenegro",
                "🇲🇫": "Flag: St. Martin",
                "🇲🇬": "Flag: Madagascar",
                "🇲🇭": "Flag: Marshall Islands",
                "🇲🇰": "Flag: North Macedonia",
                "🇲🇱": "Flag: Mali",
                "🇲🇲": "Flag: Myanmar (Burma)",
                "🇲🇳": "Flag: Mongolia",
                "🇲🇴": "Flag: Macao Sar China",
                "🇲🇵": "Flag: Northern Mariana Islands",
                "🇲🇶": "Flag: Martinique",
                "🇲🇷": "Flag: Mauritania",
                "🇲🇸": "Flag: Montserrat",
                "🇲🇹": "Flag: Malta",
                "🇲🇺": "Flag: Mauritius",
                "🇲🇻": "Flag: Maldives",
                "🇲🇼": "Flag: Malawi",
                "🇲🇽": "Flag: Mexico",
                "🇲🇾": "Flag: Malaysia",
                "🇲🇿": "Flag: Mozambique",
                "🇳🇦": "Flag: Namibia",
                "🇳🇨": "Flag: New Caledonia",
                "🇳🇪": "Flag: Niger",
                "🇳🇫": "Flag: Norfolk Island",
                "🇳🇬": "Flag: Nigeria",
                "🇳🇮": "Flag: Nicaragua",
                "🇳🇱": "Flag: Netherlands",
                "🇳🇴": "Flag: Norway",
                "🇳🇵": "Flag: Nepal",
                "🇳🇷": "Flag: Nauru",
                "🇳🇺": "Flag: Niue",
                "🇳🇿": "Flag: New Zealand",
                "🇴🇲": "Flag: Oman",
                "🇵🇦": "Flag: Panama",
                "🇵🇪": "Flag: Peru",
                "🇵🇫": "Flag: French Polynesia",
                "🇵🇬": "Flag: Papua New Guinea",
                "🇵🇭": "Flag: Philippines",
                "🇵🇰": "Flag: Pakistan",
                "🇵🇱": "Flag: Poland",
                "🇵🇲": "Flag: St. Pierre & Miquelon",
                "🇵🇳": "Flag: Pitcairn Islands",
                "🇵🇷": "Flag: Puerto Rico",
                "🇵🇸": "Flag: Palestinian Territories",
                "🇵🇹": "Flag: Portugal",
                "🇵🇼": "Flag: Palau",
                "🇵🇾": "Flag: Paraguay",
                "🇶🇦": "Flag: Qatar",
                "🇷🇪": "Flag: Réunion",
                "🇷🇴": "Flag: Romania",
                "🇷🇸": "Flag: Serbia",
                "🇷🇺": "Flag: Russia",
                "🇷🇼": "Flag: Rwanda",
                "🇸🇦": "Flag: Saudi Arabia",
                "🇸🇧": "Flag: Solomon Islands",
                "🇸🇨": "Flag: Seychelles",
                "🇸🇩": "Flag: Sudan",
                "🇸🇪": "Flag: Sweden",
                "🇸🇬": "Flag: Singapore",
                "🇸🇭": "Flag: St. Helena",
                "🇸🇮": "Flag: Slovenia",
                "🇸🇯": "Flag: Svalbard & Jan Mayen",
                "🇸🇰": "Flag: Slovakia",
                "🇸🇱": "Flag: Sierra Leone",
                "🇸🇲": "Flag: San Marino",
                "🇸🇳": "Flag: Senegal",
                "🇸🇴": "Flag: Somalia",
                "🇸🇷": "Flag: Suriname",
                "🇸🇸": "Flag: South Sudan",
                "🇸🇹": "Flag: São Tomé & Príncipe",
                "🇸🇻": "Flag: El Salvador",
                "🇸🇽": "Flag: Sint Maarten",
                "🇸🇾": "Flag: Syria",
                "🇸🇿": "Flag: Eswatini",
                "🇹🇦": "Flag: Tristan Da Cunha",
                "🇹🇨": "Flag: Turks & Caicos Islands",
                "🇹🇩": "Flag: Chad",
                "🇹🇫": "Flag: French Southern Territories",
                "🇹🇬": "Flag: Togo",
                "🇹🇭": "Flag: Thailand",
                "🇹🇯": "Flag: Tajikistan",
                "🇹🇰": "Flag: Tokelau",
                "🇹🇱": "Flag: Timor-Leste",
                "🇹🇲": "Flag: Turkmenistan",
                "🇹🇳": "Flag: Tunisia",
                "🇹🇴": "Flag: Tonga",
                "🇹🇷": "Flag: Turkey",
                "🇹🇹": "Flag: Trinidad & Tobago",
                "🇹🇻": "Flag: Tuvalu",
                "🇹🇼": "Flag: Taiwan",
                "🇹🇿": "Flag: Tanzania",
                "🇺🇦": "Flag: Ukraine",
                "🇺🇬": "Flag: Uganda",
                "🇺🇲": "Flag: U.S. Outlying Islands",
                "🇺🇳": "Flag: United Nations",
                "🇺🇸": "Flag: United States",
                "🇺🇾": "Flag: Uruguay",
                "🇺🇿": "Flag: Uzbekistan",
                "🇻🇦": "Flag: Vatican City",
                "🇻🇨": "Flag: St. Vincent & Grenadines",
                "🇻🇪": "Flag: Venezuela",
                "🇻🇬": "Flag: British Virgin Islands",
                "🇻🇮": "Flag: U.S. Virgin Islands",
                "🇻🇳": "Flag: Vietnam",
                "🇻🇺": "Flag: Vanuatu",
                "🇼🇫": "Flag: Wallis & Futuna",
                "🇼🇸": "Flag: Samoa",
                "🇽🇰": "Flag: Kosovo",
                "🇾🇪": "Flag: Yemen",
                "🇾🇹": "Flag: Mayotte",
                "🇿🇦": "Flag: South Africa",
                "🇿🇲": "Flag: Zambia",
                "🇿🇼": "Flag: Zimbabwe",
                "🏴󠁧󠁢󠁥󠁮󠁧󠁿": "Flag: England",
                "🏴󠁧󠁢󠁳󠁣󠁴󠁿": "Flag: Scotland",
                "🏴󠁧󠁢󠁷󠁬󠁳󠁿": "Flag: Wales",
                "🏴󠁵󠁳󠁴󠁸󠁿": "Flag for Texas (US-TX)"
            }
        }

        self.total_emojis = {}

        for group, items in self.emojis.items():
            box = QtWidgets.QGroupBox(group)
            layout = QtWidgets.QGridLayout()
            for i, (emoji, name) in enumerate(items.items()):
                # uses a little modified push button which recognizes when the mouse is over the button
                button = self.__QHoverPushButton(text=emoji, parent_emoji_picker=self)

                button.setFlat(True)
                button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                button.setFixedSize(30, 30)
                # the button style
                button.setStyleSheet('QPushButton {'
                                     '  font-size: 20px;'
                                     '  border-radius: 50%%;'
                                     '}'
                                     'QPushButton:hover {'
                                     '  background-color: %s'
                                     '}' % button.palette().button().color().darker().name())
                layout.addWidget(button, int(i / self.items_per_row), i % self.items_per_row)

                # adds the current emoji with its name to a dict where are all emojis without groups are listed
                self.total_emojis[emoji] = name

                box.setLayout(layout)
            self.emoji_scroll_area_vlayout.addWidget(box)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_line_edit = QtWidgets.QLineEdit(Form)
        self.search_line_edit.setObjectName("search_line_edit")
        self.verticalLayout.addWidget(self.search_line_edit)
        self.emoji_scroll_area = QtWidgets.QScrollArea(Form)
        self.emoji_scroll_area.setWidgetResizable(True)
        self.emoji_scroll_area.setObjectName("emoji_scroll_area")
        self.emoji_scroll_area_widgets = QtWidgets.QWidget()
        self.emoji_scroll_area_widgets.setGeometry(QtCore.QRect(0, 0, 384, 198))
        self.emoji_scroll_area_widgets.setObjectName("emoji_scroll_area_widgets")
        self.emoji_scroll_area_vlayout = QtWidgets.QVBoxLayout(self.emoji_scroll_area_widgets)
        self.emoji_scroll_area_vlayout.setObjectName("emoji_scroll_area_vlayout")
        self.emoji_scroll_area.setWidget(self.emoji_scroll_area_widgets)
        self.verticalLayout.addWidget(self.emoji_scroll_area)
        self.emoji_information_hlayout = QtWidgets.QHBoxLayout()
        self.emoji_information_hlayout.setObjectName("emoji_information_hlayout")
        self.emoji_image_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emoji_image_label.sizePolicy().hasHeightForWidth())
        self.emoji_image_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.emoji_image_label.setFont(font)
        self.emoji_image_label.setText("")
        self.emoji_image_label.setObjectName("emoji_image_label")
        self.emoji_information_hlayout.addWidget(self.emoji_image_label)
        self.emoji_name_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emoji_name_label.sizePolicy().hasHeightForWidth())
        self.emoji_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emoji_name_label.setFont(font)
        self.emoji_name_label.setText("")
        self.emoji_name_label.setObjectName("emoji_name_label")
        self.emoji_information_hlayout.addWidget(self.emoji_name_label)
        self.verticalLayout.addLayout(self.emoji_information_hlayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_line_edit.setPlaceholderText(_translate("Form", "Search..."))

    def select(self) -> typing.Union[str, None]:
        """Shows this window and returns the selected emoji if a button was pressed or none, if the window was closed without choosing an emoji"""
        self.exec()
        return self.selected_emoji

    def on_input(self, text: str):
        """This method gets called if the text in the search input changes and selects all emojis which correspond with the search input text"""
        for i in range(self.emoji_scroll_area_vlayout.count()):
            group = self.emoji_scroll_area_vlayout.itemAt(i).widget()
            # hides and deletes the previous 'Search results' group box
            if group.title() == 'Search results':
                group.hide()
                group.deleteLater()
            # if no text is given / the search input is empty, every group which is hidden will be shown
            elif not text and group.isHidden():
                group.show()
            # if a text is given / the search input has text, every group which is not hidden will be shown
            elif text and not group.isHidden():
                group.hide()

        if text:
            search_results = QtWidgets.QGroupBox('Search results')
            layout = QtWidgets.QGridLayout()

            items = -1

            def add_item():
                # `items` is readonly in inner functions, so it can't increased here and has to be increases in the two loop below

                # uses a little modified push button which recognizes when the mouse is over the button
                button = self.__QHoverPushButton(text=emoji, parent_emoji_picker=self)

                button.setFlat(True)
                button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                button.setFixedSize(30, 30)
                # the button style
                button.setStyleSheet('QPushButton {'
                                     '  font-size: 20px;'
                                     '  border-radius: 50%%;'
                                     '}'
                                     'QPushButton:hover {'
                                     '  background-color: %s'
                                     '}' % button.palette().button().color().darker().name())
                layout.addWidget(button, int(items / self.items_per_row), items % self.items_per_row)

            lower_text = text.lower()
            # if `self.performance_search` is True, only emoji names starting with the specified text are displayed
            if self.performance_search:
                for emoji, name in self.total_emojis.items():
                    if name.lower().startswith(lower_text):
                        items += 1
                        add_item()
            # but if `self.performance_search` is False, emoji texts which containing the specified text are displayed
            else:
                for emoji, name in self.total_emojis.items():
                    if lower_text in name.lower():
                        items += 1
                        add_item()

            # adds a spacer below the found emojis to "order" them properly
            layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding), int(items / self.items_per_row) + 1, 0, columnSpan=self.items_per_row)

            search_results.setLayout(layout)
            self.emoji_scroll_area_vlayout.insertWidget(0, search_results)

    class __QHoverPushButton(QtWidgets.QPushButton):
        """A custom QPushButton which detects when a mouse hovers it"""

        def __init__(self, text: str, parent_emoji_picker):
            """
            Args:
                text: The button text
                parent_emoji_picker (QEmojiPicker): The parent emoji picker
            """
            super().__init__(text)
            self.clicked.connect(self.on_click)

            self.parent_emoji_picker = parent_emoji_picker

        def enterEvent(self, a0: QtCore.QEvent) -> None:
            """On mouse hover / when the mouse is over the button"""
            self.parent_emoji_picker.emoji_image_label.setText(self.text())
            group_title = self.parentWidget().title()
            # when the group title is 'Search results' the user has used the search input
            if group_title == 'Search results':
                self.parent_emoji_picker.emoji_name_label.setText(self.parent_emoji_picker.total_emojis[self.text()])
            else:
                self.parent_emoji_picker.emoji_name_label.setText(self.parent_emoji_picker.emojis[group_title][self.text()])

        def leaveEvent(self, a0: QtCore.QEvent) -> None:
            """When the mouse leaves the button"""
            self.parent_emoji_picker.emoji_image_label.setText('')
            self.parent_emoji_picker.emoji_name_label.setText('')

        def on_click(self):
            """Gets called if the button is pressed. Closes the emoji picker and if it was called via `QEmojiPicker.select()` the current button emoji will be returned"""
            self.parent_emoji_picker.selected_emoji = self.text()
            self.parent_emoji_picker.close()


# https://github.com/baoboa/pyqt5/blob/master/examples/layouts/flowlayout.py
class QFlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super().__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self._items = []
        self.__pending_positions = {}

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, a0: QtWidgets.QLayoutItem) -> None:
        try:
            position = self.__pending_positions[a0.widget()]
            self._items.insert(position, a0)
            del self.__pending_positions[a0.widget()]
        except KeyError:
            self._items.append(a0)

    def addWidget(self, w: QtWidgets.QWidget, position: int = None) -> None:
        if position:
            self.__pending_positions[w] = position
        super().addWidget(w)

    def count(self):
        return len(self._items)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))

    def itemAt(self, index: int) -> QtWidgets.QLayoutItem:
        if 0 <= index < len(self._items):
            return self._items[index]

        return None

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height

    def minimumSize(self):
        size = QtCore.QSize()

        for item in self._items:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QtCore.QSize(2 * margin, 2 * margin)
        return size

    def removeItem(self, a0: QtWidgets.QLayoutItem) -> None:
        a0.widget().deleteLater()

    def removeWidget(self, w: QtWidgets.QWidget) -> None:
        w.deleteLater()

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def takeAt(self, index: int) -> QtWidgets.QLayoutItem:
        if 0 <= index < len(self._items):
            return self._items.pop(index)

        return None

    def _doLayout(self, rect, testOnly):
        """This does the layout. Dont ask me how. Source: https://github.com/baoboa/pyqt5/blob/master/examples/layouts/flowlayout.py"""
        x = rect.x()
        y = rect.y()
        line_height = 0

        for item in self._items:
            wid = item.widget()
            space_x = self.spacing() + wid.style().layoutSpacing(
                QtWidgets.QSizePolicy.PushButton,
                QtWidgets.QSizePolicy.PushButton,
                QtCore.Qt.Horizontal)
            space_y = self.spacing() + wid.style().layoutSpacing(
                QtWidgets.QSizePolicy.PushButton,
                QtWidgets.QSizePolicy.PushButton,
                QtCore.Qt.Vertical)
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not testOnly:
                item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()


# https://stackoverflow.com/questions/14780517/toggle-switch-in-qt
class QSwitch(QtWidgets.QAbstractButton):
    def __init__(self, parent=None, track_radius=10, thumb_radius=8):
        super().__init__(parent=parent)
        self.setCheckable(True)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self._track_radius = track_radius
        self._thumb_radius = thumb_radius

        self._margin = max(0, self._thumb_radius - self._track_radius)
        self._base_offset = max(self._thumb_radius, self._track_radius)
        self._end_offset = {
            True: lambda: self.width() - self._base_offset,
            False: lambda: self._base_offset,
        }
        self._offset = self._base_offset

        palette = self.palette()
        if self._thumb_radius > self._track_radius:
            self._track_color = {
                True: palette.highlight(),
                False: palette.dark(),
            }
            self._thumb_color = {
                True: palette.highlight(),
                False: palette.light(),
            }
            self._text_color = {
                True: palette.highlightedText().color(),
                False: palette.dark().color(),
            }
            self._thumb_text = {
                True: '',
                False: '',
            }
            self._track_opacity = 0.5
        else:
            self._thumb_color = {
                True: palette.highlightedText(),
                False: palette.light(),
            }
            self._track_color = {
                True: palette.highlight(),
                False: palette.dark(),
            }
            self._text_color = {
                True: palette.highlight().color(),
                False: palette.dark().color(),
            }
            self._thumb_text = {
                True: '✔',
                False: '✕',
            }
            self._track_opacity = 1

    @QtCore.pyqtProperty(int)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.update()

    def sizeHint(self):  # pylint: disable=invalid-name
        return QtCore.QSize(
            4 * self._track_radius + 2 * self._margin,
            2 * self._track_radius + 2 * self._margin,
        )

    def setChecked(self, checked):
        super().setChecked(checked)
        self.offset = self._end_offset[checked]()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.offset = self._end_offset[self.isChecked()]()

    def paintEvent(self, event):  # pylint: disable=invalid-name, unused-argument
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing, True)
        p.setPen(QtCore.Qt.NoPen)
        track_opacity = self._track_opacity
        thumb_opacity = 1.0
        text_opacity = 1.0
        if self.isEnabled():
            track_brush = self._track_color[self.isChecked()]
            thumb_brush = self._thumb_color[self.isChecked()]
            text_color = self._text_color[self.isChecked()]
        else:
            track_opacity *= 0.8
            track_brush = self.palette().shadow()
            thumb_brush = self.palette().mid()
            text_color = self.palette().shadow().color()

        p.setBrush(track_brush)
        p.setOpacity(track_opacity)
        p.drawRoundedRect(
            self._margin,
            self._margin,
            self.width() - 2 * self._margin,
            self.height() - 2 * self._margin,
            self._track_radius,
            self._track_radius,
        )
        p.setBrush(thumb_brush)
        p.setOpacity(thumb_opacity)
        p.drawEllipse(
            self.offset - self._thumb_radius,
            self._base_offset - self._thumb_radius,
            2 * self._thumb_radius,
            2 * self._thumb_radius,
        )
        p.setPen(text_color)
        p.setOpacity(text_opacity)
        font = p.font()
        font.setPixelSize(int(1.5 * self._thumb_radius))
        p.setFont(font)
        p.drawText(
            QtCore.QRectF(
                self.offset - self._thumb_radius,
                self._base_offset - self._thumb_radius,
                2 * self._thumb_radius,
                2 * self._thumb_radius,
            ),
            QtCore.Qt.AlignCenter,
            self._thumb_text[self.isChecked()],
        )

    def mouseReleaseEvent(self, event):  # pylint: disable=invalid-name
        super().mouseReleaseEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            anim = QtCore.QPropertyAnimation(self, b'offset', self)
            anim.setDuration(120)
            anim.setStartValue(self.offset)
            anim.setEndValue(self._end_offset[self.isChecked()]())
            anim.start()

    def enterEvent(self, event):  # pylint: disable=invalid-name
        self.setCursor(QtCore.Qt.PointingHandCursor)
        super().enterEvent(event)


class QTagEdit(QtWidgets.QScrollArea):
    """A tag based edit"""

    def __init__(self, parent: QtWidgets = None, tag_suggestions: typing.List[str] = []):
        super().__init__(parent)

        # setup the ui stuff
        self.setWidgetResizable(True)

        self._main_widget = QtWidgets.QWidget()
        self._layout = QFlowLayout(self._main_widget)

        self._tag_input = QtWidgets.QLineEdit()
        # self._tag_input.setPlaceholderText('Type in a new tag and hit enter...')
        self._tag_input.setFixedWidth(10)
        self._tag_input.setStyleSheet('border: 0px')
        self._tag_input.setContentsMargins(0, 5, 0, 0)
        self._tag_input.keyReleaseEvent = self.__tag_input_key_release_event

        self._layout.addWidget(self._tag_input)

        self._tag_input.palette().color(QtGui.QPalette.Background)
        tag_input_color = self._tag_input.palette().color(QtGui.QPalette.Background)
        self.setStyleSheet(f'background-color: rgb({tag_input_color.red()}, {tag_input_color.green()}, {tag_input_color.blue()})')

        self.setWidget(self._main_widget)

        # setup all other things
        self.__font_calculator = QtGui.QFontMetrics(QtWidgets.QApplication.font())
        self.__tags = {}
        self.__tag_suggestions = tag_suggestions
        self._tag_suggestions = False
        self._check_for_doubles = True

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        """Sets the focus always to `self._tag_input`"""
        self._tag_input.setFocus()

    def addTag(self, text: str) -> bool:
        """
        Adds a new tag

        Args:
            text: The text of the new tag

        Returns:
            If the tag was added successfully
        """
        # if `self._check_for_doubles` is True, it checks if the tag already exists
        if self._check_for_doubles and text.lower() in (tag.lower() for tag in self.__tags.keys()):
            self.onDoubledTag(text)
            return False
        else:
            # a new tag
            tag = self.__QTagFrame(self, text)
            # tag.setStyleSheet('border: 0px; margin: 0px; padding: 0px')

            self.__tags[text] = tag
            for tag_name in self.__tag_suggestions:
                # if the tag is in `self.__tag_suggestions` it will be removed from there
                if tag_name.lower() == text:
                    self.__tag_suggestions.remove(tag_name)
                    self.enableTagSuggestions(self._tag_suggestions)
                    break
            # insert the tag before the line edit
            self._layout.addWidget(tag, -1)
            return True

    def clear(self, input=True) -> None:
        """
        Clears all tags

        Args:
            input: If True, the current text in the line edit will be cleared as well
        """
        for i in range(self._layout.count()):
            widget = self._layout.itemAt(i).widget()
            if type(widget) == QtWidgets.QLineEdit and input:
                widget.clear()
            elif type(widget) == self.__QTagFrame:
                self.removeTag(widget.text())

    def enableCheckForDoubles(self, check_for_doubles) -> None:
        """
        Enables if a new tag, when its going to be added, should be checked if it already exists

        Args:
            check_for_doubles: True if double checking should be active, False if not
        """
        self._check_for_doubles = check_for_doubles

    def enableTagSuggestions(self, tag_suggestions: bool) -> None:
        """
        Enables whenever a new tag is typed in that suggestions from `self.__tag_suggestions(...)` should be showing or not.
        They can be added on the class initialization or via `setTagSuggestions`

        Args:
            tag_suggestions: If tag suggestions should be active or not
        """
        self._tag_suggestions = tag_suggestions
        if tag_suggestions:
            # sets the completer for the line edit
            completer = QtWidgets.QCompleter(self.__tag_suggestions)
            completer.setCompletionMode(completer.InlineCompletion)
            completer.setCaseSensitivity(QtCore.Qt.CaseSensitive)
            self._tag_input.setCompleter(completer)
        else:
            self._tag_input.setCompleter(None)

    def onDoubledTag(self, text: str) -> None:
        """
        This method gets called if `self._check_for_doubles` is True (can be set via `enableCheckForDoubles(...)`)
        and a new tag which already exists are going to be added.
        This method is actually there to display an error message

        Args:
            text: The text of the new tag
        """
        button = QtWidgets.QMessageBox()

        # if `self.tag_input.keyReleaseEvent`is not overridden, it would trigger itself when the enter key is pressed
        # to close the popup and open it again. idk why
        def reset(a0: QtGui.QKeyEvent):
            if a0.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                button.destroy()
                self._tag_input.keyReleaseEvent = self.__tag_input_key_release_event

        self._tag_input.keyReleaseEvent = reset

        # shows the warning
        button.warning(self, 'Tag already exists', f'The tag {text} already exists')

    def removeTag(self, tag: str) -> None:
        """
        Removes a tag

        Args:
            The tag to remove
        """
        if tag in self.__tags:
            self._layout.removeWidget(self.__tags[tag])
            del self.__tags[tag]

    def setTags(self, tags: typing.List[str]) -> None:
        """
        Replaces all current tags with tag from the `tags` argument

        Args:
            tags: The new tags to be set
        """
        self.clear()
        for tag in tags:
            self.addTag(tag)

    def setTagSuggestions(self, suggestions: typing.List[str]) -> None:
        """
        Sets the tag suggestions. They will be used if `self._tag_suggestions` is True (can be set via `enableTagSuggestions(...)`)
        and will be shown if a new tag is typed in

        Args:
            suggestions: The new tag suggestions
        """
        self.__tag_suggestions = suggestions
        self.enableTagSuggestions(self._tag_suggestions)

    def tags(self) -> typing.Union[typing.List[str]]:
        """
        Returns all tag names

        Returns:
            All tag names
        """
        return list(self.__tags.keys())

    def __tag_input_key_release_event(self, a0: QtGui.QKeyEvent) -> None:
        """
        The `keyReleaseEvent(...)` of the line edit. Whenever return / enter is pressed, the current text in the line edit
        will be added as new tag. It also expands the width of the line edit if the text in it is over an specific limit
        """
        if a0.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            # adds the tag
            if self.addTag(self._tag_input.text()):
                self._tag_input.clear()
                self._tag_input.setFixedWidth(10)
            return
        elif a0.key() in (QtCore.Qt.Key_Backspace, QtCore.Qt.Key_Delete):
            # calculates the current line edit text width
            width = self.__font_calculator.width(self._tag_input.text())
            if width + 10 < self._tag_input.width():
                self._tag_input.setFixedWidth(width + 10)
        else:
            # calculates the current line edit text width
            width = self.__font_calculator.width(self._tag_input.text())
            # this resizes the tag input if the text in it will be longer than it's width.
            # not the best way, but it does what it does
            if width + 20 > self._tag_input.width():
                self._tag_input.setFixedWidth(width + 20)

    class __QTagFrame(QtWidgets.QFrame):
        """The tag class for the QTagEdit tags"""

        def __init__(self, parent, text: str):
            super().__init__()

            # setup the ui stuff
            self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
            self.setLayout(QtWidgets.QHBoxLayout())
            self.setContentsMargins(3, 0, 3, 0)

            # the tag name label
            self._name = QtWidgets.QLabel()
            self._name.setText(text)
            self._name.setStyleSheet('background: transparent')

            # the tag delete button
            self._delete_button = QtWidgets.QPushButton()
            self._delete_button.setStyleSheet('QPushButton {'
                                              '     background: transparent;'
                                              '     border: 0px;'
                                              '}')
            self._delete_button.clicked.connect(self.onDeleteButtonClick)
            self._delete_button.setCursor(QtCore.Qt.PointingHandCursor)

            self.layout().addWidget(self._name)
            self.layout().addWidget(self._delete_button)

            # setup all other things
            self.__parent = parent
            self._text = text

        def onDeleteButtonClick(self) -> None:
            """This will get triggered if the delete button on a tag is pressed"""
            self.__parent.removeTag(self.text())
            self.__parent._tag_input.setFocus()

        def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
            """Styles the tag"""
            dark_color = self.palette().color(QtGui.QPalette.Background).darker()
            light_color = self.palette().color(QtGui.QPalette.Background).lighter()

            painter = QtGui.QPainter(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            painter.setPen(QtGui.QPen(dark_color, 1, QtCore.Qt.SolidLine))
            painter.setBrush(QtGui.QBrush(dark_color, QtCore.Qt.SolidPattern))

            # draws the tag 'filling'
            painter.drawRoundedRect(0, 0, self.width() - 5, self.height(), self.height() / 2, self.height() / 2)
            painter.setPen(QtGui.QPen(dark_color, 1, QtCore.Qt.SolidLine))
            painter.setBrush(QtGui.QBrush(light_color, QtCore.Qt.SolidPattern))
            painter.drawEllipse(QtCore.QPointF(self.width() - 25, self.height() / 2), 8, 8)
            painter.drawText(QtCore.QRectF(self.width() - 35, 0, 20, 30),
                             QtCore.Qt.AlignCenter,
                             '✕')

        def text(self) -> str:
            """
            Returns the current tag text

            Returns:
                The tag text

            """
            return self._text
