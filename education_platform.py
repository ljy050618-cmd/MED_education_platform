import os
from urllib.parse import quote
from fastapi import Request
from nicegui import ui, app

# 이미지 폴더 등록
app.add_static_files('/education_images', 'education_images')


@ui.page('/')
def index():

    # 한 화면만 담는 컨테이너
    with ui.column().classes(
        'w-full h-screen items-center justify-center bg-white'
    ) as page:

        pass

    def show_logo_page():
        page.clear()

        with page:
            with ui.row().classes('items-center justify-center gap-4'):
                ui.image('/education_images/Ajou_logo.png').classes(
                    'w-[68px] h-[68px]'
                )

                with ui.row().classes('items-center gap-4'):

                    # 왼쪽 글자
                    with ui.column().classes('gap-0 items-end'):
                        ui.label('아주대학교').classes(
                            'text-4xl font-bold text-gray-900 leading-tight'
                        )
                        ui.label('AJOU UNIVERSITY').classes(
                            'text-xl font-semibold text-gray-700 leading-tight'
                        )

                    # 가운데 세로선
                    ui.element('div').classes(
                        'w-[2px] h-[72px] bg-gray-400'
                    )

                    # 오른쪽 글자
                    with ui.column().classes('gap-0 items-start'):
                        ui.label('의과대학').classes(
                            'text-4xl font-bold text-gray-900 leading-tight'
                        )
                        ui.label('School of Medicine').classes(
                            'text-xl font-semibold text-gray-700 leading-tight'
                        )

    def show_program_page():
        page.clear()

        with page:
            ui.label('아주대학교 의사과학자 양성사업단').classes(
                'text-3xl font-semibold text-gray-400'
            )

            ui.label('AMPhST 프로그램').classes(
                'text-5xl font-bold text-gray-400 mt-4'
            )

            ui.label('의사과학자 연구설계 랩을 준비하고 있습니다').classes(
                'text-lg text-gray-400 mt-10'
            )

            ui.spinner(size='lg').classes('mt-2')

    def show_main_page():
        page.clear()
        
        with page:
        # 메인 페이지 안에서 좌측 상단 배치를 위해 relative 적용
            with ui.column().classes(
                'relative w-full h-screen items-center justify-center bg-white'
            ):

            # 좌측 상단 사업단 문구
                with ui.column().classes(
                  'absolute top-8 left-8 items-start gap-1 text-left'
                ):
                    ui.label('아주대학교 의사과학자 양성사업단').classes(
                        'text-base font-medium text-gray-400'
                    )
                    ui.label('AMPhST 프로그램').classes(
                        'text-xl font-semibold text-gray-400'
                    )

            # 중앙 메인 콘텐츠
                ui.label('의사과학자 연구설계 랩').classes(
                    'text-4xl font-bold text-gray-900'
                )

                ui.label('학생이 연구자 입장에서 연구 설계를 체험하는 학습용 사이트입니다.').classes(
                    'text-lg text-gray-600 mt-3'
                )

                ui.button('연구 미션 시작하기', on_click=show_login_page).classes(
                    'text-lg px-6 py-3 mt-6'
                )    



    def show_login_page():
        page.clear()

        with page:
            with ui.column().classes(
                'relative w-full h-screen items-center justify-start bg-white pt-60' 
            ):
            # 좌측 상단 사업단 문구
                with ui.column().classes(
                    'absolute top-8 left-8 items-start gap-1 text-left'
                ):
                    ui.label('아주대학교 의사과학자 양성사업단').classes(
                        'text-base font-medium text-gray-400'
                )
                    ui.label('AMPhST 프로그램').classes(
                        'text-xl font-semibold text-gray-400'
                )

            # 로그인 형식 카드
                with ui.card().classes(
                    'w-[420px] max-w-[90vw] p-8 rounded-2xl shadow-lg items-center'
                ):
                    ui.label('연구자 로그인').classes(
                        'text-3xl font-bold text-gray-900 text-center'
                )

                    ui.label('학습 체험을 위해 정보를 입력하세요.').classes(
                        'text-base text-gray-500 text-center mt-2'
                )

                    name_input = ui.input('이름').classes(
                        'w-full mt-6'
                    )

                    email_input = ui.input('이메일').classes(
                        'w-full'
                    )

                    student_id_input = ui.input('학번 또는 참가번호').classes(
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
                        'w-full text-lg py-3 mt-4'
                    )

                    ui.label('※ 실제 인증 없이 학습 체험용으로 사용됩니다.').classes(
                        'text-xs text-gray-400 mt-3 text-center'
                    )

    # 처음 화면
    show_logo_page()

    # 5초 뒤 중간 화면
    ui.timer(5.0, show_program_page, once=True)

    # 8초 뒤 메인 화면
    ui.timer(8.0, show_main_page, once=True)

