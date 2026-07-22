from doctest import Example
import string
import random
from django.shortcuts import render, redirect,HttpResponse
from django.http import HttpResponse
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import os
from .forms import PaperForm, UrduPaperForm, MathPaperForm, NurseryEnglishPaperForm, NurseryUrduPaperForm, NurseryMathPaperForm, NurseryDrawingPaperForm, NurseryGKPaperForm, NURSERY_URDU_ALPHABET, PrepEnglishPaperForm, PrepMathPaperForm, PrepUrduPaperForm


from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
def select_class_subject(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        class_name = request.POST.get("class_name")
        exam = request.POST.get('exam')
        year = request.POST.get('year')

        # Condition for English
        if class_name == "Play" and subject == "English":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("paper")  # English paper URL name

        # Condition for Nursery English
        elif class_name == "Nursery" and subject == "English":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("nursery_english")  # Nursery English paper URL name

        # Condition for Nursery Urdu
        elif class_name == "Nursery" and subject == "Urdu":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("nursery_urdu")  # Nursery Urdu paper URL name

        # Condition for Nursery Math
        elif class_name == "Nursery" and subject == "Math":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("nursery_math")  # Nursery Math paper URL name

        # Condition for Nursery Drawing
        elif class_name == "Nursery" and subject == "Drawing":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("nursery_drawing")  # Nursery Drawing paper URL name

        # Condition for Nursery G.K, Poem & Speech
        elif class_name == "Nursery" and subject == "G.K, Poem & Speech":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("nursery_gk")  # Nursery G.K, Poem & Speech paper URL name

        # Condition for Urdu
        elif class_name == "Play" and subject == "Urdu":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year
        
            return redirect("urdu")  # Urdu paper URL name

        # Condition for Math
        elif class_name == "Play" and subject == "Math":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year
        
            return redirect("math")  # Math paper URL name

        # Condition for Prep English
        elif class_name == "Prep" and subject == "English":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("prep_english")  # Prep English paper URL name
        # Condition for Prep Math
        elif class_name == "Prep" and subject == "Math":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("prep_math")  # Prep Math paper URL name

        # Condition for Prep Urdu
        elif class_name == "Prep" and subject == "Urdu":
            request.session['subject'] = subject
            request.session['class_name'] = class_name
            request.session['exam'] = exam
            request.session['year'] = year

            return redirect("prep_urdu")  # Prep Urdu paper URL name
        
        # If no match, reload same page
        return render(request, "select_class/info.html")

    # If GET request or other
    return render(request, "select_class/info.html")

def paper_generator(request):
    form = PaperForm()

    # GET subject and class from session
    subject = request.session.get('subject', 'Unknown Subject')
    class_name = request.session.get('class_name', 'Unknown Class')
    year = request.session.get('year', 'Unknown Class')
    exam = request.session.get('exam', 'Unknown Class')

    # session setup
    if 'all_questions' not in request.session:
        request.session['all_questions'] = []
    all_questions = request.session['all_questions']

    images = []
    heading = None
    question_no = None
    marks = None
    left_letters = []
    right_letters = []
    worksheet_items = []

    if request.method == "POST":
        form = PaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            start = form.cleaned_data['start_alphabet'].upper()
            end = form.cleaned_data['end_alphabet'].upper()
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            alphabet_list = list(string.ascii_uppercase)
            start_index = alphabet_list.index(start)
            end_index = alphabet_list.index(end)
            selected_range = alphabet_list[start_index:end_index + 1]

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
                'images': [],
                'left_letters': [],
                'right_letters': [],
                'worksheet_items': []
            }

            if heading == "write_alphabet":
                for letter in selected_range:
                    question_data['images'].append(f"images/{letter}.png")

            elif heading == "matching":
                if len(selected_range) > 5:
                    selected_range = random.sample(selected_range, 5)

                question_data['left_letters'] = selected_range[:]
                random.shuffle(question_data['left_letters'])

                question_data['right_letters'] = selected_range[:]
                random.shuffle(question_data['right_letters'])

            elif heading == "picture_match":
                if len(selected_range) > 5:
                    selected_range = random.sample(selected_range, 5)

                question_data['left_letters'] = selected_range[:]
                random.shuffle(question_data['left_letters'])

                shuffled_for_images = selected_range[:]
                random.shuffle(shuffled_for_images)
                for letter in shuffled_for_images:
                    question_data['images'].append(f"pics/{letter}.png")

            elif heading == "Write_first_letter":
                if len(selected_range) > 4:
                    selected_range = random.sample(selected_range, 4)

                for letter in selected_range:
                    question_data['worksheet_items'].append({
                        "image": f"pics/{letter}.png",
                        "letter": letter
                    })

            elif heading == "Circle_the_alphabet":
                target_letter = form.cleaned_data['circle_alphabet'].upper()

                grid_letters = [random.choice(selected_range) for _ in range(16)]
                for _ in range(7):
                    pos = random.randint(0, 15)
                    grid_letters[pos] = target_letter

                question_data.update({
                    'target_letter': target_letter,
                    'grid': grid_letters,
                })

            all_questions.append(question_data)
            request.session['all_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/english_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam':exam,
        'year':year,
        
            
    })





# Urdu alphabet list with exact order and correct image filenames
URDU_ALPHABET_MAP = {
    'ا': 'ا.png',
    'ب': 'ب.png',
    'پ': 'پ.png',
    'ت': 'ت.png',
    'ٹ': 'ٹ.png',
    'ث': 'ث.png',
    'ج': 'ج.png',
    'چ': 'چ.png',
    'ح': 'ح.png',
    'خ': 'خ.png',
    'د': 'د.png',
    'ڈ': 'ڈ.png',
    'ذ': 'ذ.png',
    'ر': 'ر.png',
    'ڑ': 'ڑ.png',
    'ز': 'ز.png',
    'ژ': 'ژ.png',
    'س': 'س.png',
    'ش': 'ش.png',
    'ص': 'ص.png',
    'ض': 'ض.png',
    'ط': 'ط.png',
    'ظ': 'ظ.png',
    'ع': 'ع.png',
    'غ': 'غ.png',
    'ف': 'ف.png',
    'ق': 'ق.png',
    'ک': 'ک.png',
    'گ': 'گ.png',
    'ل': 'ل.png',
    'م': 'م.png',
    'ن': 'ن.png',
    'و': 'و.png',
    'ہ': 'ہ.png',
    'ء': 'ء.png',
    'ی': 'ی.png',
    'ے': 'ے.png',
}

URDU_ALPHABET = list(URDU_ALPHABET_MAP.keys())

# Vocabulary images for picture matching and first letter questions
URDU_VOCAB_MAP = {
    'ا': 'alif.png', 'ب': 'Bay.png', 'پ': 'Pay.png', 'ت': 'Tay.png', 'ٹ': 'TTay.png',
    'ث': 'Say.png', 'ج': 'Jeem.png', 'چ': 'Chay.png', 'ح': 'Hay.png', 'خ': 'Khay.png',
    'د': 'Daal.png', 'ڈ': 'DDal.png', 'ذ': 'Zaal.png', 'ر': 'Ray.png', 'ڑ': 'RRay.png',
    'ز': 'Zay.png', 'ژ': 'SSay.png', 'س': 'Seen.png', 'ش': 'Sheen.png', 'ص': 'Suaad.png',
    'ض': 'Zuaad.png', 'ط': 'Toay.png', 'ظ': 'Zoay.png', 'ع': 'Ain.png', 'غ': 'Ghain.png',
    'ف': 'Fay.png', 'ق': 'Qaaf.png', 'ک': 'Kaaf.png', 'گ': 'Gaaf.png', 'ل': 'Laam.png',
    'م': 'Meem.png', 'ن': 'Noon.png', 'و': 'Wao.png', 'ہ': 'HHay.png'
}

