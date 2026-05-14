from urllib.parse import quote
from fastapi import Request
from nicegui import ui, app


def register_quiz_page():


    @ui.page('/quiz')
    def quiz_page(request: Request):
        name = request.query_params.get('name', '학생')
        student_id = request.query_params.get('student_id', '000000')

        paper_sets = [
            {
                'key': 'sle_cart',
                'question': '난치성 루푸스에서 CD19 CAR-T 치료는 자가면역 반응을 재설정할 수 있을까?',
                'author': 'Mackensen et al.',
                'year': '2022',
                'tags': ['SLE', 'CD19', 'CAR-T', '자가항체'],
                'count': '4문항',
                'ready': True,
                'status': '안 푼 문제',
                'accent': 'bg-sky-300',
            },
            {
                'key': 'treg_tolerance',
                'question': '면역관용은 왜 무너지고, Treg은 이를 다시 회복시킬 수 있을까?',
                'author': '준비 중',
                'year': '-',
                'tags': ['Treg', '면역관용', '자가면역'],
                'count': '준비 중',
                'ready': False,
                'status': '준비 중',
                'accent': 'bg-slate-300',
            },
            {
                'key': 'cartreg_target',
                'question': 'CAR-Treg은 무차별적 면역억제 대신 원하는 조직만 조절할 수 있을까?',
                'author': '준비 중',
                'year': '-',
                'tags': ['CAR-Treg', '항원특이성', '정밀치료'],
                'count': '준비 중',
                'ready': False,
                'status': '준비 중',
                'accent': 'bg-slate-300',
            },
            {
                'key': 'immune_checkpoint',
                'question': '면역항암제 반응 차이는 종양미세환경으로 설명될 수 있을까?',
                'author': '준비 중',
                'year': '-',
                'tags': ['면역항암제', 'T세포', '종양미세환경'],
                'count': '준비 중',
                'ready': False,
                'status': '준비 중',
                'accent': 'bg-slate-300',
            },
        ]

        quiz_results = app.storage.user.get('quiz_results', {})

        with ui.column().classes('w-full min-h-screen bg-slate-50'):

            # 상단 헤더
            with ui.element('div').classes(
                'w-full min-h-[64px] flex flex-col sm:flex-row '
                'items-start sm:items-center justify-between gap-3 '
                'px-4 sm:px-8 py-4 sm:py-0 bg-white border-b border-slate-200'
            ):
                with ui.column().classes('gap-0'):
                    ui.label('AMPhST Quiz Training').classes(
                        'text-lg sm:text-xl font-bold text-slate-900'
                    )
                    ui.label('논문별 문제 풀이 훈련').classes(
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
                            f'/class?name={quote(name)}&student_id={quote(student_id)}'
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

            # 본문
            with ui.column().classes(
                'w-full px-4 sm:px-8 lg:px-12 py-6 sm:py-8 gap-5'
            ):

                # 소개 영역: 작게
                with ui.card().classes(
                    'w-full p-5 sm:p-7 rounded-3xl bg-white border border-slate-100 shadow-sm'
                ):
                    ui.label('PAPER-BASED QUIZ').classes(
                        'text-xs font-semibold tracking-widest text-rose-500'
                    )

                    ui.label('논문별 문제 풀이 훈련').classes(
                        'text-2xl sm:text-3xl font-extrabold text-slate-900 mt-2'
                    )

                    ui.label(
                        '논문에서 출발한 문제 세트를 선택해 핵심 개념과 연구 내용을 점검합니다.'
                    ).classes(
                        'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                    )

                # 검색 / 풀이 상태 필터 영역
                with ui.element('div').classes(
                    'w-full flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3'
                ):

                    # 왼쪽: 상태 필터
                    with ui.row().classes('w-full sm:w-fit gap-2 flex-wrap'):
                        ui.button('전체').props('flat dense').classes(
                            'px-4 py-2 rounded-full bg-rose-50 text-rose-600 text-sm font-semibold'
                        )

                        ui.button('푼 문제').props('flat dense').classes(
                            'px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-500 text-sm font-semibold'
                        )

                        ui.button('안 푼 문제').props('flat dense').classes(
                            'px-4 py-2 rounded-full bg-white border border-slate-200 text-slate-500 text-sm font-semibold'
                        )

                    # 오른쪽: 검색창
                    ui.input(
                        placeholder='논문, 저자, 태그 검색'
                    ).props(
                        'outlined dense clearable'
                    ).classes(
                        'w-full sm:w-[300px] bg-white'
                    )

                # 콤팩트 문제 세트 목록
                with ui.column().classes('w-full gap-3 mt-2'):

                    for paper in paper_sets:
                        disabled_style = 'opacity-70' if not paper['ready'] else ''

                        result = quiz_results.get(paper['key'])
                        is_completed =  result is not None and result.get('completed') is True
                        card_bg = 'bg-emerald-50 border-emerald-100' if is_completed else 'bg-white border-slate-100'
                        accent_bg = 'bg-emerald-400' if is_completed else paper['accent']

                        with ui.card().classes(
                            
                            f'w-full rounded-2xl overflow-hidden bg-white border border-slate-100 {card_bg}'
                            f'shadow-sm transition-all duration-300 hover:shadow-md {disabled_style}'
                        ):
                            with ui.element('div').classes(
                                'w-full flex flex-col sm:flex-row'
                            ):

                                # 왼쪽 색상 바
                                ui.element('div').classes(
                                    f'w-full h-[5px] sm:w-[6px] sm:h-auto {accent_bg}'
                                )

                                # 본문
                                with ui.column().classes(
                                    'flex-1 min-w-0 p-5 gap-3'
                                ):

                                    # 상단 상태 / 문항 수
                                    with ui.row().classes(
                                        'w-full items-center justify-between gap-3'
                                    ):
                                        if is_completed:
                                            ui.label('푼 문제').classes(
                                                'text-xs font-semibold text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full'
                                            )
                                        elif paper['status'] == '안 푼 문제':
                                            ui.label('안 푼 문제').classes(
                                                'text-xs font-semibold text-sky-700 bg-sky-50 px-3 py-1 rounded-full'
                                            )
                                        else:
                                            ui.label('준비 중').classes(
                                                'text-xs font-semibold text-slate-500 bg-slate-100 px-3 py-1 rounded-full'
                                            )

                                        ui.label(paper['count']).classes(
                                            'text-xs font-medium text-slate-400'
                                        )

                                    # 질문
                                    ui.label(paper['question']).classes(
                                        'text-base sm:text-lg font-bold text-slate-900 leading-snug break-keep'
                                    )

                                    if is_completed:
                                        ui.label(
                                            f"이전 결과: {result['total_score']} / {result['max_total_score']}점 · {result['elapsed_text']}"
                                        ).classes(
                                            'text-sm font-semibold text-emerald-700 mt-1'
                                        )

                                    # 논문 정보 + 버튼
                                    with ui.element('div').classes(
                                        'w-full flex flex-col sm:flex-row sm:items-end sm:justify-between gap-3'
                                    ):

                                        with ui.column().classes('gap-2 min-w-0'):
                                            ui.label(
                                                f"{paper['author']}, {paper['year']}"
                                            ).classes(
                                                'text-sm font-medium text-slate-500'
                                            )

                                            with ui.row().classes('w-full flex-wrap gap-2'):
                                                for tag in paper['tags']:
                                                    ui.label(f'#{tag}').classes(
                                                        'text-xs text-slate-500 bg-slate-100 px-2 py-1 rounded-full whitespace-nowrap'
                                                    )

                                        if paper['ready']:
                                            button_label = '다시 풀기' if is_completed else '문제 풀기'
                                            button_label = '다시 풀기' if is_completed else '문제 풀기'
                                            button_icon = 'refresh' if is_completed else 'arrow_forward'

                                            ui.button(
                                                button_label,
                                                icon=button_icon,
                                                on_click=lambda p=paper: ui.navigate.to(
                                                    f"/quiz/paper?paper={p['key']}&name={quote(name)}&student_id={quote(student_id)}"
                                                )
                                            ).props('flat dense').classes(
                                                'w-fit text-rose-600 text-sm font-semibold px-0'
)
                                        else:
                                            ui.button(
                                                '준비 중'
                                            ).props('flat dense disable').classes(
                                                'w-fit text-slate-400 text-sm font-semibold px-0'
                                            )
