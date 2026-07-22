from django import forms
import string

class PaperForm(forms.Form):
    HEADING_CHOICES = [
        ('write_alphabet', 'Write Alphabet'),
        ('matching', 'Matching'),
        ('picture_match', 'Match With Picture'),
        ('Write_first_letter', 'Write first letter of each picture'),
        ('Circle_the_alphabet', 'circle the alphabet'),
        # ('Select_alphabet_to_draw_pic', 'circle the alphabet in this picture'),
    ]
    
    URDU_HEADING_CHOICES = [
        ('urdu_matching', 'کالم ملائیں (Matching)'),
        ('urdu_circle_letter', 'حرف پر دائرہ لگائیں (Circle the Letter)'),
        ('urdu_first_letter', 'تصویر کے پہلے حروف پر دائرہ لگائیں (Circle First Letter)'),
        ('urdu_picture_match', 'تصویر سے ملائیں (Match with Pictures)'),
    ]
    
    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="Select Heading")
    start_alphabet = forms.CharField(max_length=1, label="Start Alphabet")
    end_alphabet = forms.CharField(max_length=1, label="End Alphabet")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")
    circle_alphabet = forms.CharField(label='Letter to Circle',required=False)
    # color = forms.CharField(label='select color to draw',required=False)

class UrduPaperForm(forms.Form):
    URDU_HEADING_CHOICES = [
        ('urdu_write_alphabet', 'حروف لکھیں (Write Alphabet)'),
        ('urdu_matching', 'کالم ملائیں (Matching)'),
        ('urdu_circle_letter', 'حرف پر دائرہ لگائیں (Circle the Letter)'),
        ('urdu_first_letter', 'تصویر کے پہلے حروف پر دائرہ لگائیں (Circle First Letter)'),
        ('urdu_picture_match', 'تصویر سے ملائیں (Match with Pictures)'),
    ]
    
    heading = forms.ChoiceField(choices=URDU_HEADING_CHOICES, label="Select Heading")
    start_alphabet = forms.CharField(max_length=1, label="Start Harf (Letter)")
    end_alphabet = forms.CharField(max_length=1, label="End Harf (Letter)")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")
    circle_alphabet = forms.CharField(label='Harf to Circle (Letter to Circle)', required=False)
    
# forms.py

class MathPaperForm(forms.Form):
    MATH_HEADING_CHOICES = [
        ('circle_correct_number', 'Circle the Correct Number'),
        ('count_and_match', 'Count and Match'),
        ('tick_items', 'Tick the Number of Items'),
        ('match_same_number', 'Match the Same Number'),
    ]
    
    heading = forms.ChoiceField(choices=MATH_HEADING_CHOICES, label="Select Heading")
    start_number = forms.IntegerField(label="Start Number", initial=1)
    end_number = forms.IntegerField(label="End Number", initial=10)
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")
    tick_target = forms.IntegerField(label="Number to Tick (e.g., 5)", initial=5, required=False)
    tick_total = forms.IntegerField(label="Total Items (e.g., 7)", initial=7, required=False)

class NurseryEnglishPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('write_capital_small', 'Write the Capital and Small letter (e.g. Aa to Mm)'),
        ('missing_capital', 'Write the missing capital letters'),
        ('match_picture_letter', 'Match the picture with the letter'),
        ('match_same_letter', 'Match the same letter'),
        ('what_comes_between', 'What comes between'),
        ('circle_right_letter', 'Draw a circle around the right letter'),
        ('nursery_write_first_letter', 'Write the first letter of each picture'),
        ('nursery_write_body_parts', 'Write the parts of body name'),
    ]
    
    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="Select Heading")
    start_alphabet = forms.CharField(max_length=1, label="Start Alphabet")
    end_alphabet = forms.CharField(max_length=1, label="End Alphabet")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")

NURSERY_URDU_ALPHABET = [
    'ا', 'آ', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ڈ',
    'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ',
    'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ہ', 'ء', 'ی', 'ے',
]


class NurseryUrduPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('nursery_urdu_write_alphabet', 'خوش خط حروف تہجی لکھیں'),
        ('nursery_urdu_matching', 'حروف کو آپس میں ملائیں'),
        ('nursery_urdu_after_letters', 'بعد میں آنے والے حروف لکھیں'),
        ('nursery_urdu_picture_matching', 'حروف کو تصویروں کے ساتھ ملائیں'),
        ('nursery_urdu_put_dots', 'حروف کے نقطے لگائیں'),
    ]
    LETTER_CHOICES = [(letter, letter) for letter in NURSERY_URDU_ALPHABET]

    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="سوال منتخب کریں")
    start_letter = forms.ChoiceField(choices=LETTER_CHOICES, label="شروع حرف", initial='ا')
    end_letter = forms.ChoiceField(choices=LETTER_CHOICES, label="آخری حرف", initial='ش')
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")


class NurseryMathPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('nursery_math_write_counting', 'Write the counting 1 to 50'),
        ('nursery_math_between', 'What comes between'),
        ('nursery_math_circle_correct', 'Circle the correct number'),
        ('nursery_math_count_match', 'Count the picture & write the numbers'),
        ('nursery_math_find_and_circle', 'Find and circle the number'),
        ('nursery_math_match_same', 'Match the same number'),
        ('nursery_math_table', 'Write the table of'),
    ]
    
    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="Select Heading")
    start_number = forms.IntegerField(label="Start Number", initial=1, required=False)
    end_number = forms.IntegerField(label="End Number", initial=50, required=False)
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")
    target_number = forms.IntegerField(label="Target Number (for find and circle)", required=False)
    table_number = forms.IntegerField(label="Table Number (e.g., 2)", required=False)
    table_end = forms.IntegerField(label="Table Up To (e.g., 6)", initial=6, required=False)


class NurseryGKPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('gk_header', '❶ G. Knowledge (Section Header)'),
        ('gk_section', '① G. Knowledge (English Questions)'),
        ('gk_urdu_section', '① G. Knowledge (Urdu Questions)'),
        ('speech_section', '② Speech'),
        ('poem_english_section', '③ Poem (English Rhymes)'),
        ('poem_urdu_section', '③ Poem (Urdu Poem)'),
    ]

    GK_ENGLISH_QUESTIONS = [
        ('what_is_your_name', 'What is your name?'),
        ('what_is_your_father_name', "What is your father's name?"),
        ('what_is_your_school_name', 'What is your school name?'),
        ('five_parts_of_body', 'Five parts of body name?'),
        ('what_is_your_mother_name', "What is your mother's name?"),
        ('what_class_do_you_read', 'What class do you read in?'),
        ('how_old_are_you', 'How old are you?'),
        ('what_is_your_teacher_name', "What is your teacher's name?"),
        ('custom_english', 'Custom question (type below)'),
    ]

    GK_URDU_QUESTIONS = [
        ('tum_sab_kon_ho', 'تم سب کون ہیں؟'),
        ('tumhein_kis_ne_paida_kiya', 'تمہیں کس نے پیدا کیا؟'),
        ('tumhara_naam_kya_hai', 'تمہارا نام کیا ہے؟'),
        ('tumhare_abba_ka_naam', 'تمہارے ابا کا نام کیا ہے؟'),
        ('tumhari_ammi_ka_naam', 'تمہاری امی کا نام کیا ہے؟'),
        ('tum_kis_class_mein_parhte_ho', 'تم کس کلاس میں پڑھتے ہو؟'),
        ('custom_urdu', 'Custom question (type below)'),
    ]

    SPEECH_TOPICS = [
        ('my_mother', 'My Mother'),
        ('my_father', 'My Father'),
        ('my_school', 'My School'),
        ('my_teacher', 'My Teacher'),
        ('my_family', 'My Family'),
        ('custom_speech', 'Custom topic (type below)'),
    ]

    POEM_ENGLISH_CHOICES = [
        ('twinkle_twinkle', 'Twinkle twinkle little star'),
        ('baby_baby', 'Baby Baby'),
        ('johny_johny', 'Johny Johny Yes Papa'),
        ('humpty_dumpty', 'Humpty Dumpty'),
        ('jack_and_jill', 'Jack and Jill'),
        ('custom_poem_en', 'Custom poem (type below)'),
    ]

    POEM_URDU_CHOICES = [
        ('allah_sab_se_bara', 'تحسین اے اللہ سب سے بڑا'),
        ('bismillah_ka_bacha', 'بسم اللہ کا بچہ'),
        ('ammi_ki_dua', 'امی کی دعا'),
        ('pyara_nabi', 'پیارا نبی'),
        ('custom_poem_ur', 'Custom poem (type below)'),
    ]

    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="Select Section Type")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")

    # G.K English fields
    gk_question = forms.ChoiceField(choices=GK_ENGLISH_QUESTIONS, label="Select G.K Question", required=False)

    # G.K Urdu fields
    gk_urdu_question = forms.ChoiceField(choices=GK_URDU_QUESTIONS, label="اردو سوال منتخب کریں", required=False)

    # Speech fields
    speech_topic = forms.ChoiceField(choices=SPEECH_TOPICS, label="Select Speech Topic", required=False)

    # Poem English fields
    poem_english_option1 = forms.ChoiceField(choices=POEM_ENGLISH_CHOICES, label="English Poem Option 1", required=False)
    poem_english_option2 = forms.ChoiceField(choices=POEM_ENGLISH_CHOICES, label="English Poem Option 2 (or)", required=False)

    # Poem Urdu fields
    poem_urdu_option1 = forms.ChoiceField(choices=POEM_URDU_CHOICES, label="اردو نظم آپشن 1", required=False)
    poem_urdu_option2 = forms.ChoiceField(choices=POEM_URDU_CHOICES, label="اردو نظم آپشن 2 (یا)", required=False)

    # Custom text field for any custom entry
    custom_text = forms.CharField(label="Custom Text (for custom options)", required=False, max_length=200)


class NurseryDrawingPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('color_it', 'Color it'),
        ('nazra', 'Nazra'),
    ]

    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="Select Heading")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")


class PrepEnglishPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('prep_write_body_parts', 'Write the name of parts of body (Any five)'),
        ('prep_use_of_this', 'Use of "this" (Translate sentences)'),
        ('prep_vowels', 'Vowels (Vowels in the middle)'),
        ('prep_write_fruit_name', 'Write the fruit name (Any five)'),
        ('prep_write_picture_name', 'Write the picture name'),
        ('prep_write_missing_words', 'Write the missing words'),
        ('prep_write_capital_small', 'Write the Capital & small letter "Aa to Zz"'),
    ]

    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="Select Heading")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")

    # Fields for Use of This
    sentence_1 = forms.CharField(label="Sentence 1", initial="یہ ایک کتاب ہے۔", required=False)
    sentence_2 = forms.CharField(label="Sentence 2", initial="یہ ایک اُلو ہے۔", required=False)
    sentence_3 = forms.CharField(label="Sentence 3", initial="یہ ایک شیر ہے۔", required=False)
    sentence_4 = forms.CharField(label="Sentence 4", initial="یہ ایک کتاب ہے۔", required=False)
    sentence_5 = forms.CharField(label="Sentence 5", initial="یہ ایک مالٹا ہے۔", required=False)

    # Fields for Capital & Small Letters
    ALPHABETS = [(c, c) for c in string.ascii_uppercase]
    start_letter = forms.ChoiceField(choices=ALPHABETS, initial='A', required=False, label="Start Letter")
    end_letter = forms.ChoiceField(choices=ALPHABETS, initial='Z', required=False, label="End Letter")


class PrepMathPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('prep_math_counting', 'Write the counting "1" to "50".'),
        ('prep_math_english_urdu', 'Write counting in English and Urdu.'),
        ('prep_math_shapes', 'Write the shapes name.'),
        ('prep_math_before', 'What comes before..'),
        ('prep_math_count_write', 'Count the picture & write the numbers.'),
        ('prep_math_table', 'Write the table of'),
        ('prep_math_circle_correct', 'Circle the correct number'),
    ]

    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="Select Heading")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")

    # Fields for counting
    start_num = forms.IntegerField(label="Start Number", initial=1, required=False)
    end_num = forms.IntegerField(label="End Number", initial=50, required=False)

    # Fields for What comes before
    before_n1 = forms.IntegerField(label="Number 1", initial=3, required=False)
    before_n2 = forms.IntegerField(label="Number 2", initial=9, required=False)
    before_n3 = forms.IntegerField(label="Number 3", initial=12, required=False)
    before_n4 = forms.IntegerField(label="Number 4", initial=17, required=False)
    before_n5 = forms.IntegerField(label="Number 5", initial=20, required=False)
    before_n6 = forms.IntegerField(label="Number 6", initial=23, required=False)
    before_n7 = forms.IntegerField(label="Number 7", initial=26, required=False)
    before_n8 = forms.IntegerField(label="Number 8", initial=28, required=False)
    before_n9 = forms.IntegerField(label="Number 9", initial=30, required=False)
    before_n10 = forms.IntegerField(label="Number 10", initial=33, required=False)

    # Fields for Table
    table_number = forms.IntegerField(label="Table Number (e.g., 2)", initial=2, required=False)
    table_end = forms.IntegerField(label="Table Up To (e.g., 10)", initial=10, required=False)


class PrepUrduPaperForm(forms.Form):
    HEADING_CHOICES = [
        ('prep_urdu_write_alphabet', 'حروف تہجی لکھیں (Write Alphabet)'),
        ('prep_urdu_same_sound', 'اکی آواز (Same Sound)'),
        ('prep_urdu_picture_name', 'تصویر کے درست نام پر (✓) لگائیں (Tick Correct Picture Name)'),
        ('prep_urdu_after_letters', 'بعد میں آنے والے حروف لکھیں (After Letters)'),
        ('prep_urdu_name_class', 'اپنا نام لکھیں اور کلاس کا نام لکھیں (Name and Class)'),
        ('prep_urdu_dictation', 'املا لکھیں (Dictation)'),
        ('prep_urdu_half_shapes', 'حروف تہجی کی آدھی اشکال لکھیں (Half Shapes)'),
        ('prep_urdu_break_words', 'جوڑ کے توڑ لکھیں (Break the words)'),
        ('prep_urdu_matching', 'کالم ملائیں (Matching)'),
        ('prep_urdu_color_names', 'کوئی سے چار رنگوں کے نام لکھیں (Color Names)'),
        ('prep_urdu_oral', 'Urdu Oral (اردو زبانی)'),
    ]

    LETTER_CHOICES = [(letter, letter) for letter in NURSERY_URDU_ALPHABET]

    heading = forms.ChoiceField(choices=HEADING_CHOICES, label="سوال منتخب کریں")
    question_no = forms.IntegerField(label="Question No")
    marks = forms.IntegerField(label="Marks")

    # Fields for Write Alphabet
    start_letter = forms.ChoiceField(choices=LETTER_CHOICES, label="شروع حرف", initial='ا', required=False)
    end_letter = forms.ChoiceField(choices=LETTER_CHOICES, label="آخری حرف", initial='ش', required=False)

    # Shared range selection for Write Alphabet and Same Sound
    # (start_letter and end_letter already defined above are used)
