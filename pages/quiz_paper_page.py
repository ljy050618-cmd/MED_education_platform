import time

from urllib.parse import quote
from fastapi import Request
from nicegui import ui, run, app

from utils.ai_feedback import evaluate_short_answer

def register_quiz_paper_page():

    @ui.page('/quiz/paper')
    def quiz_paper_page(request: Request):
        name = request.query_params.get('name', '학생')
        student_id = request.query_params.get('student_id', '000000')
        paper = request.query_params.get('paper', 'sle_cart')

        quiz_sets = {
            'sle_cart': {
                'title': 'CD19 CAR-T와 난치성 루푸스',
                'author': 'Mackensen et al.',
                'year': '2022',
                'questions': [
                    {
                        'type': 'choice',
                        'num': '01',
                        'q': 'CD19 CAR-T 치료가 루푸스에서 주목받는 핵심 이유는 무엇인가요?',
                        'options': [
                            '모든 면역세포를 무차별적으로 제거하기 위해서',
                            'B세포 계열을 표적으로 하여 자가항체 반응을 조절할 가능성이 있기 때문에',
                            '항생제 효과를 높이기 위해서',
                            '백신 접종 횟수를 줄이기 위해서',
                        ],
                        'answer': 'B세포 계열을 표적으로 하여 자가항체 반응을 조절할 가능성이 있기 때문에',
                        'feedback': '맞습니다. CD19 CAR-T는 B세포 계열을 표적으로 하여 자가항체 생성과 관련된 면역반응을 조절할 가능성이 있습니다.',
                    },
                    {
                        'type': 'short',
                        'num': '02',
                        'q': '난치성 루푸스에서 CD19 CAR-T 치료 효과를 평가하려면 어떤 결과지표를 함께 보면 좋을까요?',
                        'key_points': ['질병활성도', '자가항체', 'B세포', '보체', '단백뇨', '안전성'],
                        'sample_answer': '질병활성도, 자가항체, B세포 수, 보체 C3/C4, 단백뇨, 이상반응 같은 안전성 지표를 함께 평가하면 좋습니다.',
                        'feedback': '좋은 답변입니다. 치료 효과를 보려면 임상적 변화뿐 아니라 면역학적 지표와 장기 침범 지표를 함께 확인해야 합니다.',
                    },
                    {
                        'type': 'choice',
                        'num': '03',
                        'q': 'CD19 CAR-T 치료 후 B세포가 감소했다면, 연구자는 어떤 점을 함께 확인해야 할까요?',
                        'options': [
                            'B세포 감소와 질병활성도 개선이 함께 나타나는지 확인한다',
                            '환자의 키가 증가했는지 확인한다',
                            '혈액형이 바뀌었는지 확인한다',
                            '백신 접종 횟수만 비교한다',
                        ],
                        'answer': 'B세포 감소와 질병활성도 개선이 함께 나타나는지 확인한다',
                        'feedback': '맞습니다. 표적 세포 변화가 실제 임상 호전과 연결되는지 확인해야 치료 효과를 더 타당하게 해석할 수 있습니다.',
                    },
                    {
                        'type': 'short',
                        'num': '04',
                        'q': '새로운 세포치료 연구에서 연구윤리와 안전성 측면에서 반드시 고려해야 할 점은 무엇인가요?',
                        'key_points': ['IRB', '동의', '이상반응', '감염', '장기 추적', '개인정보'],
                        'sample_answer': 'IRB 승인, 충분한 설명과 동의, 이상반응 모니터링, 감염 위험 관리, 장기 추적 관찰, 개인정보 보호를 고려해야 합니다.',
                        'feedback': '좋습니다. 세포치료 연구는 치료 효과뿐 아니라 안전성, 설명 동의, 장기 추적 관리가 매우 중요합니다.',
                    },
                ],
            }
        }

        selected = quiz_sets.get(paper, quiz_sets['sle_cart'])
        questions = selected['questions']

        state = {
            'started': False,
            'index': 0,
            'score': 0,
            'answered': False,
            'selected_answers': [],
            'question_scores': [],
            'start_time': None,
            'end_time': None,
        }

        QUESTION_MAX_SCORE = 25
        SHORT_PASS_SCORE = 15

        with ui.column().classes('w-full min-h-screen bg-slate-50'):

            # 상단 헤더
            with ui.element('div').classes(
                'w-full min-h-[64px] flex flex-col sm:flex-row '
                'items-start sm:items-center justify-between gap-3 '
                'px-4 sm:px-8 py-4 sm:py-0 bg-white border-b border-slate-200'
            ):
                with ui.column().classes('gap-0'):
                    ui.label('Paper Quiz').classes(
                        'text-lg sm:text-xl font-bold text-slate-900'
                    )
                    ui.label(selected['title']).classes(
                        'text-xs text-slate-400'
                    )

                with ui.row().classes('items-center gap-2 sm:gap-3 flex-wrap'):
                    ui.label(f'{name} · {student_id}').classes(
                        'text-sm text-slate-500'
                    )

                    ui.button(
                        '이전',
                        icon='arrow_back',
                        on_click=lambda: ui.navigate.to(
                            f'/quiz?name={quote(name)}&student_id={quote(student_id)}'
                        )
                    ).props('flat dense').classes(
                        'text-slate-500 text-sm'
                    )

                    ui.button(
                        '로그아웃',
                        icon='logout',
                        on_click=lambda: ui.navigate.to('/')
                    ).props('flat dense').classes(
                        'text-slate-500 text-sm'
                    )

            # 본문 컨테이너
            with ui.column().classes(
                'w-full max-w-[900px] mx-auto px-4 sm:px-8 py-6 sm:py-10 gap-5'
            ):

                # 논문 정보 카드
                with ui.card().classes(
                    'w-full p-5 sm:p-6 rounded-3xl bg-white border border-slate-100 shadow-sm'
                ):
                    ui.label('BASED ON PAPER').classes(
                        'text-xs font-semibold tracking-widest text-sky-500'
                    )

                    ui.label(selected['title']).classes(
                        'text-2xl sm:text-3xl font-extrabold text-slate-900 mt-2'
                    )

                    ui.label(f"{selected['author']}, {selected['year']}").classes(
                        'text-sm text-slate-500 mt-2'
                    )

                question_area = ui.column().classes('w-full gap-5')

                def show_intro():
                    question_area.clear()

                    with question_area:
                        with ui.card().classes(
                            'w-full p-7 sm:p-10 rounded-3xl bg-white border border-slate-100 shadow-sm'
                        ):
                            ui.label('QUIZ GUIDE').classes(
                                'text-xs font-semibold tracking-widest text-sky-500'
                            )

                            ui.label('문제 풀이를 시작하기 전 확인해 주세요').classes(
                                'text-2xl sm:text-3xl font-extrabold text-slate-900 mt-3'
                            )

                            ui.label(
                                '이 문제 세트는 객관식과 주관식 문제로 구성되어 있습니다.'
                            ).classes(
                                'text-sm sm:text-base text-slate-500 mt-4 leading-relaxed'
                            )

                            with ui.column().classes('w-full gap-3 mt-7'):
                                guide_items = [
                                    '문제는 한 번에 하나씩 제시됩니다.',
                                    '객관식은 답을 선택한 뒤 정답 확인을 누르세요.',
                                    '주관식은 답변을 작성한 뒤 피드백 확인을 누르세요.',
                                    '마지막 문제를 풀면 전체 결과가 표시됩니다.',
                                ]

                                for item in guide_items:
                                    with ui.row().classes('items-start gap-3'):
                                        ui.icon('check_circle').classes('text-sky-500 mt-1')
                                        ui.label(item).classes(
                                            'text-sm sm:text-base text-slate-600'
                                        )

                            ui.separator().classes('my-7')

                            with ui.card().classes(
                                'w-full p-4 rounded-2xl bg-slate-50 shadow-none'
                            ):
                                ui.label('기반 논문').classes(
                                    'text-xs font-semibold text-slate-400'
                                )
                                ui.label(selected['title']).classes(
                                    'text-base font-bold text-slate-800 mt-1'
                                )
                                ui.label(f"{selected['author']}, {selected['year']}").classes(
                                    'text-sm text-slate-500 mt-1'
                                )

                            ui.button(
                                '문제 풀이 시작하기',
                                on_click=start_quiz
                            ).classes(
                                'w-full sm:w-fit mt-8 px-7 py-3 rounded-xl bg-sky-600 text-white'
                            )

                def start_quiz():
                    state['started'] = True
                    state['index'] = 0
                    state['score'] = 0
                    state['answered'] = False
                    state['selected_answers'] = []
                    state['question_scores'] = [None for _ in questions]
                    state['start_time'] = time.time()
                    state['end_time'] = None
                    render_question()

                def show_result():
                    question_area.clear()

                    with question_area:
                        with ui.card().classes(
                            'w-full p-7 sm:p-10 rounded-3xl bg-white border border-slate-100 shadow-sm text-center'
                        ):
                            ui.label('QUIZ COMPLETE').classes(
                                'text-xs font-semibold tracking-widest text-emerald-500'
                            )

                            ui.label('문제 풀이 완료').classes(
                                'text-3xl sm:text-4xl font-extrabold text-slate-900 mt-3'
                            )

                            state['end_time'] = time.time()

                            total_score = sum(
                                s for s in state['question_scores']
                                if isinstance(s, int)
                            )

                            max_total_score = len(questions) * QUESTION_MAX_SCORE
                            score_percent = int((total_score / max_total_score) * 100)

                            elapsed_seconds = int(state['end_time'] - state['start_time'])
                            elapsed_minutes = elapsed_seconds // 60
                            remaining_seconds = elapsed_seconds % 60
                            
                            elapsed_text = f"{elapsed_minutes}분 {remaining_seconds}초"

                            quiz_results = app.storage.user.get('quiz_results', {})

                            quiz_results[paper] = {
                                'completed': True,
                                'total_score': total_score,
                                'max_total_score': max_total_score,
                                'score_percent': score_percent,
                                'elapsed_text': elapsed_text,
                                'question_scores': state['question_scores'],
                            }

                            app.storage.user['quiz_results'] = quiz_results
                            
                            ui.label(
                                f"총점: {total_score} / {max_total_score}점"
                            ).classes(
                                'text-xl font-bold text-slate-800 mt-5'
                            )

                            ui.label(
                                f"정답률/달성률: {score_percent}%"
                            ).classes(
                                'text-base text-slate-600 mt-2'
                            )

                            ui.label(
                                f"소요시간: {elapsed_text}"
                            ).classes(
                                'text-base text-slate-600 mt-2'
                            )

                            with ui.column().classes('w-full gap-2 mt-6'):
                                for i, score in enumerate(state['question_scores'], start=1):
                                    ui.label(
                                        f"문항 {i}: {score} / {QUESTION_MAX_SCORE}점"
                                    ).classes(
                                        'text-sm text-slate-500'
                                    )

                            with ui.row().classes(
                                'w-full justify-center gap-3 mt-8 flex-wrap'
                            ):
                                ui.button(
                                    '다시 풀기',
                                    icon='refresh',
                                    on_click=restart_quiz
                                ).classes(
                                    'px-6 py-3 rounded-xl bg-sky-600 text-white'
                                )

                                ui.button(
                                    '문제 세트로 돌아가기',
                                    icon='arrow_back',
                                    on_click=lambda: ui.navigate.to(
                                        f'/quiz?name={quote(name)}&student_id={quote(student_id)}'
                                    )
                                ).props('outline').classes(
                                    'px-6 py-3 rounded-xl text-slate-600'
                                )

                def restart_quiz():
                    state['started'] = False
                    state['index'] = 0
                    state['score'] = 0
                    state['answered'] = False
                    state['selected_answers'] = []
                    state['question_scores'] = []
                    state['start_time'] = None
                    state['end_time'] = None
                    show_intro()

                def render_question():
                    question_area.clear()
                    state['answered'] = False

                    current_index = state['index']
                    question = questions[current_index]
                    progress_value = (current_index + 1) / len(questions)

                    with question_area:

                        # 진행상황 카드
                        with ui.card().classes(
                            'w-full p-5 rounded-3xl bg-white border border-slate-100 shadow-sm'
                        ):
                            with ui.row().classes(
                                'w-full items-center justify-between gap-3'
                            ):
                                ui.label(
                                    f"Question {current_index + 1} / {len(questions)}"
                                ).classes(
                                    'text-sm font-semibold text-sky-600'
                                )

                                ui.label(
                                    f"{int(progress_value * 100)}%"
                                ).classes(
                                    'text-sm font-semibold text-slate-400'
                                )

                            ui.linear_progress(value=progress_value, show_value=False).classes(
                                'w-full mt-3'
                            )

                        # 문제 카드
                        with ui.card().classes(
                            'w-full p-6 sm:p-8 rounded-3xl bg-white border border-slate-100 shadow-sm'
                        ):
                            question_type = question.get('type', 'choice')

                            ui.label(f"QUESTION {question['num']}").classes(
                                'text-xs font-semibold tracking-widest text-sky-500'
                            )

                            if question_type == 'short':
                                ui.label('주관식').classes(
                                    'w-fit mt-3 text-xs font-semibold text-sky-700 bg-sky-50 px-3 py-1 rounded-full'
                                )
                            else:
                                ui.label('객관식').classes(
                                    'w-fit mt-3 text-xs font-semibold text-slate-600 bg-slate-100 px-3 py-1 rounded-full'
                                )

                            ui.label(question['q']).classes(
                                'text-xl sm:text-2xl font-bold text-slate-900 mt-4 leading-snug break-keep'
                            )

                            feedback_area = ui.column().classes('w-full mt-5')

                            if question_type == 'short':
                                answer_input = ui.textarea(
                                    placeholder='답변을 작성해 주세요.'
                                ).props(
                                    'outlined'
                                ).classes(
                                    'w-full mt-6'
                                )

                                with ui.card().classes(
                                    'w-full p-4 rounded-2xl bg-slate-50 shadow-none mt-4'
                                ):
                                    ui.label('포함하면 좋은 핵심 개념').classes(
                                        'text-xs font-semibold text-slate-400'
                                    )

                                    with ui.row().classes('w-full flex-wrap gap-2 mt-2'):
                                        for point in question.get('key_points', []):
                                            ui.label(point).classes(
                                                'text-xs text-slate-500 bg-white border border-slate-200 px-2 py-1 rounded-full'
                                            )

                                async def check_answer():

                                    if not answer_input.value or not answer_input.value.strip():
                                        ui.notify('답변을 먼저 입력해 주세요.')
                                        return

                                    feedback_area.clear()

                                    student_answer = answer_input.value.strip()

                                    if len(student_answer) > 1000:
                                        ui.notify('답변은 1000자 이내로 입력해 주세요.')
                                        return

                                    key_points = question.get('key_points', [])

                                    with feedback_area:
                                        with ui.card().classes(
                                            'w-full p-4 rounded-2xl bg-sky-50 shadow-none'
                                        ):
                                            ui.label('AI가 답변을 채점하고 있습니다.').classes(
                                                'text-sm font-bold text-sky-700'
                                            )
                                            ui.spinner(size='md').classes('mt-2')

                                    result = await run.io_bound(
                                        evaluate_short_answer,
                                        question['q'],
                                        student_answer,
                                        key_points,
                                        question.get('sample_answer', ''),
                                        QUESTION_MAX_SCORE,
                                        SHORT_PASS_SCORE,
                                    )

                                    score = result.get('score', 0)
                                    passed = result.get('passed', False)

                                    state['question_scores'][current_index] = score

                                    if passed:
                                        state['answered'] = True
                                        state['selected_answers'].append(student_answer)
                                    else:
                                        state['answered'] = False

                                    state['score'] = sum(
                                        s for s in state['question_scores']
                                        if isinstance(s, int)
                                    )

                                    feedback_area.clear()

                                    with feedback_area:
                                        with ui.card().classes(
                                            'w-full p-4 rounded-2xl bg-sky-50 shadow-none'
                                        ):
                                            if passed:
                                                ui.label('통과했습니다.').classes(
                                                    'text-sm font-bold text-emerald-700'
                                                )
                                            else:
                                                ui.label('아직 통과 기준에 도달하지 못했습니다.').classes(
                                                    'text-sm font-bold text-rose-700'
                                                )

                                            ui.label(
                                                f"점수: {score} / {QUESTION_MAX_SCORE}점"
                                            ).classes(
                                                'text-sm font-semibold text-slate-700 mt-2'
                                            )

                                            ui.label(
                                                f"통과 기준: {SHORT_PASS_SCORE}점 이상"
                                            ).classes(
                                                'text-xs text-slate-400 mt-1'
                                            )

                                            ui.separator().classes('my-3')

                                            ui.label('좋은 점').classes(
                                                'text-xs font-semibold text-slate-400'
                                            )
                                            ui.label(result.get('good', '')).classes(
                                                'text-sm text-slate-700 mt-1 leading-relaxed'
                                            )

                                            ui.label('보완할 점').classes(
                                                'text-xs font-semibold text-slate-400 mt-3'
                                            )
                                            ui.label(result.get('improve', '')).classes(
                                                'text-sm text-slate-700 mt-1 leading-relaxed'
                                            )

                                            ui.label('추천 답변').classes(
                                                'text-xs font-semibold text-slate-400 mt-3'
                                            )
                                            ui.label(result.get('recommended_answer', '')).classes(
                                                'text-sm text-slate-700 mt-1 leading-relaxed'
                                            )

                                            ui.label('한 줄 피드백').classes(
                                                'text-xs font-semibold text-slate-400 mt-3'
                                            )
                                            ui.label(result.get('one_line_feedback', '')).classes(
                                                'text-sm font-medium text-sky-700 mt-1 leading-relaxed'
                                            )

                                            if not passed:
                                                ui.separator().classes('my-3')
                                                ui.label(
                                                    '답변을 보완한 뒤 다시 AI 피드백 받기를 눌러야 다음 문제로 이동할 수 있습니다.'
                                                ).classes(
                                                    'text-xs text-rose-500'
                                                )
                               
                            else:
                                answer_radio = ui.radio(
                                    question['options'],
                                    value=None
                                ).classes(
                                    'mt-6 text-sm sm:text-base text-slate-700'
                                )

                                def check_answer():
                                    if answer_radio.value is None:
                                        ui.notify('답을 먼저 선택해 주세요.')
                                        return

                                    feedback_area.clear()

                                    is_correct = answer_radio.value == question['answer']

                                    if is_correct:
                                        state['question_scores'][current_index] = QUESTION_MAX_SCORE
                                        state['answered'] = True

                                        if answer_radio.value not in state['selected_answers']:
                                            state['selected_answers'].append(answer_radio.value)
                                    else:
                                        state['question_scores'][current_index] = 0
                                        state['answered'] = False

                                    state['score'] = sum(
                                        s for s in state['question_scores']
                                        if isinstance(s, int)
                                    )    

                                    with feedback_area:
                                        if is_correct:
                                            with ui.card().classes(
                                                'w-full p-4 rounded-2xl bg-emerald-50 shadow-none'
                                            ):
                                                ui.label('정답입니다.').classes(
                                                    'text-sm font-bold text-emerald-700'
                                                )
                                                ui.label(question['feedback']).classes(
                                                    'text-sm text-emerald-700 mt-1 leading-relaxed'
                                                )
                                        else:
                                            with ui.card().classes(
                                                'w-full p-4 rounded-2xl bg-slate-100 shadow-none'
                                            ):
                                                ui.label('다시 생각해볼까요?').classes(
                                                    'text-sm font-bold text-slate-700'
                                                )
                                                ui.label(
                                                    f"정답은 “{question['answer']}”입니다. {question['feedback']}"
                                                ).classes(
                                                    'text-sm text-slate-600 mt-1 leading-relaxed'
                                                )

                            def go_next():
                                if not state['answered']:
                                    ui.notify('통과 기준을 충족해야 다음 문제로 이동할 수 있습니다.')
                                    return

                                if state['index'] < len(questions) - 1:
                                    state['index'] += 1
                                    render_question()
                                else:
                                    show_result()

                            with ui.row().classes(
                                'w-full items-center justify-between gap-3 mt-7 flex-wrap'
                            ):
                                ui.button(
                                    'AI 채점 받기' if question_type == 'short' else '정답 확인',
                                    icon='smart_toy' if question_type == 'short' else 'check',
                                    on_click=check_answer
                                ).classes(
                                    'w-full sm:w-fit px-6 py-3 rounded-xl bg-sky-600 text-white'
                                )

                                next_label = '다음 문제' if current_index < len(questions) - 1 else '결과 보기'

                                ui.button(
                                    next_label,
                                    icon='arrow_forward',
                                    on_click=go_next
                                ).props('outline').classes(
                                    'w-full sm:w-fit px-6 py-3 rounded-xl text-slate-600'
                                )

                show_intro()