@ui.page('/class')
def class_page(request: Request):
    name = request.query_params.get('name', '학생')
    student_id = request.query_params.get('student_id', '000000')

    with ui.column().classes('w-full min-h-screen bg-slate-50'):

        # 상단 헤더
        with ui.row().classes(
            'w-full h-[76px] items-center justify-between px-10 bg-white border-b border-slate-200'
        ):
            with ui.column().classes('gap-0'):
                ui.label('AMPhST Research Lab').classes(
                    'text-2xl font-bold text-slate-800'
                )
                ui.label('아주대학교 의사과학자 양성사업단').classes(
                    'text-sm text-slate-400'
                )

            with ui.row().classes('items-center gap-5'):
                ui.label(f'{name}  ·  {student_id}').classes(
                    'text-base font-medium text-slate-600'
                )

                ui.button('한국어', icon='language').props('flat').classes(
                    'text-slate-500'
                )

                ui.button(
                    '로그아웃',
                    icon='logout',
                    on_click=lambda: ui.navigate.to('/')
                ).props('flat').classes(
                    'text-slate-500'
                )

        # 본문
        with ui.column().classes('w-full px-12 py-10 gap-8'):

                # 환영 영역
            with ui.card().classes(
                'w-full p-10 rounded-3xl shadow-sm bg-white border border-slate-100'
            ):
                ui.label('WELCOME RESEARCHER').classes(
                    'text-sm font-semibold tracking-widest text-blue-500'
                )

                with ui.row().classes('items-baseline gap-3 mt-3'):
                    ui.label(f'{name}').classes(
                        'text-4xl font-semibold text-slate-900 leading-none'
                    )
                    ui.label('연구자님, 환영합니다.').classes(
                        'text-3xl font-semibold text-slate-700 leading-none'
                    )

                ui.label(
                    '임상 문제를 연구 질문으로 바꾸고, 연구 설계를 단계별로 완성해보세요.'
                ).classes(
                    'text-lg text-slate-500 mt-5'
                )

                with ui.row().classes('gap-3 mt-6'):
                    ui.label('Research Design').classes(
                        'px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-sm font-medium'
                    )
                    ui.label('Clinical Data').classes(
                        'px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-sm font-medium'
                    )
                    ui.label('Ethics').classes(
                        'px-4 py-2 rounded-full bg-slate-100 text-slate-600 text-sm font-medium'
                    )       

            # 미션 카드 영역
            with ui.row().classes('w-full gap-6 flex-nowrap'):

                with ui.card().classes(
                    'flex-1 min-h-[260px] p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('Mission 01').classes(
                        'text-sm font-semibold text-blue-500'
                    )
                    ui.label('연구설계 실습').classes(
                        'text-2xl font-bold text-slate-900 mt-3'
                    )
                    ui.label(
                        '연구 질문, 대상자, 변수, 분석 방법을 선택하며 연구 설계를 완성합니다.'
                    ).classes(
                        'text-base text-slate-500 mt-3 leading-relaxed'
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
                    'flex-1 min-h-[260px] p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('Mission 02').classes(
                        'text-sm font-semibold text-emerald-500'
                    )
                    ui.label('데이터 해석 훈련').classes(
                        'text-2xl font-bold text-slate-900 mt-3'
                    )
                    ui.label(
                        '가상의 임상 데이터를 보고 변수의 의미와 연구 결과를 해석합니다.'
                    ).classes(
                        'text-base text-slate-500 mt-3 leading-relaxed'
                    )
                    ui.space()
                    ui.button('준비 중').props('outline').classes(
                        'mt-6 w-full py-3 rounded-xl text-slate-500'
                    )

                with ui.card().classes(
                    'flex-1 min-h-[260px] p-7 rounded-3xl shadow-sm bg-white border border-slate-100'
                ):
                    ui.label('Mission 03').classes(
                        'text-sm font-semibold text-purple-500'
                    )
                    ui.label('연구윤리 체크').classes(
                        'text-2xl font-bold text-slate-900 mt-3'
                    )
                    ui.label(
                        'IRB, 개인정보, 비식별화, 연구대상자 보호 원칙을 점검합니다.'
                    ).classes(
                        'text-base text-slate-500 mt-3 leading-relaxed'
                    )
                    ui.space()
                    ui.button('준비 중').props('outline').classes(
                        'mt-6 w-full py-3 rounded-xl text-slate-500'
                    )

            # 하단 안내
            with ui.card().classes(
                'w-full p-6 rounded-2xl bg-slate-100 shadow-none'
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
            'title': '디지털 헬스 연구',
            'desc': '웨어러블한 디지털 기기를 개발합니다.',
            'tag': 'Digital Health',
        }
        
           
    ]

    with ui.column().classes('w-full min-h-screen bg-slate-50'):

        # 상단 헤더
        with ui.row().classes(
            'w-full h-[60px] items-center justify-between px-8 bg-white border-b border-slate-200'
        ):
            with ui.column().classes('gap-0'):
                ui.label('AMPhST Research Library').classes(
                    'text-xl font-bold text-slate-900'
                )
                ui.label('논문 기반 연구설계 미션 아카이브').classes(
                    'text-xs text-slate-400'
                )

            with ui.row().classes('items-center gap-3'):
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
        with ui.column().classes('w-full px-10 py-8'):

            ui.label('SELECT RESEARCH FIELD').classes(
                'text-xs font-semibold tracking-widest text-blue-500'
            )

            ui.label('연구 분야를 선택하세요').classes(
                'text-3xl font-extrabold text-slate-900 mt-2'
            )

            ui.label(
                '관심 있는 연구 분야를 선택하면 기존 논문 기반 연구설계 미션으로 이동합니다.'
            ).classes(
                'text-base text-slate-500 mt-3'
            )

            # 연구 분야 목록
            with ui.column().classes('w-full gap-3 mt-7'):

                for field in fields:
                    with ui.row().classes(
                        'w-full items-center justify-between px-6 py-4 rounded-2xl '
                        'bg-white border border-slate-100 shadow-sm '
                        'transition-all duration-300 hover:shadow-md hover:-translate-y-1 hover:border-blue-200'
                    ):

                        # 번호
                        ui.label(field['num']).classes(
                            'text-2xl font-extrabold text-slate-300 w-[54px]'
                        )

                        # 제목과 설명
                        with ui.column().classes('flex-1 gap-0'):
                            with ui.row().classes('items-center gap-2'):
                                ui.label(field['title']).classes(
                                    'text-xl font-bold text-slate-900'
                                )

                                ui.label(field['tag']).classes(
                                    'text-[10px] font-semibold text-blue-500 bg-blue-50 px-2 py-1 rounded-full'
                                )

                            ui.label(field['desc']).classes(
                                'text-sm text-slate-500 mt-1'
                            )

                        # 입장 버튼
                        ui.button(
                            '입장',
                            icon='arrow_forward',
                            on_click=lambda f=field: ui.navigate.to(
                                f"/missions?lab={f['key']}&name={quote(name)}&student_id={quote(student_id)}"
                            )
                        ).props('flat dense').classes(
                            'text-blue-600 font-semibold text-sm'
                        )

