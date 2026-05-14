from urllib.parse import quote
from fastapi import Request
from nicegui import ui


def register_missions_page():


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