import os
from urllib.parse import quote
from fastapi import Request
from nicegui import ui, app

# 이미지 폴더 등록
app.add_static_files('/education_images', 'education_images')


@ui.page('/')
def index():

    with ui.column().classes(
        'w-full min-h-screen items-center justify-center bg-white'
    ) as page:
        pass

    def show_logo_page():
        page.clear()

        with page:
            with ui.column().classes('w-full min-h-screen items-center justify-center px-4'):
                with ui.row().classes(
                    'items-center justify-center gap-3 sm:gap-4 flex-wrap text-center'
                ):
                    ui.image('/education_images/Ajou_logo.png').classes(
                        'w-[52px] h-[52px] sm:w-[68px] sm:h-[68px]'
                    )

                    with ui.row().classes('items-center gap-3 sm:gap-4 flex-wrap justify-center'):

                        # 왼쪽 글자
                        with ui.column().classes('gap-0 items-end'):
                            ui.label('아주대학교').classes(
                                'text-2xl sm:text-4xl font-bold text-gray-900 leading-tight'
                            )
                            ui.label('AJOU UNIVERSITY').classes(
                                'text-sm sm:text-xl font-semibold text-gray-700 leading-tight'
                            )

                        # 가운데 세로선
                        ui.element('div').classes(
                            'w-[2px] h-[52px] sm:h-[72px] bg-gray-400'
                        )

                        # 오른쪽 글자
                        with ui.column().classes('gap-0 items-start'):
                            ui.label('의과대학').classes(
                                'text-2xl sm:text-4xl font-bold text-gray-900 leading-tight'
                            )
                            ui.label('School of Medicine').classes(
                                'text-sm sm:text-xl font-semibold text-gray-700 leading-tight'
                            )

    def show_program_page():
        page.clear()

        with page:
            with ui.column().classes(
                'w-full min-h-screen items-center justify-center bg-white px-4 text-center'
            ):
                ui.label('아주대학교 의사과학자 양성사업단').classes(
                    'text-xl sm:text-3xl font-semibold text-gray-400'
                )

                ui.label('AMPhST 프로그램').classes(
                    'text-3xl sm:text-5xl font-bold text-gray-400 mt-3 sm:mt-4'
                )

                ui.label('의사과학자 연구설계 랩을 준비하고 있습니다').classes(
                    'text-base sm:text-lg text-gray-400 mt-8 sm:mt-10'
                )

                ui.spinner(size='lg').classes('mt-2')

    def show_main_page():
        page.clear()

        with page:
            with ui.column().classes(
                'relative w-full min-h-screen items-center justify-center bg-white px-4 text-center'
            ):

                # 좌측 상단 사업단 문구
                with ui.column().classes(
                    'absolute top-4 left-4 sm:top-8 sm:left-8 items-start gap-1 text-left'
                ):
                    ui.label('아주대학교 의사과학자 양성사업단').classes(
                        'text-xs sm:text-base font-medium text-gray-400'
                    )
                    ui.label('AMPhST 프로그램').classes(
                        'text-sm sm:text-xl font-semibold text-gray-400'
                    )

                ui.label('의사과학자 연구설계 랩').classes(
                    'text-3xl sm:text-4xl font-bold text-gray-900 text-center'
                )

                ui.label('학생이 연구자 입장에서 연구 설계를 체험하는 학습용 사이트입니다.').classes(
                    'text-base sm:text-lg text-gray-600 mt-3 px-4'
                )

                ui.button(
                    '연구 미션 시작하기',
                    on_click=show_login_page
                ).classes(
                    'text-base sm:text-lg px-5 sm:px-6 py-3 mt-6'
                )

    def show_login_page():
        page.clear()

        with page:
            with ui.column().classes(
                'relative w-full min-h-screen items-center justify-center bg-white px-4 py-20'
            ):

                # 좌측 상단 사업단 문구
                with ui.column().classes(
                    'absolute top-4 left-4 sm:top-8 sm:left-8 items-start gap-1 text-left'
                ):
                    ui.label('아주대학교 의사과학자 양성사업단').classes(
                        'text-xs sm:text-base font-medium text-gray-400'
                    )
                    ui.label('AMPhST 프로그램').classes(
                        'text-sm sm:text-xl font-semibold text-gray-400'
                    )

                # 로그인 카드
                with ui.card().classes(
                    'w-full max-w-[420px] p-6 sm:p-8 rounded-2xl shadow-lg items-center'
                ):
                    ui.label('연구자 로그인').classes(
                        'text-2xl sm:text-3xl font-bold text-gray-900 text-center'
                    )

                    ui.label('학습 체험을 위해 정보를 입력하세요.').classes(
                        'text-sm sm:text-base text-gray-500 text-center mt-2'
                    )

                    name_input = ui.input('이름').props('dense').classes(
                        'w-full mt-5 sm:mt-6'
                    )

                    ui.input('이메일').props('dense').classes(
                        'w-full'
                    )

                    student_id_input = ui.input('학번 또는 참가번호').props('dense').classes(
                        'w-full'
                    )

                    def go_class_page():
                        name = quote(name_input.value or '학생')
                        student_id = quote(student_id_input.value or '000000')
                        ui.navigate.to(f'/class?name={name}&student_id={student_id}')

                    ui.button(
                        '로그인',
                        on_click=go_class_page
                    ).classes(
                        'w-full text-base sm:text-lg py-3 mt-4'
                    )

                    ui.label('※ 실제 인증 없이 학습 체험용으로 사용됩니다.').classes(
                        'text-xs text-gray-400 mt-3 text-center'
                    )

    show_logo_page()

    ui.timer(5.0, show_program_page, once=True)
    ui.timer(8.0, show_main_page, once=True)