@ui.page('/missions')
def missions_page(request: Request):
    name = request.query_params.get('name', '학생')
    student_id = request.query_params.get('student_id', '000000')
    lab = request.query_params.get('lab', 'immune')

    lab_titles = {
        'immune': '면역·감염 연구실',
        'molecular': '분자생물학 연구실',
        'precision': '정밀치료 연구실',
        'regeneration': '재생의학 연구실',
        'biomaterial': '바이오소재 연구실',
        'digital': '디지털 헬스 연구실',
    }

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
                'question': '내 몸을 공격하는 면역세포만 골라서 멈출 수 있을까?',
                'author': 'Kim et al.',
                'year': '2023',
                'tags': ['면역세포', '자가염증질환', '표적'],
                'visual': '🧩',
                'color': 'bg-emerald-50',
            },
        ],
    }

    lab_title = lab_titles.get(lab, '연구실')
    missions = missions_by_lab.get(lab, missions_by_lab['immune'])

    with ui.column().classes('w-full min-h-screen bg-slate-50'):

        # 상단 헤더
        with ui.row().classes(
            'w-full h-[64px] items-center justify-between px-8 bg-white border-b border-slate-200'
        ):
            with ui.column().classes('gap-0'):
                ui.label('AMPhST Research Missions').classes(
                    'text-xl font-bold text-slate-900'
                )
                ui.label(lab_title).classes(
                    'text-xs text-slate-400'
                )

            with ui.row().classes('items-center gap-3'):
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
        with ui.column().classes('w-full px-10 py-8'):

            ui.label(lab_title).classes(
                'text-3xl font-extrabold text-slate-900'
            )

            ui.label(
                '논문에서 출발한 연구 질문입니다. 궁금한 질문을 선택해 연구 설계를 시작하세요.'
            ).classes(
                'text-base text-slate-500 mt-3'
            )

            # 검색 / 정렬 영역

            with ui.row().classes(
                'w-full items-center justify-end mt-6 gap-3'
            ):
                ui.input(
                    placeholder='검색'
                ).props(
                    'outlined dense clearable'
                ).classes(
                    'w-[260px] bg-white'
                )

                ui.select(
                    options=['최신순', '논문연도순', '저자명순'],
                    value='최신순'
                ).props(
                    'outlined dense'
                ).classes(
                    'w-[150px] bg-white'
                )

            # 카드 그리드: 화면이 작으면 1열, 넓으면 2열
            with ui.element('div').classes(
                'w-full grid grid-cols-1 xl:grid-cols-2 gap-6 mt-8'
            ):

                for mission in missions:

                    with ui.card().classes(
                        'w-full min-h-[270px] rounded-3xl overflow-hidden '
                        'shadow-sm border border-slate-100 bg-white '
                        'transition-all duration-300 hover:shadow-md hover:-translate-y-1 cursor-pointer'
                    ):

                        # 카드 내부: 큰 화면에서는 좌우, 작은 화면에서는 위아래
                        with ui.element('div').classes(
                            'w-full h-full flex flex-col md:flex-row'
                        ):

                            # 왼쪽 정보 영역
                            with ui.column().classes(
                                'flex-1 min-w-0 p-7 justify-between gap-6'
                            ):

                                # 질문 영역
                                with ui.column().classes('gap-3'):
                                    ui.label('QUESTION').classes(
                                        'text-xs font-semibold tracking-widest text-blue-500'
                                    )

                                    ui.label(mission['question']).classes(
                                        'text-[26px] font-bold text-slate-900 leading-snug break-keep'
                                    )

                                # 논문 정보 + 태그 + 버튼
                                with ui.column().classes('gap-4'):

                                    ui.separator()

                                    # 논문 정보
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

                                    # 태그
                                    with ui.row().classes(
                                        'w-full flex-wrap gap-2'
                                    ):
                                        for tag in mission['tags']:
                                            ui.label(f'#{tag}').classes(
                                                'text-xs text-slate-500 bg-slate-100 px-2 py-1 rounded-full whitespace-nowrap'
                                            )

                                    # 버튼
                                    ui.button(
                                        '이 질문으로 시작하기',
                                        icon='arrow_forward',
                                        on_click=lambda m=mission: ui.notify(
                                            f"{m['question']} 미션을 선택했습니다."
                                        )
                                    ).props('flat dense').classes(
                                        'w-fit text-blue-600 text-sm font-semibold px-0'
                                    )

                            # 오른쪽 그림 영역: 카드 위아래로 길게 연결
                            with ui.column().classes(
                                f"w-full md:w-[34%] min-h-[140px] md:min-h-full "
                                f"items-center justify-center {mission['color']}"
                            ):
                                ui.label(mission['visual']).classes(
                                    'text-6xl md:text-7xl'
                                )

port = int(os.environ.get('PORT', 8080))
ui.run(host='0.0.0.0', port=port)