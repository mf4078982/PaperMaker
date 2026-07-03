from doctest import Example
import string
import random
from django.shortcuts import render, redirect,HttpResponse
from .forms import PaperForm, UrduPaperForm, MathPaperForm


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