def urdu_paper(request):
    form = UrduPaperForm()

    # GET subject and class from session
    subject = request.session.get('subject', 'Unknown Subject')
    class_name = request.session.get('class_name', 'Unknown Class')
    year = request.session.get('year', 'Unknown Class')
    exam = request.session.get('exam', 'Unknown Class')

    # session setup
    if 'urdu_questions' not in request.session:
        request.session['urdu_questions'] = []
    all_questions = request.session['urdu_questions']

    images = []
    heading = None
    question_no = None
    marks = None
    left_letters = []
    right_letters = []
    worksheet_items = []

    if request.method == "POST":
        form = UrduPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            start = form.cleaned_data['start_alphabet']
            end = form.cleaned_data['end_alphabet']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            # Get Urdu alphabet range
            try:
                start_index = URDU_ALPHABET.index(start)
                end_index = URDU_ALPHABET.index(end)
                selected_range = URDU_ALPHABET[start_index:end_index + 1]
            except ValueError:
                selected_range = URDU_ALPHABET[:10]  # Default to first 10 if invalid

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
                'images': [],
                'left_letters': [],
                'right_letters': [],
                'worksheet_items': []
            }

            if heading == "urdu_write_alphabet":
                for letter in selected_range:
                    image_file = URDU_ALPHABET_MAP.get(letter, f"{letter}.png")
                    question_data['images'].append(f"urdu_img/urdu/{image_file}")

            elif heading == "urdu_matching":
                if len(selected_range) > 5:
                    selected_range = random.sample(selected_range, 5)

                question_data['left_letters'] = selected_range[:]
                random.shuffle(question_data['left_letters'])

                question_data['right_letters'] = selected_range[:]
                random.shuffle(question_data['right_letters'])

            elif heading == "urdu_picture_match":
                if len(selected_range) > 5:
                    selected_range = random.sample(selected_range, 5)

                # Letters on right side (shuffled)
                question_data['right_letters'] = selected_range[:]
                random.shuffle(question_data['right_letters'])

                # Images on left side (shuffled)
                shuffled_for_images = selected_range[:]
                random.shuffle(shuffled_for_images)
                question_data['left_letters'] = [l for l in shuffled_for_images]
                for letter in shuffled_for_images:
                    vocab_file = URDU_VOCAB_MAP.get(letter)
                    if vocab_file:
                        question_data['images'].append(f"urdu_img/{vocab_file}")
                    else:
                        image_file = URDU_ALPHABET_MAP.get(letter, f"{letter}.png")
                        question_data['images'].append(f"urdu_img/urdu/{image_file}")

            elif heading == "urdu_first_letter":
                if len(selected_range) > 4:
                    selected_range = random.sample(selected_range, 4)

                for letter in selected_range:
                    # Add 2 random distractor letters (total 3 options like paper)
                    distractors = random.sample([l for l in URDU_ALPHABET if l != letter], 2)
                    options = [letter] + distractors
                    random.shuffle(options)
                    
                    vocab_file = URDU_VOCAB_MAP.get(letter)
                    if vocab_file:
                        image_path = f"urdu_img/{vocab_file}"
                    else:
                        image_file = URDU_ALPHABET_MAP.get(letter, f"{letter}.png")
                        image_path = f"urdu_img/urdu/{image_file}"

                    question_data['worksheet_items'].append({
                        "image": image_path,
                        "letter": letter,
                        "options": options
                    })

            elif heading == "urdu_circle_letter":
                target_letter = form.cleaned_data['circle_alphabet']

                # Generate 4x5 grid (20 cells) with mixed letters
                other_letters = [l for l in selected_range if l != target_letter]
                if not other_letters:
                    other_letters = [l for l in URDU_ALPHABET if l != target_letter]
                
                grid_letters = [random.choice(other_letters) for _ in range(20)]
                # Place target letter in ~8 random positions
                target_positions = random.sample(range(20), min(8, 20))
                for pos in target_positions:
                    grid_letters[pos] = target_letter

                question_data.update({
                    'target_letter': target_letter,
                    'grid': grid_letters,
                })

            all_questions.append(question_data)
            request.session['urdu_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/urdu_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam':exam,
        'year':year,
        
            
    })

def reset_paper(request):
    """Reset all questions in session"""
    if 'all_questions' in request.session:
        del request.session['all_questions']
    return redirect('paper')

def reset_urdu_paper(request):
    """Reset all Urdu questions in session"""
    if 'urdu_questions' in request.session:
        del request.session['urdu_questions']
    return redirect('urdu')


# Plural names mapping for dynamic headings
ITEM_NAMES = {
    'A': 'apples', 'B': 'balloons', 'C': 'cats', 'D': 'dogs',
    'E': 'eggs', 'F': 'fish', 'G': 'grapes', 'H': 'hats',
    'I': 'ice creams', 'J': 'jugs', 'K': 'kites', 'L': 'leaves',
    'M': 'mangoes', 'O': 'oranges', 'P': 'pears', 'Q': 'queens',
    'R': 'rabbits', 'S': 'stars', 'T': 'trees', 'U': 'umbrellas',
    'V': 'vans', 'W': 'watches', 'X': 'xylophones', 'Y': 'yachts',
    'Z': 'zebras'
}

