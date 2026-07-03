from django import forms

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