@ui.page('/class')
def class_page(request: Request):
    name = request.query_params.get('name', '학생')
    student_id = request.query_params.get('student_id', '000000')

    with ui.column().classes('w-full min-h-screen bg-slate-50'):

        # 상단 헤더
        with ui.element('div').classes(
            'w-full min-h-[64px] sm:min-h-[76px] flex flex-col sm:flex-row '
            'items-start sm:items-center justify-between gap-3 px-4 sm:px-8 lg:px-10 '
            'py-4 sm:py-0 bg-white border-b border-slate-200'
        ):
            with ui.column().classes('gap-0'):
                ui.label('AMPhST Research Lab').classes(
                    'text-xl sm:text-2xl font-bold text-slate-800'
                )
                ui.label('아주대학교 의사과학자 양성사업단').classes(
                    'text-xs sm:text-sm text-slate-400'
                )

            with ui.row().classes('items-center gap-2 sm:gap-5 flex-wrap'):
                ui.label(f'{name} · {student_id}').classes(
                    'text-sm sm:text-base font-medium text-slate-600'
                )

                ui.button('한국어', icon='language').props('flat dense').classes(
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
            'w-full px-4 sm:px-8 lg:px-12 py-6 sm:py-10 gap-6 sm:gap-8'
        ):

            # 환영 영역
            with ui.card().classes(
                'w-full p-6 sm:p-10 rounded-3xl shadow-sm bg-white border border-slate-100'
            ):
                ui.label('WELCOME RESEARCHER').classes(
                    'text-xs sm:text-sm font-semibold tracking-widest text-blue-500'
                )

                with ui.row().classes('items-baseline gap-2 sm:gap-3 mt-3 flex-wrap'):
                    ui.label(f'{name}').classes(
                        'text-3xl sm:text-4xl font-semibold text-slate-900 leading-none'
                    )
                    ui.label('연구자님, 환영합니다.').classes(
                        'text-2xl sm:text-3xl font-semibold text-slate-700 leading-none'
                    )

                ui.label(
                    '임상 문제를 연구 질문으로 바꾸고, 연구 설계를 단계별로 완성해보세요.'
                ).classes(
                    'text-base sm:text-lg text-slate-500 mt-5'
                )

                with ui.row().classes('gap-2 sm:gap-3 mt-6 flex-wrap'):
                    ui.label('Research Design').classes(
                        'px-3 sm:px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-xs sm:text-sm font-medium'
                    )
                    ui.label('Clinical Data').classes(
                        'px-3 sm:px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-xs sm:text-sm font-medium'
                    )
                    ui.label('Ethics').classes(
                        'px-3 sm:px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-xs sm:text-sm font-medium'
                    )

            # 미션 카드 영역
            with ui.element('div').classes(
                'w-full grid grid-cols-1 md:grid-cols-3 gap-6'
            ):

                with ui.card().classes(
                    'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('Mission 01').classes(
                        'text-sm font-semibold text-blue-500'
                    )
                    ui.label('연구설계 실습').classes(
                        'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                    )
                    ui.label(
                        '연구 질문, 대상자, 변수, 분석 방법을 선택하며 연구 설계를 완성합니다.'
                    ).classes(
                        'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                    )
                    ui.space()
                    ui.button(
                        '시작하기',
                        icon='arrow_forward',
                        on_click=lambda: ui.navigate.to(
                            f'/genre?name={quote(name)}&student_id={quote(student_id)}'
                        )
                    ).classes(
                        'mt-6 w-full py-3 rounded-xl bg-blue-600 text-white'
                    )

                with ui.card().classes(
                    'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('Mission 02').classes(
                        'text-sm font-semibold text-emerald-500'
                    )
                    ui.label('데이터 해석 훈련').classes(
                        'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                    )
                    ui.label(
                        '가상의 임상 데이터를 보고 변수의 의미와 연구 결과를 해석합니다.'
                    ).classes(
                        'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                    )
                    ui.space()
                    ui.button('준비 중').props('outline').classes(
                        'mt-6 w-full py-3 rounded-xl text-slate-500'
                    )

                with ui.card().classes(
                    'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('Mission 03').classes(
                        'text-sm font-semibold text-purple-500'
                    )
                    ui.label('연구윤리 체크').classes(
                        'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                    )
                    ui.label(
                        'IRB, 개인정보, 비식별화, 연구대상자 보호 원칙을 점검합니다.'
                    ).classes(
                        'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                    )
                    ui.space()
                    ui.button('준비 중').props('outline').classes(
                        'mt-6 w-full py-3 rounded-xl text-slate-500'
                    )

                with ui.card().classes(
                    'w-full min-h-[220px] sm:min-h-[260px] p-6 sm:p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('Mission 04').classes(
                        'text-sm font-semibold text-rose-500'
                    )

                    ui.label('문제풀이 훈련').classes(
                        'text-xl sm:text-2xl font-bold text-slate-900 mt-3'
                    )

                    ui.label(
                        '연구 개념과 논문 내용을 바탕으로 핵심 문제를 풀며 이해도를 점검합니다.'
                    ).classes(
                        'text-sm sm:text-base text-slate-500 mt-3 leading-relaxed'
                    )

                    ui.space()

                    ui.button(
                        '시작하기',
                        icon='arrow_forward',
                        on_click=lambda: ui.navigate.to(
                            f'/quiz?name={quote(name)}&student_id={quote(student_id)}'
                        )
                    ).classes(
                        'mt-6 w-full py-3 rounded-xl bg-rose-600 text-white'
                    )
        

            # 하단 안내
            with ui.card().classes(
                'w-full p-5 sm:p-6 rounded-2xl bg-slate-100 shadow-none'
            ):
                ui.label(
                    '학습 기록은 실제 인증 없이 체험용으로만 표시됩니다.'
                ).classes(
                    'text-sm text-slate-500'
                )


@ui.page('/genre')
def genre_page(request: Request):
    name = request.query_params.get('name', '학생')
    student_id = request.query_params.get('student_id', '000000')

    fields = [
        {
            'key': 'molecular',
            'num': '01',
            'title': '분자생물학 연구실',
            'desc': '유전자, 단백질, 세포 기능을 분석해 질병의 원리를 탐구합니다.',
            'tag': 'Molecular Biology',
        },
        {
            'key': 'immune',
            'num': '02',
            'title': '면역학 연구실',
            'desc': '면역세포, 항체, 염증 반응을 바탕으로 치료 전략을 설계합니다.',
            'tag': 'Immunology',
        },
        {
            'key': 'precision',
            'num': '03',
            'title': '유전체·정밀의학 연구실',
            'desc': '유전체와 임상 정보를 활용해 개인 맞춤형 진단과 치료를 설계합니다.',
            'tag': 'Precision Medicine',
        },
        {
            'key': 'regeneration',
            'num': '04',
            'title': '줄기세포·재생의학 연구실',
            'desc': '줄기세포, 오가노이드, 생체재료를 활용한 질환 모델과 치료를 연구합니다.',
            'tag': 'Regenerative Medicine',
        },
        {
            'key': 'biomaterial',
            'num': '05',
            'title': '바이오소재 연구실',
            'desc': '나노기술을 활용해 약물전달, 표적치료, 진단 기술을 탐구합니다.',
            'tag': 'Nanobiotechnology',
        },
        {
            'key': 'digital',
            'num': '06',
            'title': '디지털 헬스 연구실',
            'desc': '웨어러블 디지털 기기와 생체신호를 활용해 건강 상태를 분석합니다.',
            'tag': 'Digital Health',
        },
    ]

    with ui.column().classes('w-full min-h-screen bg-slate-50'):

        # 상단 헤더
        with ui.element('div').classes(
            'w-full min-h-[60px] flex flex-col sm:flex-row items-start sm:items-center '
            'justify-between gap-3 px-4 sm:px-8 py-4 sm:py-0 bg-white border-b border-slate-200'
        ):
            with ui.column().classes('gap-0'):
                ui.label('AMPhST Research Library').classes(
                    'text-lg sm:text-xl font-bold text-slate-900'
                )
                ui.label('논문 기반 연구설계 미션 아카이브').classes(
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
            'w-full px-4 sm:px-8 lg:px-10 py-6 sm:py-8'
        ):

            ui.label('SELECT RESEARCH FIELD').classes(
                'text-xs font-semibold tracking-widest text-blue-500'
            )

            ui.label('연구 분야를 선택하세요').classes(
                'text-2xl sm:text-3xl font-extrabold text-slate-900 mt-2'
            )

            ui.label(
                '관심 있는 연구 분야를 선택하면 기존 논문 기반 연구설계 미션으로 이동합니다.'
            ).classes(
                'text-sm sm:text-base text-slate-500 mt-3'
            )

            # 연구 분야 목록
            with ui.column().classes('w-full gap-3 mt-7'):

                for field in fields:
                    with ui.element('div').classes(
                        'w-full flex flex-col sm:flex-row sm:items-center sm:justify-between '
                        'gap-4 px-5 sm:px-6 py-4 rounded-2xl '
                        'bg-white border border-slate-100 shadow-sm '
                        'transition-all duration-300 hover:shadow-md hover:-translate-y-1 hover:border-blue-200'
                    ):

                        with ui.row().classes('items-start gap-4 w-full min-w-0'):
                            ui.label(field['num']).classes(
                                'text-xl sm:text-2xl font-extrabold text-slate-300 w-[44px] sm:w-[54px] shrink-0'
                            )

                            with ui.column().classes('flex-1 min-w-0 gap-1'):
                                with ui.row().classes('items-center gap-2 flex-wrap'):
                                    ui.label(field['title']).classes(
                                        'text-lg sm:text-xl font-bold text-slate-900'
                                    )

                                    ui.label(field['tag']).classes(
                                        'text-[10px] font-semibold text-blue-500 bg-blue-50 px-2 py-1 rounded-full'
                                    )

                                ui.label(field['desc']).classes(
                                    'text-sm text-slate-500 mt-1'
                                )

                        ui.button(
                            '입장',
                            icon='arrow_forward',
                            on_click=lambda f=field: ui.navigate.to(
                                f"/missions?lab={f['key']}&name={quote(name)}&student_id={quote(student_id)}"
                            )
                        ).props('flat dense').classes(
                            'w-fit sm:ml-auto text-blue-600 font-semibold text-sm'
                        )


@ui.page('/missions')
def missions_page(request: Request):
    name = request.query_params.get('name', '학생')
    student_id = request.query_params.get('student_id', '000000')
    lab = request.query_params.get('lab', 'immune')

    lab_titles = {
        'immune': '면역학 연구실',
        'molecular': '분자생물학 연구실',
        'precision': '유전체·정밀의학 연구실',
        'regeneration': '줄기세포·재생의학 연구실',
        'biomaterial': '바이오소재 연구실',
        'digital': '디지털 헬스 연구실',
    }

    default_missions = [
        {
            'question': '이 연구 분야의 첫 번째 논문 기반 질문은 무엇일까?',
            'author': 'Research Team',
            'year': '2026',
            'tags': ['준비중', '연구설계', '논문기반'],
            'visual': '📚',
            'color': 'bg-slate-50',
        },
    ]

    missions_by_lab = {
        'immune': [
            {
                'question': '내 몸을 공격하는 면역세포만 골라서 멈출 수 있을까?',
                'author': 'Mackensen et al.',
                'year': '2022',
                'tags': ['자가면역질환', '루푸스', 'CAR-T', 'B세포'],
                'visual': '🛡️',
                'color': 'bg-blue-50',
            },
            {
                'question': '난치성 루푸스에서 CD19 CAR-T 치료는 자가면역 반응을 재설정할 수 있을까?',
                'author': 'Mackensen et al.',
                'year': '2022',
                'tags': ['SLE', 'CD19', 'CAR-T', '자가항체'],
                'visual': '🧬',
                'color': 'bg-indigo-50',
            },
            {
                'question': '면역관용은 왜 무너지고, Treg은 이를 다시 회복시킬 수 있을까?',
                'author': 'Brunkow et al.',
                'year': '2001',
                'tags': ['Treg', 'FOXP3', '면역관용', '자가면역'],
                'visual': '⚖️',
                'color': 'bg-emerald-50',
            },
            {
                'question': 'CAR-Treg은 무차별적 면역억제 대신 원하는 조직만 조절할 수 있을까?',
                'author': 'Sakaguchi et al.',
                'year': '1995',
                'tags': ['CAR-Treg', '항원특이성', '면역조절', '정밀치료'],
                'visual': '🎯',
                'color': 'bg-purple-50',
            },
        ],
        'molecular': [
            {
                'question': '암세포는 왜 멈추라는 신호를 무시할까?',
                'author': 'Lee et al.',
                'year': '2022',
                'tags': ['유전자발현', '암세포', '세포신호'],
                'visual': '🧫',
                'color': 'bg-blue-50',
            },
            {
                'question': '단백질 하나의 변화가 질병을 만들 수 있을까?',
                'author': 'Kim et al.',
                'year': '2023',
                'tags': ['단백질기능', '돌연변이', '질병기전'],
                'visual': '🧩',
                'color': 'bg-emerald-50',
            },
        ],
        'precision': [
            {
                'question': '왜 같은 약을 써도 사람마다 치료 반응이 다를까?',
                'author': 'Park et al.',
                'year': '2023',
                'tags': ['정밀의학', '약물반응', '유전체'],
                'visual': '🧬',
                'color': 'bg-indigo-50',
            },
        ],
        'regeneration': [
            {
                'question': '작은 오가노이드로 실제 질병을 재현할 수 있을까?',
                'author': 'Han et al.',
                'year': '2024',
                'tags': ['오가노이드', '줄기세포', '질환모델'],
                'visual': '🧫',
                'color': 'bg-emerald-50',
            },
        ],
        'biomaterial': [
            {
                'question': '약을 아픈 부위에만 정확히 보낼 수 있을까?',
                'author': 'Choi et al.',
                'year': '2023',
                'tags': ['나노입자', '약물전달', '표적치료'],
                'visual': '🧪',
                'color': 'bg-orange-50',
            },
        ],
        'digital': [
            {
                'question': '웨어러블 기기는 몸의 이상 신호를 얼마나 빨리 알아챌 수 있을까?',
                'author': 'Kim et al.',
                'year': '2024',
                'tags': ['웨어러블', '생체신호', '디지털헬스'],
                'visual': '⌚',
                'color': 'bg-cyan-50',
            },
        ],
    }

    lab_title = lab_titles.get(lab, '연구실')
    missions = missions_by_lab.get(lab, default_missions)

    with ui.column().classes('w-full min-h-screen bg-slate-50'):

        # 상단 헤더
        with ui.element('div').classes(
            'w-full min-h-[64px] flex flex-col sm:flex-row items-start sm:items-center '
            'justify-between gap-3 px-4 sm:px-8 py-4 sm:py-0 bg-white border-b border-slate-200'
        ):
            with ui.column().classes('gap-0'):
                ui.label('AMPhST Research Missions').classes(
                    'text-lg sm:text-xl font-bold text-slate-900'
                )
                ui.label(lab_title).classes(
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
                        f'/genre?name={quote(name)}&student_id={quote(student_id)}'
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
            'w-full px-4 sm:px-8 lg:px-10 py-6 sm:py-8'
        ):

            ui.label(lab_title).classes(
                'text-2xl sm:text-3xl font-extrabold text-slate-900'
            )

            ui.label(
                '논문에서 출발한 연구 질문입니다. 궁금한 질문을 선택해 연구 설계를 시작하세요.'
            ).classes(
                'text-sm sm:text-base text-slate-500 mt-3'
            )

            # 검색 / 정렬 영역
            with ui.element('div').classes(
                'w-full flex flex-col sm:flex-row sm:items-center sm:justify-end mt-6 gap-3'
            ):
                ui.input(
                    placeholder='검색'
                ).props(
                    'outlined dense clearable'
                ).classes(
                    'w-full sm:w-[260px] bg-white'
                )

                ui.select(
                    options=['최신순', '논문연도순', '저자명순'],
                    value='최신순'
                ).props(
                    'outlined dense'
                ).classes(
                    'w-full sm:w-[150px] bg-white'
                )

            # 카드 그리드
            with ui.element('div').classes(
                'w-full grid grid-cols-1 xl:grid-cols-2 gap-6 mt-6 sm:mt-8'
            ):

                for mission in missions:

                    with ui.card().classes(
                        'w-full min-h-[270px] rounded-3xl overflow-hidden '
                        'shadow-sm border border-slate-100 bg-white '
                        'transition-all duration-300 hover:shadow-md hover:-translate-y-1 cursor-pointer'
                    ):

                        with ui.element('div').classes(
                            'w-full h-full flex flex-col md:flex-row'
                        ):

                            # 왼쪽 정보 영역
                            with ui.column().classes(
                                'flex-1 min-w-0 p-5 sm:p-7 justify-between gap-6'
                            ):

                                # 질문 영역
                                with ui.column().classes('gap-3'):
                                    ui.label('QUESTION').classes(
                                        'text-xs font-semibold tracking-widest text-blue-500'
                                    )

                                    ui.label(mission['question']).classes(
                                        'text-xl sm:text-[26px] font-bold text-slate-900 leading-snug break-keep'
                                    )

                                # 논문 정보 + 태그 + 버튼
                                with ui.column().classes('gap-4'):

                                    ui.separator()

                                    with ui.row().classes(
                                        'w-full items-end justify-between gap-4'
                                    ):
                                        with ui.column().classes('gap-0'):
                                            ui.label('Based on Paper').classes(
                                                'text-xs text-slate-400'
                                            )
                                            ui.label(mission['author']).classes(
                                                'text-sm font-semibold text-slate-700'
                                            )

                                        ui.label(mission['year']).classes(
                                            'text-sm font-bold text-slate-400'
                                        )

                                    with ui.row().classes(
                                        'w-full flex-wrap gap-2'
                                    ):
                                        for tag in mission['tags']:
                                            ui.label(f'#{tag}').classes(
                                                'text-xs text-slate-500 bg-slate-100 px-2 py-1 rounded-full whitespace-nowrap'
                                            )

                                    ui.button(
                                        '이 질문으로 시작하기',
                                        icon='arrow_forward',
                                        on_click=lambda m=mission: ui.notify(
                                            f"{m['question']} 미션을 선택했습니다."
                                        )
                                    ).props('flat dense').classes(
                                        'w-fit text-blue-600 text-sm font-semibold px-0'
                                    )

                            # 오른쪽 그림 영역
                            with ui.column().classes(
                                f"w-full md:w-[34%] min-h-[110px] md:min-h-full "
                                f"items-center justify-center {mission['color']}"
                            ):
                                ui.label(mission['visual']).classes(
                                    'text-5xl sm:text-6xl md:text-7xl'
                                )

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

                    with ui.card().classes(
                        f'w-full rounded-2xl overflow-hidden bg-white border border-slate-100 '
                        f'shadow-sm transition-all duration-300 hover:shadow-md {disabled_style}'
                    ):
                        with ui.element('div').classes(
                            'w-full flex flex-col sm:flex-row'
                        ):

                            # 왼쪽 색상 바
                            ui.element('div').classes(
                                f'w-full h-[5px] sm:w-[6px] sm:h-auto {paper["accent"]}'
                            )

                            # 본문
                            with ui.column().classes(
                                'flex-1 min-w-0 p-5 gap-3'
                            ):

                                # 상단 상태 / 문항 수
                                with ui.row().classes(
                                    'w-full items-center justify-between gap-3'
                                ):
                                    if paper['status'] == '안 푼 문제':
                                        ui.label('안 푼 문제').classes(
                                            'text-xs font-semibold text-sky -700 bg-sky-50 px-3 py-1 rounded-full'
                                        )
                                    elif paper['status'] == '푼 문제':
                                        ui.label('푼 문제').classes(
                                            'text-xs font-semibold text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full'
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
                                        ui.button(
                                            '문제 풀기',
                                            icon='arrow_forward',
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
    }

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

                        ui.label(
                            f"{len(questions)}문항 중 {state['score']}문항을 완료했습니다."
                        ).classes(
                            'text-lg text-slate-600 mt-5'
                        )

                        score_percent = int((state['score'] / len(questions)) * 100)

                        ui.linear_progress(
                            value=state['score'] / len(questions)
                        ).classes(
                            'w-full mt-6'
                        )

                        ui.label(f'완료율 {score_percent}%').classes(
                            'text-sm text-slate-400 mt-2'
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

                            def check_answer():
                                if not answer_input.value or not answer_input.value.strip():
                                    ui.notify('답변을 먼저 입력해 주세요.')
                                    return

                                feedback_area.clear()

                                student_answer = answer_input.value.strip()
                                key_points = question.get('key_points', [])

                                matched_points = [
                                    point for point in key_points
                                    if point.lower() in student_answer.lower()
                                ]

                                if not state['answered']:
                                    state['selected_answers'].append(student_answer)
                                    state['score'] += 1
                                    state['answered'] = True

                                with feedback_area:
                                    with ui.card().classes(
                                        'w-full p-4 rounded-2xl bg-sky-50 shadow-none'
                                    ):
                                        ui.label('피드백').classes(
                                            'text-sm font-bold text-sky-700'
                                        )

                                        if matched_points:
                                            ui.label(
                                                f"좋습니다. 답변에 {', '.join(matched_points)} 개념이 포함되어 있습니다."
                                            ).classes(
                                                'text-sm text-slate-700 mt-2 leading-relaxed'
                                            )
                                        else:
                                            ui.label(
                                                '핵심 개념이 충분히 드러나지는 않았지만, 답변 방향을 확인했습니다.'
                                            ).classes(
                                                'text-sm text-slate-700 mt-2 leading-relaxed'
                                            )

                                        ui.label(question['feedback']).classes(
                                            'text-sm text-slate-700 mt-2 leading-relaxed'
                                        )

                                        ui.separator().classes('my-3')

                                        ui.label('예시 답안').classes(
                                            'text-xs font-semibold text-slate-400'
                                        )
                                        ui.label(question['sample_answer']).classes(
                                            'text-sm text-slate-600 mt-1 leading-relaxed'
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

                                if not state['answered']:
                                    state['selected_answers'].append(answer_radio.value)
                                    if is_correct:
                                        state['score'] += 1
                                    state['answered'] = True

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
                                ui.notify('정답 확인 또는 피드백 확인을 먼저 눌러주세요.')
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
                                '피드백 확인' if question_type == 'short' else '정답 확인',
                                icon='rate_review' if question_type == 'short' else 'check',
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


port = int(os.environ.get('PORT', 8080))
ui.run(host='0.0.0.0', port=port)