def math_paper(request):
    form = MathPaperForm()

    subject = request.session.get('subject', 'Math')
    class_name = request.session.get('class_name', 'Play')
    year = request.session.get('year', '2026')
    exam = request.session.get('exam', 'First Term')

    if 'math_questions' not in request.session:
        request.session['math_questions'] = []
    all_questions = request.session['math_questions']

    if request.method == "POST":
        form = MathPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            start_num = form.cleaned_data['start_number']
            end_num = form.cleaned_data['end_number']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
                'sub_items': [],
                'matching_left': [],
                'matching_right': [],
                'tick_data': {}
            }

            # Pre-select A-Z letters
            alphabet_list = list(string.ascii_uppercase)

            if heading == "circle_correct_number":
                chosen_nums = [random.randint(start_num, end_num) for _ in range(4)]
                chosen_letters = random.sample(alphabet_list, 4)
                
                for i in range(4):
                    target_count = chosen_nums[i]
                    letter = chosen_letters[i]
                    image_path = f"pics/{letter}.png"
                    
                    distractors = []
                    while len(distractors) < 2:
                        dist = random.randint(start_num, end_num)
                        if dist != target_count and dist not in distractors:
                            distractors.append(dist)
                    
                    options = [target_count] + distractors
                    random.shuffle(options)
                    
                    question_data['sub_items'].append({
                        'image': image_path,
                        'count': target_count,
                        'count_range': list(range(target_count)),
                        'options': options
                    })

            elif heading == "count_and_match":
                range_nums = list(range(start_num, end_num + 1))
                if len(range_nums) < 5:
                    range_nums = list(range(1, 10))
                
                chosen_nums = random.sample(range_nums, 5)
                chosen_letters = random.sample(alphabet_list, 5)
                
                left_items = []
                for i in range(5):
                    target_count = chosen_nums[i]
                    letter = chosen_letters[i]
                    image_path = f"pics/{letter}.png"
                    left_items.append({
                        'count': target_count,
                        'count_range': list(range(target_count)),
                        'image': image_path
                    })
                
                shuffled_left = left_items[:]
                random.shuffle(shuffled_left)
                
                shuffled_right = chosen_nums[:]
                random.shuffle(shuffled_right)
                
                question_data['matching_left'] = shuffled_left
                question_data['matching_right'] = shuffled_right

            elif heading == "tick_items":
                tick_target = form.cleaned_data.get('tick_target', 5)
                tick_total = form.cleaned_data.get('tick_total', 7)
                
                letter = random.choice(alphabet_list)
                image_path = f"pics/{letter}.png"
                item_name = ITEM_NAMES.get(letter, 'objects')
                
                question_data['tick_data'] = {
                    'target': tick_target,
                    'total': tick_total,
                    'image': image_path,
                    'item_name': item_name,
                    'total_range': list(range(tick_total))
                }

            elif heading == "match_same_number":
                range_nums = list(range(start_num, end_num + 1))
                if len(range_nums) < 5:
                    range_nums = list(range(1, 10))
                
                chosen_nums = random.sample(range_nums, 5)
                
                left_nums = chosen_nums[:]
                random.shuffle(left_nums)
                
                right_nums = chosen_nums[:]
                random.shuffle(right_nums)
                
                question_data['matching_left'] = left_nums
                question_data['matching_right'] = right_nums

            all_questions.append(question_data)
            request.session['math_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/math_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })

def reset_math_paper(request):
    """Reset all Math questions in session"""
    if 'math_questions' in request.session:
        del request.session['math_questions']
    return redirect('math')

def nursery_english_paper(request):
    form = NurseryEnglishPaperForm()

    subject = request.session.get('subject', 'English')
    class_name = request.session.get('class_name', 'Nursery')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'nursery_questions' not in request.session:
        request.session['nursery_questions'] = []
    all_questions = request.session['nursery_questions']

    if request.method == "POST":
        form = NurseryEnglishPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            start = form.cleaned_data['start_alphabet'].upper()
            end = form.cleaned_data['end_alphabet'].upper()
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            alphabet_list = list(string.ascii_uppercase)
            start_index = alphabet_list.index(start) if start in alphabet_list else 0
            end_index = alphabet_list.index(end) if end in alphabet_list else len(alphabet_list) - 1
            selected_range = alphabet_list[start_index:end_index + 1]

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
                'start_alphabet': start,
                'end_alphabet': end,
                'left_letters': [],
                'right_letters': [],
                'worksheet_items': [],
                'missing_items': []
            }

            if heading == "write_capital_small":
                num_letters = len(selected_range)
                num_rows = (num_letters + 3) // 4
                if num_rows < 1:
                    num_rows = 1
                question_data['num_rows'] = list(range(num_rows))

            elif heading == "missing_capital":
                i = 0
                while i < len(selected_range) and len(question_data['missing_items']) < 5:
                    first_letter = selected_range[i]
                    second_letter = selected_range[i+1] if i+1 < len(selected_range) else ""
                    question_data['missing_items'].append({
                        'prompt_capital': first_letter.upper(),
                        'prompt_small': first_letter.lower(),
                        'target_capital': second_letter.upper(),
                        'target_small': second_letter.lower(),
                    })
                    i += 2

            elif heading == "match_picture_letter":
                chosen_letters = selected_range[:]
                if len(chosen_letters) > 5:
                    chosen_letters = random.sample(chosen_letters, 5)
                
                left_letters = chosen_letters[:]
                random.shuffle(left_letters)
                question_data['left_letters'] = left_letters

                shuffled_for_images = chosen_letters[:]
                random.shuffle(shuffled_for_images)
                for letter in shuffled_for_images:
                    question_data['worksheet_items'].append({
                        "image": f"pics/{letter}.png",
                        "letter": letter
                    })

            elif heading == "match_same_letter":
                chosen_letters = selected_range[:]
                if len(chosen_letters) > 5:
                    chosen_letters = random.sample(chosen_letters, 5)

                left_letters = [l.upper() for l in chosen_letters]
                random.shuffle(left_letters)
                question_data['left_letters'] = left_letters

                right_letters = [l.lower() for l in chosen_letters]
                random.shuffle(right_letters)
                question_data['right_letters'] = right_letters

            elif heading == "what_comes_between":
                # Build all possible triplets (non-overlapping randomly picked)
                all_triplets = []
                for idx in range(0, len(selected_range) - 2):
                    all_triplets.append({
                        'first': selected_range[idx],
                        'last': selected_range[idx + 2],
                    })
                # Randomly pick 5 non-consecutive triplets
                if len(all_triplets) > 5:
                    random.shuffle(all_triplets)
                    picked = []
                    used_firsts = set()
                    for t in all_triplets:
                        if t['first'] not in used_firsts and t['last'] not in used_firsts:
                            picked.append(t)
                            used_firsts.add(t['first'])
                            used_firsts.add(t['last'])
                        if len(picked) >= 5:
                            break
                    # If we couldn't get 5 unique, fill from remaining
                    if len(picked) < 5:
                        for t in all_triplets:
                            if t not in picked:
                                picked.append(t)
                            if len(picked) >= 5:
                                break
                    between_items = picked
                else:
                    between_items = all_triplets
                question_data['between_items'] = between_items

            elif heading == "circle_right_letter":
                chosen_letters = selected_range[:]
                if len(chosen_letters) > 4:
                    chosen_letters = random.sample(chosen_letters, 4)
                circle_items = []
                all_upper = list(string.ascii_uppercase)
                for letter in chosen_letters:
                    correct = letter.upper()
                    wrong_pool = [x for x in all_upper if x != correct]
                    wrong = random.choice(wrong_pool)
                    circle_items.append({
                        'image': f"pics/{letter}.png",
                        'letter': letter,
                        'option1': correct,
                        'option2': wrong,
                    })
                question_data['circle_items'] = circle_items

            elif heading == "nursery_write_first_letter":
                default_letters = ['A', 'B', 'O', 'E']
                chosen_letters = []
                for letter in default_letters:
                    if letter in selected_range:
                        chosen_letters.append(letter)
                if len(chosen_letters) < 4:
                    remaining = [x for x in selected_range if x not in chosen_letters]
                    needed = 4 - len(chosen_letters)
                    chosen_letters.extend(random.sample(remaining, min(needed, len(remaining))))
                if not chosen_letters:
                    chosen_letters = ['A', 'B', 'O', 'E']
                while len(chosen_letters) < 4:
                    chosen_letters.append(random.choice(selected_range))
                
                for letter in chosen_letters[:4]:
                    question_data['worksheet_items'].append({
                        "image": f"pics/{letter}.png",
                        "letter": letter
                    })

            elif heading == "nursery_write_body_parts":
                question_data['body_parts'] = [
                    {'image': 'pics/eye.png', 'name': 'Eye'},
                    {'image': 'pics/lips.png', 'name': 'Lips'},
                    {'image': 'pics/ear.png', 'name': 'Ear'},
                    {'image': 'pics/nose.png', 'name': 'Nose'},
                    {'image': 'pics/hand.png', 'name': 'Hand'},
                ]

            all_questions.append(question_data)
            request.session['nursery_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/nursery_english_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })

def reset_nursery_english_paper(request):
    if 'nursery_questions' in request.session:
        del request.session['nursery_questions']
    return redirect('nursery_english')


def nursery_gk_paper(request):
    form = NurseryGKPaperForm()

    subject = request.session.get('subject', 'G.K, Poem & Speech')
    class_name = request.session.get('class_name', 'Nursery')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'nursery_gk_questions' not in request.session:
        request.session['nursery_gk_questions'] = []
    all_questions = request.session['nursery_gk_questions']

    # Build lookup dicts from form choices for display text
    gk_en_dict = dict(NurseryGKPaperForm.GK_ENGLISH_QUESTIONS)
    gk_ur_dict = dict(NurseryGKPaperForm.GK_URDU_QUESTIONS)
    speech_dict = dict(NurseryGKPaperForm.SPEECH_TOPICS)
    poem_en_dict = dict(NurseryGKPaperForm.POEM_ENGLISH_CHOICES)
    poem_ur_dict = dict(NurseryGKPaperForm.POEM_URDU_CHOICES)

    if request.method == "POST":
        form = NurseryGKPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']
            custom_text = form.cleaned_data.get('custom_text', '')

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
            }

            if heading == 'gk_section':
                gk_key = form.cleaned_data.get('gk_question', '')
                if gk_key == 'custom_english' and custom_text:
                    question_data['question_text'] = custom_text
                else:
                    question_data['question_text'] = gk_en_dict.get(gk_key, '')

            elif heading == 'gk_urdu_section':
                gk_ur_key = form.cleaned_data.get('gk_urdu_question', '')
                if gk_ur_key == 'custom_urdu' and custom_text:
                    question_data['question_text'] = custom_text
                else:
                    question_data['question_text'] = gk_ur_dict.get(gk_ur_key, '')

            elif heading == 'speech_section':
                speech_key = form.cleaned_data.get('speech_topic', '')
                if speech_key == 'custom_speech' and custom_text:
                    question_data['speech_title'] = custom_text
                else:
                    question_data['speech_title'] = speech_dict.get(speech_key, '')

            elif heading == 'poem_english_section':
                poem1_key = form.cleaned_data.get('poem_english_option1', '')
                poem2_key = form.cleaned_data.get('poem_english_option2', '')
                if poem1_key == 'custom_poem_en' and custom_text:
                    question_data['poem_option1'] = custom_text
                else:
                    question_data['poem_option1'] = poem_en_dict.get(poem1_key, '')
                if poem2_key == 'custom_poem_en' and custom_text:
                    question_data['poem_option2'] = custom_text
                else:
                    question_data['poem_option2'] = poem_en_dict.get(poem2_key, '')

            elif heading == 'poem_urdu_section':
                poem_ur1_key = form.cleaned_data.get('poem_urdu_option1', '')
                poem_ur2_key = form.cleaned_data.get('poem_urdu_option2', '')
                if poem_ur1_key == 'custom_poem_ur' and custom_text:
                    question_data['poem_option1'] = custom_text
                else:
                    question_data['poem_option1'] = poem_ur_dict.get(poem_ur1_key, '')
                if poem_ur2_key == 'custom_poem_ur' and custom_text:
                    question_data['poem_option2'] = custom_text
                else:
                    question_data['poem_option2'] = poem_ur_dict.get(poem_ur2_key, '')

            all_questions.append(question_data)
            request.session['nursery_gk_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/nursery_gk_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })

def reset_nursery_gk_paper(request):
    if 'nursery_gk_questions' in request.session:
        del request.session['nursery_gk_questions']
    return redirect('nursery_gk')


def _default_nursery_urdu_questions():
    default_letters = _nursery_urdu_letter_range('ا', 'ش')
    default_matching_letters = random.sample(default_letters, 5)
    default_matching_left = default_matching_letters[:]
    default_matching_right = default_matching_letters[:]
    random.shuffle(default_matching_left)
    random.shuffle(default_matching_right)

    rows_data = []
    for i in range(0, len(default_letters), 5):
        rows_data.append(default_letters[i:i+5])

    # Default for Q3 (After Letters)
    default_after_letters = ['پ', 'ت', 'ب', 'س']
    after_items = [{'letter': l} for l in default_after_letters]

    # Default for Q4 (Picture Matching)
    default_pic_match_letters = ['ا', 'ب', 'پ', 'ت', 'س']
    shuffled_pic_letters = default_pic_match_letters[:]
    random.shuffle(shuffled_pic_letters)
    pic_match_images = []
    for letter in shuffled_pic_letters:
        if letter == 'ا':
            pic_match_images.append("urdu_img/urdu/alif.png")
        else:
            vocab_file = URDU_VOCAB_MAP.get(letter)
            pic_match_images.append(f"urdu_img/{vocab_file}")
            
    shuffled_text_letters = default_pic_match_letters[:]
    random.shuffle(shuffled_text_letters)

    # Default for Q5 (Put Dots)
    dots_rows = [
        ['ٮ', 'ٮ', 'ٮ', 'ٮ', 'ٮ'],
        ['ح', 'ح', 'ح'],
        ['ر', 'ر', 'د', 'د'],
        ['ص', 'س']
    ]

    return [
        {
            'heading': 'nursery_urdu_write_alphabet',
            'question_no': 1,
            'marks': 10,
            'start_letter': 'ا',
            'end_letter': 'ش',
            'rows_data': rows_data,
        },
        {
            'heading': 'nursery_urdu_matching',
            'question_no': 2,
            'marks': 10,
            'left_letters': default_matching_left,
            'right_letters': default_matching_right,
        },
        {
            'heading': 'nursery_urdu_after_letters',
            'question_no': 3,
            'marks': 10,
            'items': after_items,
        },
        {
            'heading': 'nursery_urdu_picture_matching',
            'question_no': 4,
            'marks': 10,
            'left_images': pic_match_images,
            'right_letters': shuffled_text_letters,
        },
        {
            'heading': 'nursery_urdu_put_dots',
            'question_no': 5,
            'marks': 10,
            'rows': dots_rows,
        },
    ]


def _nursery_urdu_letter_range(start_letter, end_letter):
    try:
        start_index = NURSERY_URDU_ALPHABET.index(start_letter)
        end_index = NURSERY_URDU_ALPHABET.index(end_letter)
    except ValueError:
        return NURSERY_URDU_ALPHABET[:5]

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    return NURSERY_URDU_ALPHABET[start_index:end_index + 1]


def nursery_urdu_paper(request):
    form = NurseryUrduPaperForm()

    subject = request.session.get('subject', 'Urdu')
    class_name = request.session.get('class_name', 'Nursery')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'nursery_urdu_questions' not in request.session:
        request.session['nursery_urdu_questions'] = _default_nursery_urdu_questions()
        request.session.modified = True
    all_questions = request.session['nursery_urdu_questions']

    if request.method == "POST":
        form = NurseryUrduPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            start_letter = form.cleaned_data['start_letter']
            end_letter = form.cleaned_data['end_letter']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']
            selected_range = _nursery_urdu_letter_range(start_letter, end_letter)

            if heading == 'nursery_urdu_write_alphabet':
                rows_data = []
                for i in range(0, len(selected_range), 5):
                    rows_data.append(selected_range[i:i+5])

                question_data = {
                    'heading': heading,
                    'question_no': question_no,
                    'marks': marks,
                    'start_letter': selected_range[0],
                    'end_letter': selected_range[-1],
                    'rows_data': rows_data,
                }
            elif heading == 'nursery_urdu_matching':
                matching_letters = selected_range[:]
                if len(matching_letters) > 5:
                    matching_letters = random.sample(matching_letters, 5)
                left_letters = matching_letters[:]
                right_letters = matching_letters[:]
                random.shuffle(left_letters)
                random.shuffle(right_letters)

                question_data = {
                    'heading': heading,
                    'question_no': question_no,
                    'marks': marks,
                    'left_letters': left_letters,
                    'right_letters': right_letters,
                }
            elif heading == 'nursery_urdu_after_letters':
                sample_count = min(4, len(selected_range))
                sampled = random.sample(selected_range, sample_count)
                ordered_sampled = [l for l in selected_range if l in sampled]
                after_items = [{'letter': l} for l in ordered_sampled]
                question_data = {
                    'heading': heading,
                    'question_no': question_no,
                    'marks': marks,
                    'items': after_items,
                }
            elif heading == 'nursery_urdu_picture_matching':
                available_letters = [l for l in selected_range if l in URDU_VOCAB_MAP]
                if not available_letters:
                    available_letters = ['ا', 'ب', 'پ', 'ت', 'س']
                
                sample_count = min(5, len(available_letters))
                sampled = random.sample(available_letters, sample_count)
                
                shuffled_pic_letters = sampled[:]
                random.shuffle(shuffled_pic_letters)
                
                pic_match_images = []
                for letter in shuffled_pic_letters:
                    if letter == 'ا':
                        pic_match_images.append("urdu_img/urdu/alif.png")
                    else:
                        vocab_file = URDU_VOCAB_MAP.get(letter)
                        pic_match_images.append(f"urdu_img/{vocab_file}")
                
                shuffled_text_letters = sampled[:]
                random.shuffle(shuffled_text_letters)
                
                question_data = {
                    'heading': heading,
                    'question_no': question_no,
                    'marks': marks,
                    'left_images': pic_match_images,
                    'right_letters': shuffled_text_letters,
                }
            elif heading == 'nursery_urdu_put_dots':
                dots_rows = [
                    ['ٮ', 'ٮ', 'ٮ', 'ٮ', 'ٮ'],
                    ['ح', 'ح', 'ح'],
                    ['ر', 'ر', 'د', 'د'],
                    ['ص', 'س']
                ]
                question_data = {
                    'heading': heading,
                    'question_no': question_no,
                    'marks': marks,
                    'rows': dots_rows,
                }

            all_questions.append(question_data)
            request.session['nursery_urdu_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/nursery_urdu_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })


def reset_nursery_urdu_paper(request):
    request.session['nursery_urdu_questions'] = []
    request.session.modified = True
    return redirect('nursery_urdu')


FIND_CIRCLE_IMAGE_BY_NUMBER = {
    1: 'elephant.png.png',
    2: 'cat.png.png',
    3: 'butterfly.png.png',
    4: 'lion.png.png',
    5: 'fish.png.png',
    6: 'rabbit.png.png',
    7: 'Giraffe.png.png',
    8: 'monkey.png.png',
    9: 'sparrow.png.png',
    10: 'star.png.png',
    11: 'Dinosaur.png.png',
    12: 'Rocket.png.png',
    13: 'Robot.png.png',
    14: 'Castle.png.png',
    15: 'Hot Air Balloon.png.png',
}


def _find_circle_image_name(target_number):
    return FIND_CIRCLE_IMAGE_BY_NUMBER.get(int(target_number or 0))


def _default_nursery_math_questions():
    # Randomly select 4 images for circle correct question
    available_images = ['A.png', 'B.png', 'C.png', 'D.png', 'E.png', 'F.png', 'G.png', 'H.png', 'I.png', 'J.png', 'K.png', 'L.png', 'M.png', 'N.png', 'O.png', 'P.png', 'Q.png', 'R.png', 'S.png', 'T.png', 'U.png', 'V.png', 'W.png', 'X.png', 'Y.png', 'Z.png']
    selected_circle_images = random.sample(available_images, 4)
    
    # Randomly select 5 images for count match question
    selected_count_images = random.sample(available_images, 5)
    
    selected_find_circle_number = random.randint(1, 15)
    selected_find_circle_image = _find_circle_image_name(selected_find_circle_number)
    
    return [
        {
            'heading': 'nursery_math_write_counting',
            'question_no': 1,
            'marks': 10,
            'start_number': 1,
            'end_number': 50,
        },
        {
            'heading': 'nursery_math_between',
            'question_no': 2,
            'marks': 10,
            'start_number': 1,
            'end_number': 20,
            'between_items': [
                {'first': 1, 'last': 3},
                {'first': 4, 'last': 6},
                {'first': 7, 'last': 9},
                {'first': 10, 'last': 12},
            ]
        },
        {
            'heading': 'nursery_math_circle_correct',
            'question_no': 3,
            'marks': 10,
            'sub_items': [
                {'type': 'clocks', 'image': f'pics/{selected_circle_images[0]}', 'count': 4, 'range': list(range(4)), 'options': [4, 3, 7]},
                {'type': 'car', 'image': f'pics/{selected_circle_images[1]}', 'count': 1, 'range': list(range(1)), 'options': [6, 1]},
                {'type': 'cups', 'image': f'pics/{selected_circle_images[2]}', 'count': 9, 'range': list(range(9)), 'options': [5, 9, 8]},
                {'type': 'butterflies', 'image': f'pics/{selected_circle_images[3]}', 'count': 3, 'range': list(range(3)), 'options': [1, 3]},
            ]
        },
        {
            'heading': 'nursery_math_count_match',
            'question_no': 4,
            'marks': 10,
            'left_items': [
                {'type': 'star', 'image': f'pics/{selected_count_images[0]}', 'count': 1, 'range': list(range(1))},
                {'type': 'bird', 'image': f'pics/{selected_count_images[1]}', 'count': 5, 'range': list(range(5))},
                {'type': 'apple', 'image': f'pics/{selected_count_images[2]}', 'count': 2, 'range': list(range(2))},
                {'type': 'ice_cream', 'image': f'pics/{selected_count_images[3]}', 'count': 4, 'range': list(range(4))},
                {'type': 'balloon', 'image': f'pics/{selected_count_images[4]}', 'count': 3, 'range': list(range(3))},
            ],
            'right_numbers': [5, 4, 3, 2, 1]
        },
        {
            'heading': 'nursery_math_find_and_circle',
            'question_no': 5,
            'marks': 5,
            'target_number': selected_find_circle_number,
            'image': f'find_numbers/{selected_find_circle_image}',
        },
        {
            'heading': 'nursery_math_match_same',
            'question_no': 6,
            'marks': 5,
            'left_column': [8, 9, 7, 6, 3],
            'right_column': [7, 8, 9, 3, 6],
        },
        {
            'heading': 'nursery_math_table',
            'question_no': 7,
            'marks': 10,
            'table_number': 2,
            'table_range': [1, 2, 3, 4, 5, 6],
        }
    ]


def nursery_math_paper(request):
    form = NurseryMathPaperForm()

    subject = request.session.get('subject', 'Math')
    class_name = request.session.get('class_name', 'Nursery')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'nursery_math_questions' not in request.session:
        request.session['nursery_math_questions'] = _default_nursery_math_questions()
        request.session.modified = True
    all_questions = request.session['nursery_math_questions']

    if request.method == "POST":
        form = NurseryMathPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            start_num = form.cleaned_data['start_number']
            end_num = form.cleaned_data['end_number']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
                'start_number': start_num,
                'end_number': end_num,
            }

            if heading == 'nursery_math_write_counting':
                pass

            elif heading == 'nursery_math_between':
                items = []
                for i in range(start_num, end_num - 1, 3):
                    items.append({
                        'first': i,
                        'last': i + 2
                    })
                question_data['between_items'] = items

            elif heading == 'nursery_math_circle_correct':
                chosen_nums = [random.randint(max(1, start_num), min(10, end_num)) for _ in range(4)]
                types = ['clocks', 'car', 'cups', 'butterflies']
                # Randomly select 4 images from pics directory
                available_images = ['A.png', 'B.png', 'C.png', 'D.png', 'E.png', 'F.png', 'G.png', 'H.png', 'I.png', 'J.png', 'K.png', 'L.png', 'M.png', 'N.png', 'O.png', 'P.png', 'Q.png', 'R.png', 'S.png', 'T.png', 'U.png', 'V.png', 'W.png', 'X.png', 'Y.png', 'Z.png']
                selected_images = random.sample(available_images, 4)
                images = [f'pics/{img}' for img in selected_images]
                sub_items = []
                for i in range(4):
                    count = chosen_nums[i]
                    distractors = []
                    while len(distractors) < 2:
                        dist = random.randint(max(1, start_num), min(10, end_num))
                        if dist != count and dist not in distractors:
                            distractors.append(dist)
                    options = [count] + distractors
                    random.shuffle(options)
                    sub_items.append({
                        'type': types[i],
                        'image': images[i],
                        'count': count,
                        'range': list(range(count)),
                        'options': options
                    })
                question_data['sub_items'] = sub_items

            elif heading == 'nursery_math_count_match':
                counts = random.sample(range(max(1, start_num), min(10, end_num) + 1), min(5, end_num - start_num + 1))
                while len(counts) < 5:
                    counts.append(random.randint(max(1, start_num), min(10, end_num)))
                types = ['star', 'bird', 'apple', 'ice_cream', 'balloon']
                images = ['pics/S.png', 'pics/F.png', 'pics/A.png', 'pics/I.png', 'pics/B.png']
                left_items = []
                for i in range(5):
                    left_items.append({
                        'type': types[i],
                        'image': images[i],
                        'count': counts[i],
                        'range': list(range(counts[i]))
                    })
                right_numbers = counts[:]
                random.shuffle(right_numbers)
                question_data['left_items'] = left_items
                question_data['right_numbers'] = right_numbers

            elif heading == 'nursery_math_find_and_circle':
                target_number = form.cleaned_data.get('target_number') or 1
                selected_image = _find_circle_image_name(target_number)
                question_data['target_number'] = target_number
                question_data['image'] = f'find_numbers/{selected_image}' if selected_image else ''

            elif heading == 'nursery_math_match_same':
                range_nums = list(range(max(1, start_num), min(10, end_num) + 1))
                if len(range_nums) < 5:
                    range_nums = list(range(1, 10))
                
                chosen_nums = random.sample(range_nums, 5)
                
                left_nums = chosen_nums[:]
                random.shuffle(left_nums)
                
                right_nums = chosen_nums[:]
                random.shuffle(right_nums)
                
                question_data['left_column'] = left_nums
                question_data['right_column'] = right_nums

            elif heading == 'nursery_math_table':
                table_number = form.cleaned_data.get('table_number', 2)
                table_end = form.cleaned_data.get('table_end', 6)
                table_range = list(range(1, table_end + 1))
                question_data['table_number'] = table_number
                question_data['table_range'] = table_range

            all_questions.append(question_data)
            request.session['nursery_math_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/nursery_math_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })


def reset_nursery_math_paper(request):
    request.session['nursery_math_questions'] = []
    request.session.modified = True
    return redirect('nursery_math')


def nursery_drawing_paper(request):
    form = NurseryDrawingPaperForm()

    subject = request.session.get('subject', 'Drawing')
    class_name = request.session.get('class_name', 'Nursery')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'nursery_drawing_questions' not in request.session:
        request.session['nursery_drawing_questions'] = []
    all_questions = request.session['nursery_drawing_questions']

    if request.method == "POST":
        form = NurseryDrawingPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            # Get all available images from pics directory (A-Z)
            alphabet_list = list(string.ascii_uppercase)
            
            if heading == "color_it":
                # Randomly select 1 image for each color it question
                selected_letter = random.choice(alphabet_list)
                
                question_data = {
                    'heading': heading,
                    'question_no': question_no,
                    'marks': marks,
                    'image': f"pics/{selected_letter}.png"
                }

            elif heading == "nazra":
                # Nazra question - no image needed
                question_data = {
                    'heading': heading,
                    'question_no': question_no,
                    'marks': marks,
                }

            all_questions.append(question_data)
            request.session['nursery_drawing_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/nursery_drawing_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })


def reset_nursery_drawing_paper(request):
    if 'nursery_drawing_questions' in request.session:
        del request.session['nursery_drawing_questions']
    return redirect('nursery_drawing')


def generate_find_circle_image(request):
    """Serve the find-and-circle image directly without PIL processing for best quality"""
    target_number = int(request.GET.get('target', 11))
    mapped_image_name = _find_circle_image_name(target_number)

    if not mapped_image_name:
        mapped_image_name = 'elephant.png.png'

    image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'find_numbers', mapped_image_name)

    try:
        from django.http import FileResponse
        return FileResponse(open(image_path, 'rb'), content_type='image/png')
    except Exception:
        # Fallback: return a blank white image
        from io import BytesIO
        img = Image.new('RGBA', (1040, 780), color=(255, 255, 255, 255))
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        return HttpResponse(buffer, content_type='image/png')


def prep_english_paper(request):
    form = PrepEnglishPaperForm()

    subject = request.session.get('subject', 'English')
    class_name = request.session.get('class_name', 'Prep')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'prep_questions' not in request.session:
        request.session['prep_questions'] = []
    all_questions = request.session['prep_questions']

    if request.method == "POST":
        form = PrepEnglishPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
            }

            if heading == "prep_write_body_parts":
                question_data['body_parts'] = [
                    {'image': 'pics/eye.png', 'name': 'Eye'},
                    {'image': 'pics/lips.png', 'name': 'Lips'},
                    {'image': 'pics/ear.png', 'name': 'Ear'},
                    {'image': 'pics/nose.png', 'name': 'Nose'},
                    {'image': 'pics/hand.png', 'name': 'Hand'},
                ]

            elif heading == "prep_use_of_this":
                question_data['sentences'] = [
                    form.cleaned_data.get('sentence_1'),
                    form.cleaned_data.get('sentence_2'),
                    form.cleaned_data.get('sentence_3'),
                    form.cleaned_data.get('sentence_4'),
                    form.cleaned_data.get('sentence_5'),
                ]

            elif heading == "prep_vowels":
                question_data['vowels_hand'] = 'pics/hand.png'
                question_data['vowels_list'] = ['a', 'e', 'i', 'o', 'u']

            elif heading == "prep_write_fruit_name":
                question_data['fruits_left'] = [
                    {'image': 'pics/fruit_orange.png', 'name': 'Orange'},
                    {'image': 'pics/fruit_peach.png', 'name': 'Peach'},
                    {'image': 'pics/fruit_apple.png', 'name': 'Apple'},
                    {'image': 'pics/fruit_grapes.png', 'name': 'Grapes'},
                ]
                question_data['fruit_right'] = {'image': 'pics/fruit_mango.png', 'name': 'Mango'}

            elif heading == "prep_write_picture_name":
                import random
                # All Play class alphabet pictures (A-Z) - each letter maps to an animal/object
                all_pics = [
                    {'image': 'pics/A.png', 'name': 'Apple'},
                    {'image': 'pics/B.png', 'name': 'Ball'},
                    {'image': 'pics/C.png', 'name': 'Cat'},
                    {'image': 'pics/D.png', 'name': 'Dog'},
                    {'image': 'pics/E.png', 'name': 'Elephant'},
                    {'image': 'pics/F.png', 'name': 'Fish'},
                    {'image': 'pics/G.png', 'name': 'Goat'},
                    {'image': 'pics/H.png', 'name': 'Horse'},
                    {'image': 'pics/I.png', 'name': 'Igloo'},
                    {'image': 'pics/J.png', 'name': 'Jug'},
                    {'image': 'pics/K.png', 'name': 'Kite'},
                    {'image': 'pics/L.png', 'name': 'Lion'},
                    {'image': 'pics/M.png', 'name': 'Monkey'},
                    {'image': 'pics/N.png', 'name': 'Nest'},
                    {'image': 'pics/O.png', 'name': 'Orange'},
                    {'image': 'pics/P.png', 'name': 'Parrot'},
                    {'image': 'pics/Q.png', 'name': 'Queen'},
                    {'image': 'pics/R.png', 'name': 'Rabbit'},
                    {'image': 'pics/S.png', 'name': 'Snake'},
                    {'image': 'pics/T.png', 'name': 'Tree'},
                    {'image': 'pics/U.png', 'name': 'Umbrella'},
                    {'image': 'pics/V.png', 'name': 'Van'},
                    {'image': 'pics/W.png', 'name': 'Watch'},
                    {'image': 'pics/X.png', 'name': 'X-Ray'},
                    {'image': 'pics/Y.png', 'name': 'Yoyo'},
                    {'image': 'pics/Z.png', 'name': 'Zebra'},
                ]
                question_data['pic_items'] = random.sample(all_pics, 4)

            elif heading == "prep_write_missing_words":
                import random
                all_missing = [
                    {'word': 'P....rrot',  'image': 'pics/P.png'},
                    {'word': 'Sn....ke',   'image': 'pics/S.png'},
                    {'word': 'Umb....ella','image': 'pics/U.png'},
                    {'word': 'Y...yo',     'image': 'pics/Y.png'},
                    {'word': 'App...e',    'image': 'pics/A.png'},
                    {'word': 'B...ll',     'image': 'pics/B.png'},
                    {'word': 'C...t',      'image': 'pics/C.png'},
                    {'word': 'D...g',      'image': 'pics/D.png'},
                    {'word': 'El...ph...t','image': 'pics/E.png'},
                    {'word': 'F...sh',     'image': 'pics/F.png'},
                    {'word': 'G...at',     'image': 'pics/G.png'},
                    {'word': 'H...rse',    'image': 'pics/H.png'},
                    {'word': 'K...te',     'image': 'pics/K.png'},
                    {'word': 'L...on',     'image': 'pics/L.png'},
                    {'word': 'M...nk...y', 'image': 'pics/M.png'},
                    {'word': 'N...st',     'image': 'pics/N.png'},
                    {'word': 'R...bb...t', 'image': 'pics/R.png'},
                    {'word': 'Tr...e',     'image': 'pics/T.png'},
                    {'word': 'W...tch',    'image': 'pics/W.png'},
                    {'word': 'Z...bra',    'image': 'pics/Z.png'},
                ]
                question_data['missing_words'] = random.sample(all_missing, 5)

            elif heading == "prep_write_capital_small":
                start_l = form.cleaned_data.get('start_letter') or 'A'
                end_l = form.cleaned_data.get('end_letter') or 'Z'
                
                # Ensure correct ordering
                if start_l > end_l:
                    start_l, end_l = end_l, start_l
                
                # Get the alphabet range
                import string as str_module
                letters = list(str_module.ascii_uppercase)
                idx_start = letters.index(start_l)
                idx_end = letters.index(end_l)
                selected_range = letters[idx_start:idx_end + 1]
                
                # Calculate per_row dynamically
                range_size = len(selected_range)
                if range_size <= 10:
                    per_row = range_size
                else:
                    per_row = 4
                
                # Calculate horizontal column positions (as percentages) based on per_row
                col_positions = [((i + 0.5) / per_row) * 100 for i in range(per_row)]
                
                # Split into rows
                rows = []
                for idx in range(0, len(selected_range), per_row):
                    chunk = selected_range[idx:idx + per_row]
                    row_dots = [col_positions[i] for i in range(len(chunk))]
                    rows.append({
                        'letters': chunk,
                        'dots': row_dots
                    })
                
                question_data['letter_rows'] = rows
                question_data['range_label'] = f"{start_l}a to {end_l}{end_l.lower()}"

            all_questions.append(question_data)
            request.session['prep_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/prep_english_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })


def reset_prep_english_paper(request):
    if 'prep_questions' in request.session:
        del request.session['prep_questions']
    return redirect('prep_english')

def prep_math_paper(request):
    form = PrepMathPaperForm()

    subject = request.session.get('subject', 'Math')
    class_name = request.session.get('class_name', 'Prep')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'prep_math_questions' not in request.session:
        request.session['prep_math_questions'] = []
    all_questions = request.session['prep_math_questions']

    if request.method == "POST":
        form = PrepMathPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
            }

            if heading == "prep_math_counting":
                start = form.cleaned_data.get('start_num', 1)
                end = form.cleaned_data.get('end_num', 50)
                question_data['start_num'] = start
                question_data['end_num'] = end
                
                try:
                    num_boxes = int(end) - int(start) + 1
                    if num_boxes < 1:
                        num_boxes = 50
                except (ValueError, TypeError):
                    num_boxes = 50
                
                question_data['boxes'] = list(range(num_boxes))

            elif heading == "prep_math_english_urdu":
                question_data['rows'] = [1, 2, 3, 4, 5]

            elif heading == "prep_math_shapes":
                question_data['shapes'] = ['square', 'circle', 'star']

            elif heading == "prep_math_before":
                question_data['before_items'] = [
                    {'left': form.cleaned_data.get('before_n1'), 'right': form.cleaned_data.get('before_n6')},
                    {'left': form.cleaned_data.get('before_n2'), 'right': form.cleaned_data.get('before_n7')},
                    {'left': form.cleaned_data.get('before_n3'), 'right': form.cleaned_data.get('before_n8')},
                    {'left': form.cleaned_data.get('before_n4'), 'right': form.cleaned_data.get('before_n9')},
                    {'left': form.cleaned_data.get('before_n5'), 'right': form.cleaned_data.get('before_n10')},
                ]

            elif heading == "prep_math_count_write":
                import random
                # Same images as play class
                all_pics = [
                    'pics/A.png', 'pics/B.png', 'pics/C.png', 'pics/D.png', 'pics/E.png',
                    'pics/F.png', 'pics/G.png', 'pics/H.png', 'pics/K.png', 'pics/L.png',
                    'pics/M.png', 'pics/N.png', 'pics/P.png', 'pics/R.png', 'pics/T.png',
                    'pics/W.png', 'pics/Z.png'
                ]
                selected_pics = random.sample(all_pics, 5)
                # Create groups of 5, 4, 3, 2, 1
                counts = [5, 4, 3, 2, 1]
                
                right_numbers = [5, 4, 3, 2, 1]
                random.shuffle(right_numbers)
                
                groups = []
                for idx, count in enumerate(counts):
                    groups.append({
                        'image': selected_pics[idx],
                        'count': count,
                        'range': list(range(count)),
                        'number': right_numbers[idx]
                    })
                question_data['groups'] = groups

            elif heading == "prep_math_table":
                table_num = form.cleaned_data.get('table_number', 2)
                table_end = form.cleaned_data.get('table_end', 10)
                question_data['table_number'] = table_num
                question_data['table_end'] = table_end
                
                # Generate table rows
                table_rows = []
                for i in range(1, table_end + 1):
                    table_rows.append({
                        'multiplicand': table_num,
                        'multiplier': i,
                        'product': table_num * i
                    })
                question_data['table_rows'] = table_rows

            elif heading == "prep_math_circle_correct":
                import random
                # Use pics/ folder images — Play class English paper wali images
                all_pics = [
                    {'image': 'pics/B.png',  'name': 'butterfly'},
                    {'image': 'pics/C.png',  'name': 'cat'},
                    {'image': 'pics/F.png',  'name': 'fish'},
                    {'image': 'pics/D.png',  'name': 'dog'},
                    {'image': 'pics/H.png',  'name': 'horse'},
                    {'image': 'pics/L.png',  'name': 'lion'},
                    {'image': 'pics/M.png',  'name': 'monkey'},
                    {'image': 'pics/R.png',  'name': 'rabbit'},
                    {'image': 'pics/Z.png',  'name': 'zebra'},
                    {'image': 'pics/G.png',  'name': 'goat'},
                    {'image': 'pics/E.png',  'name': 'elephant'},
                    {'image': 'pics/P.png',  'name': 'parrot'},
                ]
                
                # Randomly pick 4 different images
                chosen = random.sample(all_pics, 4)
                
                # Assign random counts and generate distractor options
                counts = random.sample(range(1, 10), 4)
                
                items = []
                for i, pic in enumerate(chosen):
                    target_count = counts[i]
                    distractors = []
                    while len(distractors) < 2:
                        d = random.randint(1, 9)
                        if d != target_count and d not in distractors:
                            distractors.append(d)
                    options = [target_count] + distractors
                    random.shuffle(options)
                    items.append({
                        'image': pic['image'],
                        'count_range': list(range(target_count)),
                        'options': options
                    })
                
                question_data['sub_items'] = items

            all_questions.append(question_data)
            request.session['prep_math_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/prep_math_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })

def reset_prep_math_paper(request):
    if 'prep_math_questions' in request.session:
        del request.session['prep_math_questions']
    return redirect('prep_math')


# ────────────────────────────────────────────
# Prep Urdu Paper
# ────────────────────────────────────────────

# Urdu vocabulary images for Prep picture name question
PREP_URDU_PICTURE_ITEMS = [
    # pics/ فولڈر - Play class English والی اصل تصاویر
    # تصویر کا نام بالکل درست اردو میں (images دیکھ کر verify کیے گئے)
    {'image': 'pics/C.png',  'name_correct': 'بلی',       'name_wrong': 'کتا'},
    {'image': 'pics/D.png',  'name_correct': 'کتا',       'name_wrong': 'بکری'},
    {'image': 'pics/E.png',  'name_correct': 'ہاتھی',     'name_wrong': 'گینڈا'},
    {'image': 'pics/F.png',  'name_correct': 'مچھلی',     'name_wrong': 'پرندہ'},
    {'image': 'pics/G.png',  'name_correct': 'بکری',      'name_wrong': 'بھیڑ'},
    {'image': 'pics/H.png',  'name_correct': 'مرغی',      'name_wrong': 'مور'},
    {'image': 'pics/L.png',  'name_correct': 'شیر',       'name_wrong': 'چیتا'},
    {'image': 'pics/M.png',  'name_correct': 'بندر',      'name_wrong': 'ریچھ'},
    {'image': 'pics/R.png',  'name_correct': 'خرگوش',     'name_wrong': 'گلہری'},
    {'image': 'pics/A.png',  'name_correct': 'سیب',       'name_wrong': 'انار'},
    {'image': 'pics/B.png',  'name_correct': 'گیند',      'name_wrong': 'پتنگ'},
    {'image': 'pics/K.png',  'name_correct': 'پتنگ',      'name_wrong': 'گیند'},
    {'image': 'pics/N.png',  'name_correct': 'ناک',       'name_wrong': 'کان'},
    {'image': 'pics/P.png',  'name_correct': 'طوطا',      'name_wrong': 'کبوتر'},
    {'image': 'pics/S.png',  'name_correct': 'صابن',      'name_wrong': 'تیل'},
    {'image': 'pics/T.png',  'name_correct': 'کچھوا',     'name_wrong': 'مینڈک'},
    {'image': 'pics/U.png',  'name_correct': 'چھتری',     'name_wrong': 'ٹوپی'},
    {'image': 'pics/W.png',  'name_correct': 'گھڑی',      'name_wrong': 'گھنٹہ'},
    {'image': 'pics/O.png',  'name_correct': 'مالٹا',     'name_wrong': 'لیمو'},
]

def prep_urdu_paper(request):
    form = PrepUrduPaperForm()

    subject = request.session.get('subject', 'Urdu')
    class_name = request.session.get('class_name', 'Prep')
    year = request.session.get('year', 'Unknown')
    exam = request.session.get('exam', 'Unknown')

    if 'prep_urdu_questions' not in request.session:
        request.session['prep_urdu_questions'] = []
    all_questions = request.session['prep_urdu_questions']

    if request.method == "POST":
        form = PrepUrduPaperForm(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            question_no = form.cleaned_data['question_no']
            marks = form.cleaned_data['marks']

            question_data = {
                'heading': heading,
                'question_no': question_no,
                'marks': marks,
            }

            if heading == "prep_urdu_write_alphabet":
                start = form.cleaned_data.get('start_letter', 'ا')
                end = form.cleaned_data.get('end_letter', 'ش')

                try:
                    start_idx = NURSERY_URDU_ALPHABET.index(start)
                    end_idx = NURSERY_URDU_ALPHABET.index(end)
                    selected_range = NURSERY_URDU_ALPHABET[start_idx:end_idx + 1]
                except ValueError:
                    selected_range = NURSERY_URDU_ALPHABET[:10]

                question_data['start_letter'] = start
                question_data['end_letter'] = end

                # Build rows_data: each row has 5 letter slots with 4 lines
                per_row = 5
                rows = []
                for idx in range(0, len(selected_range), per_row):
                    chunk = selected_range[idx:idx + per_row]
                    rows.append({
                        'letters': chunk,
                        'count': len(chunk),
                        'dot_range': list(range(len(chunk))),
                    })
                question_data['rows_data'] = rows

            elif heading == "prep_urdu_same_sound":
                start = form.cleaned_data.get('start_letter', 'ا')
                end = form.cleaned_data.get('end_letter', 'ش')

                try:
                    start_idx = NURSERY_URDU_ALPHABET.index(start)
                    end_idx = NURSERY_URDU_ALPHABET.index(end)
                    if start_idx > end_idx:
                        start_idx, end_idx = end_idx, start_idx
                        start, end = end, start
                    selected_range = NURSERY_URDU_ALPHABET[start_idx:end_idx + 1]
                except ValueError:
                    selected_range = NURSERY_URDU_ALPHABET[:10]

                question_data['start_letter'] = start
                question_data['end_letter'] = end

                # Build rows_data: each row has 5 letter slots with 4 lines
                per_row = 5
                rows = []
                for idx in range(0, len(selected_range), per_row):
                    chunk = selected_range[idx:idx + per_row]
                    rows.append({
                        'letters': chunk,
                        'count': len(chunk),
                        'dot_range': list(range(len(chunk))),
                    })
                question_data['rows_data'] = rows

            elif heading == "prep_urdu_picture_name":
                import random
                # Randomly pick 5 picture items
                chosen = random.sample(PREP_URDU_PICTURE_ITEMS, min(5, len(PREP_URDU_PICTURE_ITEMS)))
                pic_items = []
                for item in chosen:
                    # Randomize option order
                    options = [item['name_correct'], item['name_wrong']]
                    random.shuffle(options)
                    pic_items.append({
                        'image': item['image'],
                        'option1': options[0],
                        'option2': options[1],
                    })
                question_data['pic_items'] = pic_items

            elif heading == "prep_urdu_after_letters":
                import random
                start = form.cleaned_data.get('start_letter', 'ا')
                end = form.cleaned_data.get('end_letter', 'ش')
                try:
                    start_idx = NURSERY_URDU_ALPHABET.index(start)
                    end_idx = NURSERY_URDU_ALPHABET.index(end)
                    if start_idx > end_idx:
                        start_idx, end_idx = end_idx, start_idx
                    selected_range = NURSERY_URDU_ALPHABET[start_idx:end_idx + 1]
                except ValueError:
                    selected_range = NURSERY_URDU_ALPHABET[:10]
                
                # Exclude last letter if it's there
                if len(selected_range) > 5 and selected_range[-1] == 'ے':
                    selected_range = selected_range[:-1]
                letters = random.sample(selected_range, min(5, len(selected_range)))
                question_data['letters'] = letters

            elif heading == "prep_urdu_name_class":
                pass

            elif heading == "prep_urdu_dictation":
                pass

            elif heading == "prep_urdu_half_shapes":
                import random
                half_shape_letters = ['ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ', 'س', 'ش', 'ص', 'ض', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'ہ', 'ی']
                letters = random.sample(half_shape_letters, 5)
                question_data['letters'] = letters

            elif heading == "prep_urdu_break_words":
                import random
                words = ['طوطا', 'اونٹ', 'بات', 'داتا', 'جسم', 'تارا', 'چابی', 'روٹی', 'مالی', 'پانی']
                selected_words = random.sample(words, 5)
                question_data['words'] = selected_words

            elif heading == "prep_urdu_matching":
                import random
                words = ['بابا', 'جوڑ', 'سوچو', 'کھانا', 'پانی', 'جانا', 'آنا', 'نانا', 'دادا', 'تارا']
                selected_words = random.sample(words, 4)
                left_words = selected_words[:]
                right_words = selected_words[:]
                random.shuffle(left_words)
                random.shuffle(right_words)
                question_data['left_words'] = left_words
                question_data['right_words'] = right_words

            elif heading == "prep_urdu_color_names":
                pass

            elif heading == "prep_urdu_oral":
                pass

            all_questions.append(question_data)
            request.session['prep_urdu_questions'] = all_questions
            request.session.modified = True

    return render(request, "My_Paper/prep_urdu_paper.html", {
        "form": form,
        "all_questions": all_questions,
        "subject": subject,
        "class_name": class_name,
        'exam': exam,
        'year': year,
    })


def reset_prep_urdu_paper(request):
    if 'prep_urdu_questions' in request.session:
        del request.session['prep_urdu_questions']
    return redirect('prep_urdu')
